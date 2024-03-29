# -*- coding: utf-8 -*-
"""
(PS2 Q3)
The following script produces an animation which models the "leapfrogging" vortex
rings seen in lecture.

@author: Benjamin Cheung
2023-02-12
"""
import numpy as np
import matplotlib.pyplot as pl

dt = 0.025
Nsteps = 60

## Setting up initial conditions (vortex centres and circulation)
# Vortex rings
y_v = np.array([1, 1, -1, -1])
x_v = np.array([-3, -4, -3, -4])
k_v = np.array([5, 5, -5, -5]) 

# Setting up the plot
pl.ion()
fig, ax = pl.subplots(1,1, figsize=(6,6))
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
r_mask = 0.25
#within this mask, you will not plot any streamline 
#so that you can see more clearly the movement of the vortex centres

for i in range(len(x_v)): #looping over each vortex
    
    x_diff = X - x_v[i]
    y_diff = Y - y_v[i]
    
    r = np.sqrt(x_diff**2 + y_diff**2)
    
    r_masked = np.where(r < r_mask, np.nan, r) #mask out region close to the vortex
    
    vel_x -= (k_v[i]*y_diff)/(r_masked**2) #update velocity fields
    vel_y += (k_v[i]*x_diff)/(r_masked**2) #see velocity calculations in pdf submission

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
    # re-initialize the total velocity field
    vel_x = np.zeros(np.shape(Y)) 
    vel_y = np.zeros(np.shape(Y)) 
    
    x_new = np.zeros(np.shape(x_v)) #placeholders for new vortex positions
    y_new = np.zeros(np.shape(y_v))
    
    for i in range(len(x_v)): #loop over each vertex
        ux = 0
        uy = 0
        
        for j in range(len(x_v)): #for each other vortex, compute velocity contribution
            if j == i:
                continue
            
            x_diff = x_v[i] - x_v[j]
            y_diff = y_v[i] - y_v[j]
            r = np.sqrt(x_diff**2 + y_diff**2)
            
            ux -= (k_v[j]*y_diff)/(r**2)
            uy += (k_v[j]*x_diff)/(r**2)
        
        x_new[i] = x_v[i] + ux*dt
        y_new[i] = y_v[i] + uy*dt
        
    x_v = x_new #update positions of the vortices
    y_v = y_new

   #compute the updated velocity field
    for i in range(len(x_v)):
        
        x_diff = X - x_v[i]
        y_diff = Y - y_v[i]
        
        r = np.sqrt(x_diff**2 + y_diff**2)
        
        r_masked = np.where(r < r_mask, np.nan, r)
        
        vel_x -= (k_v[i]*y_diff)/(r_masked**2)
        vel_y += (k_v[i]*x_diff)/(r_masked**2)

    ## update plot
    # the following two lines clear out the previous streamlines
    #ax.collections = []
    #ax.patches = []
    
    #The above code didn't work with my version of matplotlib, so I replaced them with this:
    for collection in ax.collections:
        collection.remove()
    for patch in ax.patches:
        patch.remove()

    p.set_xdata(x_v)
    p.set_ydata(y_v)
    
    ax.streamplot(X, Y, vel_x, vel_y, density=[1, 1], color='C0')

    fig.canvas.draw()
    pl.pause(0.001) #play around with the delay time for better visualization
    count += 1


