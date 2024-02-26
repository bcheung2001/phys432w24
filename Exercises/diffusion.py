# -*- coding: utf-8 -*-
"""
Code for handling diffusion

@author: Benjamin Cheung
"""

import numpy as np
import matplotlib.pyplot as plt

dt = 1
dx = 1

Ngrid = 50
Nsteps = 5000

x = np.arange(0, Ngrid*1., dx)/Ngrid

D1 = 0.1
D2 = 1.0

beta1 = D1*dt/dx/dx
beta2 = D2*dt/dx/dx

f1 = np.copy(x)
f2 = np.copy(x)

n = len(x)

A1 = np.eye(n)*(1.0+2.0*beta1) + np.eye(n,k=1)*(-beta1) + np.eye(n,k=-1)*(-beta1)
A1[0][0] = 1
A1[0][1] = 0
A1[-1][-1] = 1 + beta1

A2 = np.eye(n)*(1.0+2.0*beta2) + np.eye(n,k=1)*(-beta2) + np.eye(n,k=-1)*(-beta2)
A2[0][0] = 1
A2[0][1] = 0
A2[-1][-1] = 1 + beta2

plt.ion()
fig, ax = plt.subplots(1,2)

ax[0].set_xlim([0,1])
ax[0].set_ylim([0,2])
ax[1].set_xlim([0,1])
ax[1].set_ylim([0,2])

ax[0].plot(x,f1, '-k')
ax[1].plot(x,f2, '-k')

p1, = ax[0].plot(x, f1, 'ro')
p2, = ax[1].plot(x, f2, 'ro')

fig.canvas.draw()

for _ in range(Nsteps):
    f1 = np.linalg.solve(A1,f1)
    f2 = np.linalg.solve(A2,f2)    
    
    p1.set_ydata(f1)
    p2.set_ydata(f2)
    
    fig.canvas.draw()
    
    plt.pause(0.001)