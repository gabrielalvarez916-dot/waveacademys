// Funciones compartidas de sesión. Se carga después de config.js y de supabase-js.
(function () {
  var cfg = window.WAVE_CONFIG;

  var sb = window.supabase.createClient(cfg.SUPABASE_URL, cfg.SUPABASE_KEY, {
    auth: { persistSession: true, autoRefreshToken: true, detectSessionInUrl: false }
  });

  // Página de cada rol (los nombres de rol son los de la tabla profiles)
  var PANELES = {
    admin: '/admin.html',
    family: '/familia.html',
    student: '/alumno.html',
    tutor: '/tutor.html'
  };

  async function getProfile(userId) {
    var res = await sb
      .from('profiles')
      .select('role, full_name, is_suspended, must_change_password')
      .eq('id', userId)
      .maybeSingle();
    if (res.error) throw res.error;
    return res.data;
  }

  // A dónde mandar a una persona según su perfil
  function destino(perfil) {
    if (perfil.must_change_password) return '/cambiar-clave.html';
    return PANELES[perfil.role] || '/ingresar.html';
  }

  async function salir() {
    await sb.auth.signOut();
    location.replace('/ingresar.html');
  }

  window.Wave = { sb: sb, PANELES: PANELES, getProfile: getProfile, destino: destino, salir: salir };
})();
