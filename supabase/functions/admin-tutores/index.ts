import { createClient } from "npm:@supabase/supabase-js@2";

// Alta de tutores (solo el administrador). POST { nombre, email } -> crea la cuenta con rol tutor y una clave inicial.
const cors = {
  "Access-Control-Allow-Origin": "*",
  "Access-Control-Allow-Headers": "authorization, x-client-info, apikey, content-type",
};
const json = (b: unknown, s = 200) =>
  new Response(JSON.stringify(b), { status: s, headers: { ...cors, "content-type": "application/json" } });

Deno.serve(async (req) => {
  if (req.method === "OPTIONS") return new Response("ok", { headers: cors });
  try {
    const url = Deno.env.get("SUPABASE_URL")!;
    const admin = createClient(url, Deno.env.get("SUPABASE_SERVICE_ROLE_KEY")!);
    const userClient = createClient(url, Deno.env.get("SUPABASE_ANON_KEY")!, {
      global: { headers: { Authorization: req.headers.get("Authorization") ?? "" } },
    });
    const { data: { user } } = await userClient.auth.getUser();
    if (!user) return json({ error: "No autenticado" }, 401);
    const { data: yo } = await admin.from("profiles").select("role").eq("id", user.id).single();
    if (yo?.role !== "admin") return json({ error: "Solo el administrador" }, 403);

    const { nombre, email } = await req.json();
    const mail = String(email || "").trim().toLowerCase();
    if (!String(nombre || "").trim() || !/^[^@\s]+@[^@\s]+\.[^@\s]+$/.test(mail)) return json({ error: "Faltan el nombre o un correo válido" }, 400);
    const clave = Deno.env.get("INITIAL_PASSWORD") ?? "Wave1234";
    const { data: creado, error } = await admin.auth.admin.createUser({
      email: mail, password: clave, email_confirm: true, user_metadata: { full_name: String(nombre).trim() },
    });
    if (error) return json({ error: /already|registered|exists/i.test(error.message) ? "Ya hay una cuenta con ese correo" : error.message }, 400);
    const { error: pErr } = await admin.from("profiles")
      .update({ role: "tutor", full_name: String(nombre).trim(), email: mail, must_change_password: true }).eq("id", creado.user.id);
    if (pErr) { await admin.auth.admin.deleteUser(creado.user.id); throw pErr; }
    return json({ id: creado.user.id, email: mail, initial_password: clave });
  } catch (e) {
    console.error(e);
    return json({ error: "No se pudo crear el tutor. Probá de nuevo." }, 500);
  }
});
