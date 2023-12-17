import numpy as np
import math as m
import matplotlib.pyplot as plt


def mo (x,y,z):
    mm = m.sqrt(x**2+y**2+z**2)
    return mm

def d(cx1,cx2,cy1,cy2,cz1,cz2):
    distanza= mo(cx1-cx2,cy1-cy2,cz1-cz2)
    return distanza



def cv(v0,t,a):    #Calcolo della velocità
    vv=a*t+v0
    return vv

def ma(v0,t,p0,a):    #Calcolo della traslazione moto ad acc costante
    ak=0.5*a*(t**2)+v0*t+ p0
    return ak

def acc(ma,mb,ra,rb,xa,xb,xcorpo):#calcolo della componente di un'accelerazione
    a=G*((ma*(xa-xcorpo)/(ra**3))+(mb*(xb-xcorpo)/(rb**3)))
    return a
def cm (xa,ya,za,xb,yb,zb,xc,yc,zc,ma,mb,mc):
    xcm=(ma*xa+mb*xb+mc*xc)/(ma+mb+mc)
    ycm=(ma*ya+mb*yb+mc*yc)/(ma+mb+mc)
    zcm=(ma*za+mb*zb+mc*zc)/(ma+mb+mc)
    return xcm,ycm,zcm




G=2000 #Costante di gravitazione universale

#Corpo 1

m1=150
x01=0
y01=0
z01=0
vx01=0
vy01=0
vz01=0
ax01=0
ay01=0
az01=0



p1=[x01,y01,z01]
v1=[vx01,vy01,vz01]
a1=[ax01,ay01,az01]



#Corpo 2

m2=30
x02=5
y02=-12
z02=3
vx02=10
vy02=6
vz02=4
ax02=0
ay02=0
az02=0



p2=[x02,y02,z02]
v2=[vx02,vy02,vz02]
a2=[ax02,ay02,az02]



#Corpo 3

m3=5
x03=-10
y03=10
z03=-2
vx03=4
vy03=2
vz03=-1
ax03=0
ay03=0
az03=0



p3=[x03,y03,z03]
v3=[vx03,vy03,vz03]
a3=[ax03,ay03,az03]




st=120#Risoluzione del calcolo della traiettoria
t0=0;t=t0;dt=0.0001   #tempo
i=0

p1xyz=np.zeros((st+1,3))    #array dei vettori delle traiettorie
p2xyz=np.zeros((st+1,3))
p3xyz=np.zeros((st+1,3))

while i<=st:

    a1[0]=acc(m2,m3,d(p1[0],p2[0],p1[1],p2[1],p1[2],p2[2]),d(p1[0],p3[0],p1[1],p3[1],p1[2],p3[2]),p2[0],p3[0],p1[0])
    a1[1]=acc(m2,m3,d(p1[0],p2[0],p1[1],p2[1],p1[2],p2[2]),d(p1[0],p3[0],p1[1],p3[1],p1[2],p3[2]),p2[1],p3[1],p1[1])
    a1[2]=acc(m2,m3,d(p1[0],p2[0],p1[1],p2[1],p1[2],p2[2]),d(p1[0],p3[0],p1[1],p3[1],p1[2],p3[2]),p2[2],p3[2],p1[2])

    a2[0]=acc(m1,m3,d(p1[0],p2[0],p1[1],p2[1],p1[2],p2[2]),d(p2[0],p3[0],p2[1],p3[1],p2[2],p3[2]),p1[0],p3[0],p2[0])
    a2[1]=acc(m1,m3,d(p1[0],p2[0],p1[1],p2[1],p1[2],p2[2]),d(p2[0],p3[0],p2[1],p3[1],p2[2],p3[2]),p1[1],p3[1],p2[1])
    a2[2]=acc(m1,m3,d(p1[0],p2[0],p1[1],p2[1],p3[2],p2[2]),d(p2[0],p3[0],p2[1],p3[1],p2[2],p3[2]),p1[2],p3[2],p2[2])

    a3[0]=acc(m2,m1,d(p3[0],p2[0],p3[1],p2[1],p3[2],p2[2]),d(p1[0],p3[0],p1[1],p3[1],p1[2],p3[2]),p2[0],p1[0],p3[0])
    a3[1]=acc(m2,m1,d(p3[0],p2[0],p3[1],p2[1],p3[2],p2[2]),d(p1[0],p3[0],p1[1],p3[1],p1[2],p3[2]),p2[1],p1[1],p3[1])
    a3[2]=acc(m2,m1,d(p3[0],p2[0],p3[1],p2[1],p3[2],p2[2]),d(p1[0],p3[0],p1[1],p3[1],p1[2],p3[2]),p2[2],p1[2],p3[2])

    p1[0]=ma(v1[0],t,p1[0],a1[0])#Calcolo delle nuove          coordinate di 1 su x
    p1[1]=ma(v1[1],t,p1[1],a1[1])    #Calcolo delle nuove coordinate di 1 su y
    p1[2]=ma(v1[2],t,p1[2],a1[2])    #Calcolo delle nuove coordinate di 1 su z
    p2[0]=ma(v2[0],t,p2[0],a2[0])#Calcolo delle nuove coordinate di 2 su x
    p2[1]=ma(v2[1],t,p2[1],a2[1])    #Calcolo delle nuove coordinate di 2 su y
    p2[2]=ma(v2[2],t,p2[2],a2[2]) #Calcolo delle nuove coordinate di 2 su z
    p3[0]=ma(v3[0],t,p3[0],a3[0])#Calcolo delle nuove coordinate di 3 su x
    p3[1]=ma(v3[1],t,p3[1],a3[1])    #Calcolo delle nuove coordinate di 3 su y
    p3[2]=ma(v3[2],t,p3[2],a3[2]) #Calcolo delle nuove coordinate di 3 su z


    p1xyz[i,:]=[p1[0],p1[1],p1[2]]
    p2xyz[i,:]=[p2[0],p2[1],p2[2]]
    p3xyz[i,:]=[p3[0],p3[1],p3[2]]

    caricamento=(i*100/st)
    print("Caricamento= %2.1f "%caricamento)
    print(cm(p1[0],p1[1],p1[2],p2[0],p2[1],p2[2],p3[0],p3[1],p3[2],m1,m2,m3))

    t=t+dt
    i=i+1


fig= plt.figure(1)

d3 = fig.add_subplot(111,projection='3d')
d3.plot(p1xyz[:,0],p1xyz[:,1],p1xyz[:,2],marker='o')
d3.plot(p2xyz[:,0],p2xyz[:,1],p2xyz[:,2])
d3.plot(p3xyz[:,0],p3xyz[:,1],p3xyz[:,2])

d3.set_xlabel('X',)
d3.set_ylabel('Y')
d3.set_zlabel('Z',)

plt.figure(2)
plt.plot(p1xyz[:,0],p1xyz[:,1],marker='o')
plt.plot(p2xyz[:,0],p2xyz[:,1])
plt.plot(p3xyz[:,0],p3xyz[:,1])

plt.show()

