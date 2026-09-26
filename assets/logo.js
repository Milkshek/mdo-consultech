/* Liquid emblem. Vector-field pattern adapted from collidingScopes/liquid-logo
 * (MIT), assets/vendor/liquid-logo-LICENSE.txt. The original silhouette is kept
 * intact; only the gold emblem is shaded. No network dependencies. */
(() => {
  const canvas = document.querySelector('.liquid-logo');
  const toggle = document.querySelector('.animation-toggle');
  if (!canvas || !toggle) return;
  const motion = matchMedia('(prefers-reduced-motion: reduce)');
  let gl, program, frame = 0, visible = false, paused = false, ready = false;
  let elapsed = 0, previous = 0, failed = false;
  const vertex = `attribute vec2 position; varying vec2 uv;
    void main(){uv=position*.5+.5;gl_Position=vec4(position,0.,1.);}`;
  const fragment = `precision mediump float;
    uniform sampler2D logo; uniform float time; varying vec2 uv;
    void main(){
      // Crop only the emblem from the unmodified supplied brand image.
      vec2 imageUV=vec2((140.+uv.x*220.)/510.,(120.+(1.-uv.y)*265.)/540.);
      vec4 original=texture2D(logo,imageUV);
      vec3 background=vec3(124.,15.,26.)/255.;
      float mask=smoothstep(.055,.45,original.g-original.b);
      // Flow field inspired by the original liquid-logo shader, six iterations.
      vec2 p=uv*2.-1.;
      vec2 v=p*.9;
      float flow=0.;
      for(int i=0;i<6;i++){
        float idx=float(i)+1.;
        v+=cos(v.yx*idx+vec2(0.,idx)+time*.55)/idx;
        flow+=(sin(v.x+v.y)+1.)*.11;
      }
      float wave=uv.y*9.+uv.x*5.+flow*2.-time*1.5;
      float sheen=.5+.5*sin(wave);
      float highlight=pow(sheen,7.);
      vec3 gold=mix(vec3(.60,.32,.07),vec3(.95,.72,.28),sheen);
      gold=mix(gold,vec3(1.,.96,.77),highlight*.95);
      gl_FragColor=vec4(mix(background,gold,mask),1.);
    }`;
  function fallback() {
    failed = true;
    cancelAnimationFrame(frame);
    frame = 0;
    canvas.classList.remove('is-ready');
    toggle.hidden = true;
  }
  function compile(type, source) {
    const shader = gl.createShader(type);
    gl.shaderSource(shader, source);
    gl.compileShader(shader);
    if (!gl.getShaderParameter(shader, gl.COMPILE_STATUS)) throw new Error('Shader unavailable');
    return shader;
  }
  function draw(now) {
    frame = 0;
    if (!ready || failed || !visible || paused || motion.matches || document.hidden) return;
    if (previous) elapsed += Math.min(now - previous, 80);
    previous = now;
    gl.uniform1f(gl.getUniformLocation(program, 'time'), elapsed / 1000);
    gl.drawArrays(gl.TRIANGLES, 0, 6);
    frame = requestAnimationFrame(draw);
  }
  function sync() {
    cancelAnimationFrame(frame);
    frame = 0;
    previous = 0;
    toggle.hidden = !ready || failed || motion.matches;
    canvas.classList.toggle('is-ready', ready && !failed && !motion.matches);
    if (ready && !failed && visible && !paused && !motion.matches && !document.hidden) frame = requestAnimationFrame(draw);
  }
  function init() {
    if (ready || failed || motion.matches) return;
    try {
      gl = canvas.getContext('webgl', { alpha: false, antialias: false, depth: false, powerPreference: 'low-power' });
      if (!gl) { fallback(); return; }
      const vert = compile(gl.VERTEX_SHADER, vertex);
      const frag = compile(gl.FRAGMENT_SHADER, fragment);
      program = gl.createProgram();
      gl.attachShader(program, vert); gl.attachShader(program, frag); gl.linkProgram(program);
      gl.deleteShader(vert); gl.deleteShader(frag);
      if (!gl.getProgramParameter(program, gl.LINK_STATUS)) throw new Error('WebGL unavailable');
      gl.useProgram(program);
      const buffer = gl.createBuffer();
      gl.bindBuffer(gl.ARRAY_BUFFER, buffer);
      gl.bufferData(gl.ARRAY_BUFFER, new Float32Array([-1,-1,1,-1,-1,1,-1,1,1,-1,1,1]), gl.STATIC_DRAW);
      const position = gl.getAttribLocation(program, 'position');
      gl.enableVertexAttribArray(position); gl.vertexAttribPointer(position, 2, gl.FLOAT, false, 0, 0);
      const image = new Image();
      image.onload = () => {
        if (failed) return;
        const texture = gl.createTexture();
        gl.bindTexture(gl.TEXTURE_2D, texture);
        gl.texParameteri(gl.TEXTURE_2D, gl.TEXTURE_WRAP_S, gl.CLAMP_TO_EDGE);
        gl.texParameteri(gl.TEXTURE_2D, gl.TEXTURE_WRAP_T, gl.CLAMP_TO_EDGE);
        gl.texParameteri(gl.TEXTURE_2D, gl.TEXTURE_MIN_FILTER, gl.LINEAR);
        gl.texParameteri(gl.TEXTURE_2D, gl.TEXTURE_MAG_FILTER, gl.LINEAR);
        gl.texImage2D(gl.TEXTURE_2D, 0, gl.RGBA, gl.RGBA, gl.UNSIGNED_BYTE, image);
        gl.uniform1i(gl.getUniformLocation(program, 'logo'), 0);
        gl.viewport(0, 0, canvas.width, canvas.height);
        gl.uniform1f(gl.getUniformLocation(program, 'time'), 0);
        gl.drawArrays(gl.TRIANGLES, 0, 6);
        ready = true;
        sync();
      };
      image.onerror = fallback;
      image.src = canvas.dataset.image;
    } catch (_) { fallback(); }
  }
  toggle.addEventListener('click', () => {
    paused = !paused;
    toggle.setAttribute('aria-label', paused ? toggle.dataset.play : toggle.dataset.pause);
    toggle.querySelector('span').textContent = paused ? toggle.dataset.play : toggle.dataset.pause;
    sync();
  });
  canvas.addEventListener('webglcontextlost', event => { event.preventDefault(); fallback(); });
  document.addEventListener('visibilitychange', sync);
  motion.addEventListener('change', () => { init(); sync(); });
  if ('IntersectionObserver' in window) {
    new IntersectionObserver(entries => { visible = entries[0].isIntersecting; sync(); }).observe(canvas);
  } else { visible = true; }
  init();
})();
