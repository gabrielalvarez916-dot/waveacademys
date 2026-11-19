import soundfile as sf, numpy as np, json, subprocess
from kokoro_onnx import Kokoro
k=Kokoro('/home/claude/tts/kokoro.onnx','/home/claude/tts/voices.bin')
T0=[0.3,5.4,11.0,17.0,24.0,31.0,38.0,45.0,47.6,52.2,58.0]
FIN=64.0
H=["¿Cómo puede ser que un dos valga doscientos?","La respuesta está en una fábrica... de alfajores.","Cada alfajor suelto es una unidad.","Pero cuando juntás diez, se empaquetan: eso es una decena.","Y diez paquetes llenan una caja: una centena.","Ahora mirá el número cuatro mil doscientos cinco.","El dos cae en las centenas. Ya no es un dos: vale doscientos.","¿Y el cero? Parece que no hace nada...","Sacalo. ¡Y el número se rompe!","El cero cuida el lugar vacío.","La cifra es lo que ves. El valor, es dónde está."]
V='em_alex'; sr=24000; clips=[]; dur=[]; a0=[]; aw=[]; t=0.3
for i,txt in enumerate(H):
  W=(T0[i+1] if i+1<len(T0) else FIN+0.5)-T0[i]
  s,sr=k.create(txt,voice=V,speed=0.97,lang='es'); d=len(s)/sr
  w=max(d+1.3, W/1.6); a0.append(round(t,3)); aw.append(round(w,3)); dur.append(round(d,3)); clips.append((t,s)); t+=w
  print(i,round(d,2),'ventana anim',round(W,2),'-> audio',round(w,2))
pista=np.zeros(int((t+0.5)*sr),dtype=np.float32)
for st,s in clips: a=int(st*sr); pista[a:a+len(s)]+=s
pista=pista/max(1e-6,np.abs(pista).max())*0.9
sf.write('/tmp/voz.wav',pista,sr)
subprocess.run(['ffmpeg','-v','error','-y','-i','/tmp/voz.wav','-af','highpass=f=70,acompressor=threshold=-18dB:ratio=3,loudnorm=I=-16','-ac','1','-b:a','80k','/tmp/voz.mp3'],check=True)
json.dump({'t0':T0,'fin':FIN+0.5,'a0':a0,'aw':aw,'dur':dur},open('/tmp/tiempos.json','w')); print('total',round(t,1),'s')
