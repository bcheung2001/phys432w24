# -*- coding: utf-8 -*-
"""
(PS3 Q3)
The following script produces an animation which models lava flowing down an incline,
as seen in lecture

@author: Benjamin Cheung
2023-02-25
"""

import numpy as np
import matplotlib.pyplot as plt

dt = 0.0005
Nsteps = 500

dx = 0.1
Ngrid = 10
H = 5. #height of the lava, ~5cm from lecture notes

geff = 500. #effective gravitational acceleration for an incline of 30° (see pdf submission)
nu = 1000. #viscosity (10^3, from lecture)

beta = nu*dt/dx/dx

x = np.arange(0, Ngrid*H)/Ngrid

u = np.zeros(x.shape) #starting at rest

n = len(x)
A = np.eye(n)*(1.+2.*beta) + np.eye(n,k=1)*(-beta) + np.eye(n,k=-1)*(-beta)
A[0][0] = 1 #no-slip boundary condition at y=0
A[0][1] = 0
A[-1][-1] = 1 + beta #no-stress boundary condition at y=H

plt.ion()
fig, ax = plt.subplots(1,1)
ax.set_ylim([0,7])
ax.set_xlim([0,5])
ax.set_xlabel(r'$y$ (cm)')
ax.set_ylabel(r'$u_x$ (cm/s)')

ax.plot(x, -geff*(0.5*x*x - H*x)/nu, '-k', label='Steady-state solution') #steady-state solution

p, = ax.plot(x,u,'ro')

fig.canvas.draw()

for _ in range(Nsteps):
    
    u[1:] += geff*dt #source term; do not add to y=0 component to comply with no-slip B.C.
    
    u = np.linalg.solve(A, u)
    p.set_ydata(u) #update plot
    
    fig.canvas.draw()
    ax.legend()
    
    plt.pause(0.005)