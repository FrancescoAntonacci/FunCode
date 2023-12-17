#Progetto Moto parabolico in coordinate polari e coordinate cartesiane
import matplotlib.pyplot as plt
import numpy as np
import math as m
from mpl_toolkits.mplot3d import Axes3D



def mo (x,y,z):
    mm = m.sqrt(x**2+y**2+z**2)
    return mm


def cv(v0,t,a):    #Calcolo della velocità
    vv=a*t+v0
    return vv

def noacc(v0,t,p0):    #Calcolo della traslazione moto a v costante
    na=v0*t+ p0
    return na


def acc(v0,t,p0,a):    #Calcolo della traslazione moto ad acc costante
    ak=0.5*a*(t**2)+v0*t+ p0
    return ak

#Caratteristiche corpo
x0=0 ; y0=0; z0=0; #Posizione
d0=mo(x0,y0,z0)
p=[x0,y0,z0,d0]

x=y0 ; y=y0; z=z0; #Posizione  NON SARANNO USATE, IN QUANTO QUESTO E' UN PURO ESERCIZIO SUI VETTORI
d=mo(x,y,z)
p=[x,y,z,d]


v0x=10 ; v0y=20; v0z=5; #Velocità
v0=mo(v0x,v0y,v0z)
vin=[v0x,v0y,v0z,v0]

vx=v0x ; vy=v0y; vz=v0z; #Velocità  NON SARANNO USATE, IN QUANTO QUESTO E' UN PURO ESERCIZIO SUI VETTORI
vm=mo(vx,vy,vz)
v=[vx,vy,vz,vm]


g=-9.81 #accelerazione gravizionale sull'asse y

st=20#Risoluzione del calcolo della traiettoria
t0=0;t=t0;tf=2*(v0y/-g); dt=(tf-t0)/st   #tempo-



vtrai=[x,y,z,d,vx,vy,vz,v,g,t]          #Calcolo Traiettoria
trai=np.zeros((st+1,10))
i=0

while (i<=st):

    vtrai[0]=noacc(v0x,t,x0)
    vtrai[1]=acc(v0y,t,y0,g)
    vtrai[2]=noacc(v0z,t,z0)
    vtrai[3]=mo(vtrai[0],vtrai[1],vtrai[2])

    vtrai[5]=cv(v0y,t,g)
    vtrai[7]=mo(vtrai[4],vtrai[5],vtrai[6])

    vtrai[8]=g

    vtrai[9]=t


    trai[i]=vtrai[0:]
    t=t+dt
    i=i+1



print (trai)



'''
  plt.figure(1)
  plt.plot(ts,xt,'r.')
  plt.xlabel("t")
  plt.ylabel("x(t)")
  plt.figure(2)
  plt.plot(ts,yt,'r.')
  plt.xlabel("t")
  plt.ylabel("y(t)")
  plt.figure(3)
  plt.plot(ts,zt,'r.')
  plt.xlabel("t")
  plt.ylabel("z(t)")
  plt.figure(4)
  plt.plot(ts,v_mod_t,'r.')
  plt.xlabel("t")
  plt.ylabel("|v|")
  plt.figure(5)
  plt.plot(ts,a_mod_t,'r.')
  plt.xlabel("t")
  plt.ylabel("|a|")

  plt.figure(8)
  plt.plot(ts,a_perp_t,'r.')
  plt.xlabel("t")
  plt.ylabel("a perpendicolare a v")
  plt.figure(9)
  plt.plot(ts,a_para_t,'r.')
  plt.xlabel("t")
  plt.ylabel("a parallela a v")
  plt.figure(10)
  plt.plot(ts,r_osc_t,'r.')
  plt.xlabel("t")
  plt.ylabel("raggio osculatore")
  fig = plt.figure(20)

'''


fig= plt.figure(1)

d3 = fig.add_subplot(111,projection='3d')
d3.plot(trai[:,0],trai[:,1],trai[:,2])

d3.set_xlabel('X',)
d3.set_ylabel('Y')
d3.set_zlabel('Z',)
plt.show()

'''

plt.title("Maremma cignala")
plt.xlabel("x")
plt.ylabel("y")
plt.zlabel("z")
plt.plot(trai[:,0],trai[:,1],trai[:,2])#caratteristiche grafico. Label= legenda: stessa sintassi di Latec
plt.grid()
'''
