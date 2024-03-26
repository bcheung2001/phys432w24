# -*- coding: utf-8 -*-
"""
(PS4 Q3)
The following script produces an animation which models a strong adiabatic shock

@author: Benjamin Cheung
2023-03-25
"""

import numpy as np
import matplotlib.pyplot as plt

def advect(f, u, dt, dx): #Helper function for the advection step
    
    n = len(f)
    
    J = np.zeros(n-1) #Fluxes

    for i in range(n-1):
        if u[i] > 0: #Compute the flux
            J[i] = f[i]*u[i]
        else:
            J[i] = f[i+1]*u[i]
    
    f[1:-1] = f[1:-1] - (dt/dx)*(J[1:] - J[:-1]) #Advect
    
    f[0] = f[0] - (dt/dx)*J[0]
    f[-1] = f[-1] + (dt/dx)*J[-1]

    return f

def gaussian(x,amp,width): #Generate Gaussian centered at the origin
    return amp*np.exp(-(x/width)**2)

Nsteps = 3000 #Simulation runtime
Ngrid = 500 #Grid size

gamma = 5.0/3.0 #Adiabatic index

x = np.linspace(0,1,Ngrid)
dx = x[1] - x[0] #Set dx and dt
dt = 0.02*dx

f1 = np.ones(Ngrid) #Density
f2 = np.zeros(Ngrid) #Momentum density
f3 = np.ones(Ngrid) + gaussian(x, 250, 0.1) #Energy density; a Gaussian perturbation at the origin
                                            #is added to produce a strong shock propagating to the right
u = f2/f1
P = (gamma - 1)*(f3 - f1*(u**2)/2) #Compute pressure and sound speed (see submission pdf for details)
cs2 = gamma*P/f1

plt.ion()

fig,ax = plt.subplots(2,1)

ax[0].set_xlim(0,1)
ax[1].set_xlim(0,1)
ax[0].set_ylim(0,5)
ax[1].set_ylim(-2,2)
ax[0].grid()
ax[1].grid()

ax[0].set_ylabel('Density')
ax[1].set_ylabel('Mach number')

p1, = ax[0].plot(x,f1, 'r.')
p2, = ax[1].plot(x, f2/f1/(np.sqrt(cs2)), 'b.')

for _ in range(Nsteps):
    
    u_bound = ((f2[:-1]/f1[:-1]) + (f2[1:]/f1[1:]))/2 #Compute cell boundary velocities
    
    f1 = advect(f1, u_bound, dt, dx) #Advect density, then momentum
    f2 = advect(f2, u_bound, dt, dx)
    
    u = f2/f1
    P = (gamma - 1)*(f3 - f1*(u**2)/2) #Compute pressure
    
    f2[1:-1] = f2[1:-1] - (dt/dx/2)*(P[2:] - P[:-2]) #Apply pressure gradient force to momentum 
    f2[0] = f2[0] - (dt/dx/2)*(P[1]-P[0]) #Apply reflective boundary conditions
    f2[-1] = f2[-1] - (dt/dx/2)*(P[-1]-P[-2])
    
    u_bound = ((f2[:-1]/f1[:-1]) + (f2[1:]/f1[1:]))/2 #Recompute advection velocities
    
    f3 = advect(f3, u_bound, dt, dx) #Advect energy
    
    u = f2/f1
    P = (gamma - 1)*(f3 - f1*(u**2)/2) #Recompute pressure
    
    f3[1:-1] = f3[1:-1] - (dt/dx/2)*(P[2:]*u[2:] - P[:-2]*u[:-2]) #Apply pressure to energy equation
    f3[0] = f3[0] - (dt/dx/2)*(P[1]*u[1] - P[0]*u[0]) #Apply reflective boundary conditions
    f3[-1] = f3[-1] - (dt/dx/2)*(P[-1]*u[-1] - P[-2]*u[-2]) 
    
    P = (gamma - 1)*(f3 - (f2**2/f1/2)) #Recompute pressure and sound speed
    cs2 = gamma*P/f1
    
    p1.set_ydata(f1) #Update plots
    p2.set_ydata(f2/f1/(np.sqrt(cs2)))    
    
    plt.pause(0.001)
