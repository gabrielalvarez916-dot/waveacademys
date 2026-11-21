-- MÁQUINA DEL NIVEL MEDIO · funciones propias en la base (separadas de las del Avanzado).
-- No modifica ninguna función, tabla ni dato existente: solo CREA piezas nuevas con nombre *_medio.
-- Todas rechazan cualquier materia que no sea del Nivel Medio, así nunca pueden tocar el Avanzado.
-- No usan lesson_drafts ni fabrica-pdf: el proceso de PDFs del Avanzado nunca ve nada del Medio.

-- 1) clave propia de la máquina del Medio (la del Avanzado sigue siendo otra)
insert into public.gen_config (clave, valor)
select 'medio_token', encode(extensions.gen_random_bytes(24), 'hex')
where not exists (select 1 from public.gen_config where clave = 'medio_token');

-- 2) ¿esta materia es del Nivel Medio?
create or replace function private.medio_es_materia(p_subject uuid) returns boolean
language sql stable security definer set search_path to 'public' as $$
  select exists (select 1 from subjects s join grades g on g.id = s.grade_id join levels lv on lv.id = g.level_id
                 where s.id = p_subject and lv.name = 'Nivel Medio');
$$;

-- 3) cargar una misión del Medio: actividades de cada nivel, Relámpago (lección 5) y examen "Nivel jefe" (sin publicar).
--    El PDF NO va por acá: lo sube la función pdf-medio. No crea borradores (lesson_drafts).
create or replace function public.cargar_mision_medio(p_token text, p jsonb) returns text
language plpgsql security definer set search_path to 'public' as $$
declare t record; lec uuid; l1 uuid; paso uuid; qid uuid; ex uuid; k text; x jsonb; i int; par jsonb;
begin
  if p_token is null or p_token is distinct from (select valor from gen_config where clave = 'medio_token') then raise exception 'token inválido'; end if;
  if not private.medio_es_materia((p->>'subject_id')::uuid) then raise exception 'Esa materia no es del Nivel Medio: esta función no la toca'; end if;
  select id, version into t from topics where subject_id = (p->>'subject_id')::uuid and position = (p->>'tema')::int and coalesce(solo_para, '') <> 'internacional' limit 1;
  if t.id is null then raise exception 'No existe la misión % en esa materia', p->>'tema'; end if;
  if coalesce(t.version, 'comun') <> 'comun' then raise exception 'La misión % es "%": la máquina del Medio por ahora carga solo misiones comunes', p->>'tema', t.version; end if;
  -- lección 5 (práctica general, con el Relámpago) con los mismos pasos que la lección 1, si todavía no existe
  if not exists (select 1 from lessons where topic_id = t.id and position = 5) then
    select id into l1 from lessons where topic_id = t.id and position = 1;
    insert into lessons (topic_id, title, position, is_published) values (t.id, p->>'practica', 5, false) returning id into lec;
    insert into lesson_steps (lesson_id, step_type, title, position, content)
      select lec, s.step_type, s.title, s.position, '{}'::jsonb from lesson_steps s where s.lesson_id = l1;
  end if;
  -- actividades por consigna de cada lección
  for k in select jsonb_object_keys(p->'act') loop
    select s.id into paso from lesson_steps s join lessons l on l.id = s.lesson_id where l.topic_id = t.id and l.position = k::int and s.step_type = 'final_activity';
    if paso is null then raise exception 'La lección % no tiene el paso de actividad', k; end if;
    if exists (select 1 from questions where lesson_step_id = paso) then raise exception 'La lección % ya tiene actividades: no se pisan', k; end if;
    i := 0;
    for x in select * from jsonb_array_elements(p->'act'->k) loop
      i := i + 1;
      insert into questions (lesson_step_id, question_type, prompt, options, points, position, tiempo_seg, neutro)
        values (paso, (x->>'t')::question_type, x->>'p', x->'o', 1, i, (x->>'tiempo')::smallint, x->'neutro') returning id into qid;
      insert into question_rubrics (question_id, reference_answer, explanation) values (qid, x->'r', x->>'e');
    end loop;
  end loop;
  -- examen "Nivel jefe" (sin publicar)
  if exists (select 1 from exams where topic_id = t.id) then raise exception 'La misión ya tiene examen: no se pisa'; end if;
  insert into exams (topic_id, title, passing_score, preguntas_por_intento, publicado) values (t.id, p->>'examen_titulo', 70, 5, false) returning id into ex;
  i := 0;
  for par in select * from jsonb_array_elements(p->'examen') loop
    i := i + 1; x := par->1;
    insert into questions (exam_id, lesson_id, question_type, prompt, options, points, position, neutro)
      values (ex, (select id from lessons where topic_id = t.id and position = (par->>0)::int), (x->>'t')::question_type, x->>'p', x->'o', 1, i, x->'neutro') returning id into qid;
    insert into question_rubrics (question_id, reference_answer, explanation) values (qid, x->'r', x->>'e');
  end loop;
  return 'ok';
end $$;

-- 4) cargar una clase animada del Medio en el paso de video de su nivel (o en la introducción de la materia)
create or replace function public.cargar_clase_medio(p_token text, p_html text, p_step_id uuid default null, p_subject_id uuid default null, p_neutro boolean default false) returns text
language plpgsql security definer set search_path to 'public' as $$
declare n int := 0; suj uuid;
begin
  if p_token is null or p_token is distinct from (select valor from gen_config where clave = 'medio_token') then raise exception 'token inválido'; end if;
  if p_html is null or p_html not like '<!doctype html>%' then raise exception 'html inválido'; end if;
  if p_step_id is not null then
    select t.subject_id into suj from lesson_steps s join lessons l on l.id = s.lesson_id join topics t on t.id = l.topic_id where s.id = p_step_id;
    if not coalesce(private.medio_es_materia(suj), false) then raise exception 'Ese paso no es del Nivel Medio: esta función no lo toca'; end if;
    update lesson_steps set content = coalesce(content, '{}'::jsonb) || case when p_neutro then jsonb_build_object('clase_html_neutro', p_html) else jsonb_build_object('clase', true, 'clase_html', p_html) end
      where id = p_step_id and step_type = 'video';
    get diagnostics n = row_count;
  elsif p_subject_id is not null then
    if not private.medio_es_materia(p_subject_id) then raise exception 'Esa materia no es del Nivel Medio: esta función no la toca'; end if;
    if p_neutro then update subjects set intro_clase_html_neutro = p_html where id = p_subject_id;
    else update subjects set intro_clase = true, intro_clase_html = p_html where id = p_subject_id; end if;
    get diagnostics n = row_count;
  end if;
  return case when n = 1 then 'ok' else 'no encontrado' end;
end $$;
