# -*- coding: utf-8 -*-
"""
Code for Godunov method

@author: Benjamin Cheung
"""

import numpy as np
import matplotlib.pyplot as plt

dt = 1
dx = 1

Ngrid = 50
Nsteps = 5000

x = np.arange(0, Ngrid*1., dx)/Ngrid

u = -0.1

f = np.copy(x)

plt.ion()
fig, ax = plt.subplots(1,1)

ax.set_xlim([0,1])
ax.set_ylim([0,2])

ax.plot(x,f, '-k')

p, = ax.plot(x, f, 'ro')

fig.canvas.draw()

for _ in range(Nsteps):
    f[1:Ngrid-1] = f[1:Ngrid-1] - (u*dt)*(f[2:] - f[1:Ngrid-1])/dx
    
    p.set_ydata(f)
    
    fig.canvas.draw()
    
    plt.pause(0.001)