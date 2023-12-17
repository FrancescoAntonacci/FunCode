import numpy as np
from matplotlib import pyplot  as plt
from mpl_toolkits.mplot3d import Axes3D

##
xmin=-2
xmax=1
ymin=-1.5
ymax=1.5
pixel_density=100
num_it=100
##


def c_mat(xmin, xmax, ymin, ymax, pixel_density):
    re = np.linspace(xmin, xmax, int((xmax - xmin) * pixel_density))
    im = np.linspace(ymin, ymax, int((ymax - ymin) * pixel_density))
    return re[np.newaxis, :] + im[:, np.newaxis] * 1j

v=[]#Value

def st(c, num_it):
    z = 0
    for i in range(num_it):
        z = z ** 2 + c

    return abs(z) < 2

def mod_c(c, num_it):
    z = 0
    for i in range(num_it):
        z = z ** 2 + c

    return abs(z)


def get_points(members,num_it):
    x=[]
    y=[]
    z=[]
    for i in range(num_it,num_it+20):
        x.append(members.real)
        y.append(members.imag)
        v=mod_c(members.real,i)
        z.append(v)
    p=[x,y,z]
    return p


def get_members(c, num_it):
    mask = st(c, num_it)
    return c[mask]

c = c_mat(xmin, xmax,ymin,ymax,pixel_density)
members = get_members(c, num_it)

points=get_points(members,num_it)


##
size=10
plt.figure(1)
plt.scatter(points[0],points[2])
plt.show()



plt.show()
fig=plt.figure(2)


d3 = fig.add_subplot(111,projection='3d')
d3.scatter3D(points[0],points[1],points[2],s=1)


d3.set_xlabel('X',)
d3.set_ylabel('Y')
d3.set_zlabel('Z',)
plt.show()



plt.show()




