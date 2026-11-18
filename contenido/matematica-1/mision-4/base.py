import json, os
D=lambda t,x:{"tipo":"definicion","titulo":t,"texto":x}
P=lambda x:{"tipo":"parrafo","texto":x}
IM=lambda t,x:{"tipo":"importante","titulo":t,"texto":x}
T=lambda t,c,f,x=None:{"tipo":"tabla","titulo":t,"columnas":c,"filas":f,"iguales":True,**({"texto":x} if x else {})}
E=lambda t,x,i:{"tipo":"ejemplo","titulo":t,"texto":x,"items":i}
S=lambda e,t,b:{"etapa":e,"titulo":t,"bloques":b}
MC=lambda p,o,ok,e,**k:{"t":"multiple_choice","p":p,"o":o,"r":{"correcta":ok},"e":e,**k}
VF=lambda p,ok,e,**k:{"t":"true_false","p":p,"o":["Verdadero","Falso"],"r":{"correcta":ok},"e":e,**k}
N=lambda p,r,e,o=None,**k:{"t":"numeric","p":p,"o":o or {},"r":r,"e":e,**k}
