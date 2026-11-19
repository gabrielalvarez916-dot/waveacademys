import asyncio, subprocess, sys, json
from playwright.async_api import async_playwright
HTML='file:///home/claude/waveacademys/actividades/clases/demo-valor-posicional.html'
FPS=30; OUT='/tmp/sin_audio.mp4'
async def main():
  V=json.load(open('/tmp/tiempos.json')); total=V['a0'][-1]+V['aw'][-1]+1.0
  N=int(total*FPS) if len(sys.argv)<2 else int(sys.argv[1])
  async with async_playwright() as p:
    b=await p.chromium.launch(executable_path='/usr/bin/google-chrome',chromium_sandbox=False,args=['--no-sandbox','--no-proxy-server','--mute-audio'])
    pg=await b.new_page(viewport={'width':1280,'height':720},device_scale_factor=1.5)
    await pg.goto(HTML,wait_until='domcontentloaded')
    await pg.evaluate("""()=>{document.getElementById('ui').remove();document.getElementById('pp').remove();gsap.globalTimeline.pause();
      const V=window.VOZ; window.tA=function(ta){let i=0;while(i+1<V.a0.length&&ta>=V.a0[i+1])i++; if(ta<V.a0[0])return ta;
      const W=(i+1<V.t0.length?V.t0[i+1]:V.fin)-V.t0[i]; return V.t0[i]+Math.min(V.aw[i],ta-V.a0[i])*W/V.aw[i];};}""")
    ff=subprocess.Popen(['ffmpeg','-v','error','-y','-f','image2pipe','-framerate',str(FPS),'-c:v','mjpeg','-i','-','-c:v','libx264','-preset','veryfast','-crf','20','-pix_fmt','yuv420p',OUT],stdin=subprocess.PIPE)
    for f in range(N):
      ta=f/FPS
      await pg.evaluate(f"()=>{{gsap.globalTimeline.time({ta});ESCENA.time(Math.min(ESCENA.duration(),tA({ta})))}}")
      ff.stdin.write(await pg.screenshot(type='jpeg',quality=90))
      if f%300==0: print('cuadro',f,'/',N,flush=True)
    ff.stdin.close(); ff.wait(); await b.close()
asyncio.run(main())
