# -*- coding: utf-8 -*-
"""
Insert description of the code

@author: Benjamin Cheung
2023-02-11
"""
import numpy as np
import matplotlib.pyplot as pl

dt = 0.01
Nsteps = 1000

## Setting up initial conditions (vortex centres and circulation)
# Vortex rings
y_v = np.array([1, 1, -1, -1])
x_v = np.array([-2, -4, -2, -4])
k_v = np.array([1, 1, -1, -1]) 

# Setting up the plot
pl.ion()
fig, ax = pl.subplots(1,1,figsize=(4,4))
# mark the initial positions of vortices
p, = ax.plot(x_v, y_v, 'k+', markersize=10) 
#play around with the marker size and type as you see fit

# draw the initial velocity streamline
ngrid = 5
Y, X = np.mgrid[-ngrid:ngrid:360j, -ngrid:ngrid:360j] 
#360j sets the resolution of the cartesian grid; play around with it as you see fit
vel_x = np.zeros(np.shape(Y)) #this holds x-velocity
vel_y = np.zeros(np.shape(Y)) #this holds y-velocity

# masking radius for better visualization of the vortex centres
r_mask = 0.15 
#within this mask, you will not plot any streamline 
#so that you can see more clearly the movement of the vortex centres

#for i in range(len(x_v)): #looping over each vortex
    # insert lines for computing the total velocity field
    # insert lines for masking (set the masking area to NaN)

# set up the boundaries of the simulation box
ax.set_xlim([-ngrid, ngrid])
ax.set_ylim([-ngrid, ngrid])

# initial plot of the streamlines
ax.streamplot(X, Y, vel_x, vel_y, density=[1, 1]) 
#play around with density as you see fit; 
#see the API documentation for more detail

fig.canvas.draw()

# Evolution
count = 0
while count < Nsteps:
    ## Compute and update advection velocity
    # insert lines to re-initialize the total velocity field
    #for i in range(len(x_v)):
        # insert lines to compute the total
        # advection velocity on each vortex
    
    # insert lines to update the positions of vortices

    # insert lines to re-initialize the total velocity field
    #for i in range(len(x_v)):
        # insert lines to update the streamlines and masking

    ## update plot
    # the following two lines clear out the previous streamlines
    ax.collections = []
    ax.patches = []

    p.set_xdata(x_v)
    p.set_ydata(y_v)

    ax.streamplot(X, Y, vel_x, vel_y, density=[1, 1])

    fig.canvas.draw()
    pl.pause(0.001) #play around with the delay time for better visualization
    count += 1


