import numpy as np
import pylab as pl
from scipy.interpolate import lagrange

x = np.array([0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8])
y = np.array([0, 2.12, 3.02, 3.25, 3.14, 2.05, 2.52, 2.16, 1.84])

polLagrange = lagrange(x, y)
xPol = np.linspace(np.min(x), np.max(x), 350, endpoint=True)
PxPol = polLagrange(xPol)

pl.plot(xPol, PxPol, color='firebrick')
pl.plot(x, y, 'o', color='orange')
pl.show()
h = 0.1
x = x + y;


def DerivadaProgresiva(x0, h):
    DP = (polLagrange(x0 + h) - polLagrange(x0)) / h
    return DP


print(DerivadaProgresiva(0.35, 0.1))
