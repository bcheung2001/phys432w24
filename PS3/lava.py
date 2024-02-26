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
H = 5.

geff = 500.
nu = 1000.

beta = nu*dt/dx/dx

x = np.arange(0, Ngrid*H)/Ngrid

u = np.zeros(x.shape)

n = len(x)
A = np.eye(n)*(1.+2.*beta) + np.eye(n,k=1)*(-beta) + np.eye(n,k=-1)*(-beta)
A[0][0] = 1
A[0][1] = 0
A[-1][-1] = 1 + beta

plt.ion()
fig, ax = plt.subplots(1,1)
ax.set_ylim([0,7])
ax.set_xlim([0,5])
ax.set_xlabel(r'$y$ (cm)')
ax.set_ylabel(r'$u_x$ (cm/s)')

ax.plot(x, -geff*(0.5*x*x - H*x)/nu, '-k', label='Steady-state solution')

p, = ax.plot(x,u,'ro')

fig.canvas.draw()

for _ in range(Nsteps):
    
    u[1:] += geff*dt
    
    u = np.linalg.solve(A, u)
    p.set_ydata(u)
    
    fig.canvas.draw()
    ax.legend()
    
    plt.pause(0.005)