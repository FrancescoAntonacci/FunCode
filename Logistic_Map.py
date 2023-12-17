#Idea:This code will plot the logistic map
import numpy as np
from matplotlib import pyplot as plt


## Points definition
class point():
    def __init__(self,x,y,z):
        self.x=x
        self.y=y
        self.z=z

    def mod(self):
        self.m=module(self.x,self.y,self.z)

    def display(self):
        plt.plot(self.x,self.y)
        #plt.show()



## Useful functions
def module(x,y,z):
    '''
    module of some coordinates
    '''
    m=np.sqrt(x**2+y**2+z**2)
    return m
##

def parabola_lm(r,x):
    return r*x*(1-x)

def cyclic_lm(r,x,n):
    for i in range(0,n):
        x = parabola_lm(r,x)
    return x

def onclick_lm(event):
    x0=np.random.uniform(0,1)
    sw_dia(x0,event.xdata,100)




## Spiderweb diagram

def sw_dia(x0,r,n_p):
    '''
    This functions plots a spiderweb diagram given a starting value x0, a coefficient and the number of iterations.
    '''
    x0_wd=x0 #starting point of the recursive function
    r_wd=r
    n_p_wd=n_p #number of points of the web diagram

    p=[point(x0_wd,parabola_lm(r_wd,x0_wd),0)]
    xx_wd=[]
    yy_wd=[]

    for i in range(1,n_p_wd+1):

        p.append(point(p[i-1].y,parabola_lm(r_wd,p[i-1].y),p[i-1].z))
        xx_wd.append(p[i-1].x)
        yy_wd.append(p[i-1].x)
        xx_wd.append(p[i-1].x)
        yy_wd.append(p[i-1].y)

    plt.figure("Spiderweb diagram")

    x_to_plot=np.linspace(0,1,10000)

    plt.plot(xx_wd,yy_wd)
    plt.plot(x_to_plot,x_to_plot)
    plt.plot(x_to_plot,parabola_lm(r_wd,x_to_plot))

    plt.show()


## Logistic map
def logistic_map(plot):
    points=10**7 #number of points to display in the plot
    r = np.random.uniform(0,4,points)
    x0 = np.random.uniform(0,1,points)
    n_i=120 #numbero of iterations
    size=0.01 #size of dots in the plot

    conv_lm = cyclic_lm(r,x0,n_i)

    if (plot==True):
        fig = plt.figure('Bifurcation diagram')

        plt.errorbar(r,conv_lm,fmt='.',color='black',markersize=size)
        plt.xlabel('$r$')
        plt.ylabel('$x_{%.0f}$'%(n_i))
        plt.title('Bifurcation diagram')
        plt.show()
        cid = fig.canvas.mpl_connect('button_press_event', onclick_lm)

logistic_map(True)

