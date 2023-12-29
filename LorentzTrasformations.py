import numpy as np
import scipy as sc
from matplotlib import pyplot as plt
import matplotlib.animation as animation
from matplotlib.widgets import Button, Slider



##
c=1
v=0.5 #velocity of the Reference frame
beta=v/c #times the speed of light

## Classes
class point():
    def __init__ (self,ct0,x0,y0,z0):
        self.ct=ct0
        self.x=x0
        self.y=y0
        self.z=z0

class velocity():
    def __init__ (self,c,vx0,vy0,vz0):
        self.c=c
        self.vx=vx0
        self.vy=vy0
        self.vz=vz0
##   Relativity variables


def lorentz_transform_matrix(beta):
    # Lorentz transformation matrix
    gamma = 1 / np.sqrt(1 - beta**2)
    matrix = np.array([[gamma, -gamma*beta, 0, 0],
                       [-gamma*beta, gamma, 0, 0],
                       [0, 0, 1, 0],
                       [0, 0, 0, 1]])
    return matrix

def lorentz_transform(events, beta):
    # Apply Lorentz transformations using the matrix
    matrix = lorentz_transform_matrix(beta)
    transformed_events = np.dot(matrix, events)
    return transformed_events

## Plot Characteristics

density=1
#points=density**2
t_max=5
t_min=0
x_max=5
x_min=0
y_max=5
y_min=0
z_max=5
z_min=0
## To be updated
## Points to plot

tt,xx,yy,zz=np.mgrid[t_min:t_max:density,x_min:x_max:density,y_min:y_max:density,z_min:z_max:density] #Creating some points which will be plotted
tt=np.array(tt.flatten()) #This il just vector manipolation for computational needs
xx=np.array(xx.flatten())
yy=np.array(yy.flatten())
zz=np.array(zz.flatten())

events=[[0,0,0,0]]
for i in range(1,tt.size):
    events.append(np.array([tt[i],xx[i],yy[i],zz[i]]))

transformed_events = np.array([lorentz_transform(events[i], beta) for i in range(0,tt.size)])
transformed_events=np.array(transformed_events.flatten())

tt1=transformed_events[0::4]
xx1=transformed_events[1::4]
yy1=transformed_events[2::4]
zz1=transformed_events[3::4]
##

## Variables to plot
aa=tt
bb=xx
cc=yy
aa1=tt1
bb1=xx1
cc1=yy1



##

 ##Plot
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')
ax.scatter(aa, bb, cc, label='Original Events', color='blue')

# Apply Lorentz transformations and plot the transformed events
ax.scatter(aa1, bb1,cc1, label='Transformed Events', color='red',)
ax.quiver(aa,bb,cc, (aa1-aa), (bb1-bb), (cc1-cc),normalize=True)

# Set labels
ax.set_xlabel('T')
ax.set_ylabel('X')
ax.set_zlabel('Y')

ax.legend()
plt.title('Lorentz Transformations in 4D')
plt.show()