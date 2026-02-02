# PHYSICS MICRO-PROJECT
# Falling Particles under Gravity
# v2 - Particle Dynamics with Measurements
# Tracks total energy, max velocity, penetration, and bounce count

import numpy as np
import matplotlib.pyplot as plt

# Simulation parameters
n = 10 # number of particles
pos = np.random.rand(n, 2) * 10 # initial positions
vel = np.zeros((n, 2))          # initial velocities
g = np.array([0.0, -9.8])       # gravity vector
dt = 0.1                        # time step
steps = 200                     # number of simulation steps

# Measurement logs
energy_log = []                 # total mechanical energy per timestep
max_speed_log = []              # max particle speed per timestep
max_penetration_log = []        # max depth below ground per timestep
bounce_count_log = []           # number of particles hitting ground per timestep

#plotting & measurement setup

plt.ion()                       

for i in range(steps):
    # euler integration
    vel = vel + g * dt
    pos = pos + vel * dt

    # collision detection
    hit_ground = pos[:, 1] < 0
    
    # measurements per timestep
    kinetic_energy = 0.5 * np.sum(vel**2, axis=1)
    potential_energy = -g[1] * pos[:, 1]           # m = 1
    total_energy = np.sum(kinetic_energy + potential_energy)

    speeds = np.linalg.norm(vel, axis=1)
    max_speed = np.max(speeds)
    max_penetration = np.max(-pos[:, 1][hit_ground]) if np.any(hit_ground) else 0.0
    bounce_count = np.sum(hit_ground)

    # bounce response
    vel[hit_ground, 1] *= -0.8   # damping factor 
    pos[hit_ground, 1] = 0

    # logging measurements
    energy_log.append(total_energy)
    max_speed_log.append(max_speed)
    max_penetration_log.append(max_penetration)
    bounce_count_log.append(bounce_count)


    #plotting

    plt.clf()
    plt.scatter(pos[:, 0], pos[:, 1])
    plt.xlim(0, 10)
    plt.ylim(0, 10)
    plt.pause(0.01)

plt.ioff()
plt.show()

#====================================================================
# Optional post-simulation plots
# Uncomment the following section to visualize logged measurements
#====================================================================

# Post-simulation analysis plots

# Optional thresholds for reference (example values)
#energy_threshold = max(energy_log) * 1.05  # 5% above max energy
#speed_threshold  = max(max_speed_log) * 1.05

#fig, axs = plt.subplots(4, 1, figsize=(7, 10), sharex=True)

# 1️ Total Energy
#axs[0].plot(energy_log, color='blue', label='Total Energy')
#axs[0].axhline(energy_threshold, color='gray', linestyle='--', label='Energy Threshold')
#axs[0].set_ylabel('Total Energy')
#axs[0].set_title('Post-Simulation Summary - v2')
#axs[0].legend()
#axs[0].grid(True)

# 2️ Max Speed
#axs[1].plot(max_speed_log, color='green', label='Max Speed')
#axs[1].axhline(speed_threshold, color='gray', linestyle='--', label='Speed Threshold')
#axs[1].set_ylabel('Max Speed')
#axs[1].legend()
#axs[1].grid(True)

# 3️ Max Penetration
#axs[2].plot(max_penetration_log, color='red', label='Max Penetration')
#axs[2].set_ylabel('Max Penetration')
#axs[2].legend()
#axs[2].grid(True)

# 4️ Bounce Count
#axs[3].plot(bounce_count_log, color='purple', label='Bounce Count')
#axs[3].set_ylabel('Bounces')
#axs[3].set_xlabel('Timestep')
#axs[3].legend()
#axs[3].grid(True)

#plt.tight_layout()
#plt.show()

