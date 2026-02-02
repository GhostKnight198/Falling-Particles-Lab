# PHYSICS MICRO-PROJECT
# Falling Particles under Gravity
# v1 - basic gravity and bounce

import numpy as np
import matplotlib.pyplot as plt


n = 10 # number of particles

pos = np.random.rand(n, 2) * 10 # initial positions
vel = np.zeros((n, 2))          # initial velocities

# np.random.rand generates uniform random numbers in [0, 1)
# Scale by 10 to get positions in [0, 10)
# np.zeros creates an array of zeros for initial velocities

g = np.array([0.0, -9.8])       # gravity vector
dt = 0.1                        # time step

# time steps are used instead of continuous time for simulation because computers operate in discrete intervals

#plotting & bounce setup

plt.ion()                       

for i in range(200):
    vel = vel + g * dt
    pos = pos + vel * dt

    hit_ground = pos[:, 1] < 0
    vel[hit_ground, 1] *= -0.8 # reverse y-velocity and apply damping
    pos[hit_ground, 1] = 0

    # hit_ground is a boolean array indicating which particles have hit the ground
    # For those particles, we reverse their y-velocity and apply a damping factor of 0.8
    # We also reset their y-position to 0 to keep them above the ground
    # This simulates a bounce with energy loss
    
    #plotting

    plt.clf()
    plt.scatter(pos[:, 0], pos[:, 1])
    plt.xlim(0, 10)
    plt.ylim(0, 10)
    plt.pause(0.05) 


