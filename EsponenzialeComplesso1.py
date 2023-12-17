import numpy as np
import math as m
import matplotlib.pyplot as plt

def exp(x,y):
    a=(2.7182**x)*np.cos(y)
    b=(2.7182**x)*np.sin(y)
    return a,b

step=100
k=step**2


xvalori=np.linspace(-1,1.3,step)
yvalori=np.linspace(-2,2,step)
px=np.zeros((step,step))
py=np.zeros((step,step))
expx=np.linspace(1,2,k)
expy=np.linspace(1,2,k)

i=0
while (i<step):
    px[i,:]=xvalori
    py[:,i]=yvalori
    i=i+1
i=0
while (i<step):
    j=0
    while(j<step):
        p=i*step+j

        expx[p],expy[p]=exp(px[i,j], py[i,j])

        print((p/(step**2))*100)
        j=j+1

    i=1+i


plt.figure(1)
plt.plot(px,py,'o')
plt.plot(expx,expy,'o')

plt.show()


"""

"""


"""

plt.plot(p2xyz[:,0],p2xyz[:,1])
plt.plot(p3xyz[:,0],p3xyz[:,1])

plt.show()
"""

"""fig= plt.figure(1)

d3 = fig.add_subplot(111,projection='3d')
d3.plot(p1xyz[:,0],p1xyz[:,1],p1xyz[:,2],marker='o')
d3.plot(p2xyz[:,0],p2xyz[:,1],p2xyz[:,2])
d3.plot(p3xyz[:,0],p3xyz[:,1],p3xyz[:,2])

d3.set_xlabel('X',)
d3.set_ylabel('Y')
d3.set_zlabel('Z',)"""
