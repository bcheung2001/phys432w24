# -*- coding: utf-8 -*-
"""
Code for sound waves in 1D

@author: Benjamin Cheung
"""

import numpy as np
import matplotlib.pyplot as plt

def gaussian(size,amp,width):
    gauss = np.zeros(size)
    
    for i in range(size):
        gauss[i] = amp*np.exp(-((i-size/2)/width)**2/2)
    
    return gauss

cs2 = 10

Ngrid = 250
Nsteps = 1000

x = np.linspace(0, 1, Ngrid)
dx = x[1]-x[0]
dt = 0.1*dx
f1 = np.zeros(Ngrid)
f2 = np.zeros(Ngrid)

f1 = 1 + gaussian(Ngrid, 0.5, 4)
#f2 = gaussian(Ngrid, 0.25, 4)

plt.ion()
fig, ax = plt.subplots(2,1)

ax[0].set_xlim([0,1])
ax[1].set_xlim([0,1])
ax[0].set_ylim([0.3,1.7])
ax[1].set_ylim([-1,1])

p1, = ax[0].plot(x, f1, 'r.')
p2, = ax[1].plot(x, f2, 'b.')

fig.canvas.draw()

for _ in range(Nsteps):
    
    #Step 1: No source
    u = np.zeros(Ngrid+1)
    
    u[1:Ngrid] = ((f2[:-1]/f1[:-1]) + (f2[1:]/f1[1:]))/2
    
    J1 = np.zeros(Ngrid+1)
    J2 = np.zeros(Ngrid+1)
    
    for i in range(1,len(J1)):
        if u[i] >= 0:
            J1[i] = u[i]*f1[i-1]
            J2[i] = u[i]*f2[i-1]
        else:
            J1[i] = u[i]*f1[i]
            J2[i] = u[i]*f2[i]
    
    f1 = f1 - (dt/dx)*(J1[1:] - J1[:Ngrid])
    f2 = f2 - (dt/dx)*(J2[1:] - J2[:Ngrid])
    
    #Step 2: Source
    f2[0] = f2[0] - (dt/dx)*cs2*(f1[1] - f1[0])/2
    f2[Ngrid-1] = f2[Ngrid-1] - (dt/dx)*cs2*(f1[Ngrid-1] - f1[Ngrid-2])/2
    
    f2[1:Ngrid-1] = f2[1:Ngrid-1] - (dt/dx)*cs2*(f1[2:] - f1[:Ngrid-2])/2
    
    p1.set_ydata(f1)
    p2.set_ydata(f2)
    
    fig.canvas.draw()
    
    plt.pause(0.001)