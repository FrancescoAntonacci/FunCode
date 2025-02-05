import numpy as np
from matplotlib import pyplot as plt

##
res = 1000
xmax = 30
xmin = 0
xx = np.linspace(xmin, xmax, res)
n = 1000  # Elements of the base
##

def f(x):
    return np.sin(x)/(x+1)

def dotprod(f, g, xx):
    return np.sum(f * g * (xx[1] - xx[0]))

def f1(x):
    return np.exp(-x)

def gram_schmidt(xx, n):
    """ Computes an orthonormal basis using Gram-Schmidt for exp(-n*x) functions """
    basis = []
    for i in range(1, n + 1):
        w = np.exp(-i * xx)
        for prev in basis:
            w -= dotprod(w, prev, xx) * prev
        norm = np.sqrt(dotprod(w, w, xx))
        if norm != 0:
            basis.append(w / norm)
    return basis

def Fourier(f, xx, basis):
    """ Computes the Fourier approximation using the orthonormal basis """
    return sum(dotprod(f(xx), phi, xx) * phi for phi in basis)

# Compute orthonormal basis
basis = gram_schmidt(xx, n)

# Compute Fourier approximation
yy = Fourier(f, xx, basis)

# Plot results
plt.figure()
plt.plot(xx, f(xx), label="f(x)")
plt.plot(xx, yy, label="Fourier Approximation")
plt.legend()
plt.show()
