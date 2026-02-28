# PHYSICS MICRO-PROJECT
# Falling Particles under Gravity
# v4 – Linear Air Resistance
#
# Focus:
# Introduce a physically motivated dissipative force (linear air resistance)
# while keeping the numerical integration scheme unchanged, and study how
# dissipation alters energy behavior, particle speeds, and collision artifacts.
#
# Hypotheses:
# H1: Total mechanical energy will decrease monotonically due to air resistance.
# H2: Particle speeds will asymptotically approach a terminal velocity.
# H3: Ground penetration depth will decrease over time as kinetic energy is dissipated.
# H4: Numerical penetration errors will persist due to discrete collision handling,
#     but their magnitude will diminish as particle speeds decrease.
#
# Notes:
# - Explicit Euler integration is intentionally retained from v3.
# - Energy conservation is no longer expected.
# - Bounce count is excluded since dissipation dominates long-term behavior.

import numpy as np
import matplotlib.pyplot as plt 

# Reproducibility
SEED = 42
np.random.seed(SEED)

# simulation parameters
n = 10
g = np.array([0.0, -9.8])
restitution = 0.8
dt = 1e-2
steps = 500
c = 0.1

# Initial conditions
pos_init = np.random.rand(n, 2) * 10
vel_init = np.zeros((n, 2))

# Simulation Core
# -------------------------------

def run_simulation(dt, steps, c, pos0, vel0):
    pos = pos0.copy()
    vel = vel0.copy()

    energy_log = []
    penetration_log = []
    max_speed_log = []

    for _ in range(steps):

         # acceleration (gravity + linear drag)
        a = g - c * vel

        # explicit Euler integration
        vel = vel + a * dt
        pos = pos + vel * dt

        # ground collision detection
        hit_ground = pos[:, 1] < 0

         # penetration measurement (before correction)
        penetration = -pos[hit_ground, 1]
        max_penetration = np.max(penetration) if np.any(hit_ground) else 0.0

         # collision response
        vel[hit_ground, 1] *= -restitution
        pos[hit_ground, 1] = 0.0

        # Energies & speeds
        kinetic = 0.5 * np.sum(vel**2, axis=1)
        potential = -g[1] * pos[:, 1]
        total_energy = np.sum(kinetic + potential)

        speeds = np.linalg.norm(vel, axis=1)

        # logging
        energy_log.append(total_energy)
        penetration_log.append(max_penetration)
        max_speed_log.append(np.max(speeds))

    return {
        "energy": np.array(energy_log),
        "penetration": np.array(penetration_log),
        "max_speed": np.array(max_speed_log)
    }

# Run simulation
logs = run_simulation(dt, steps, c, pos_init, vel_init)
time = np.arange(steps) * dt


# Analysis plots
# -------------------------------
plt.figure()
plt.plot(time, logs["energy"])
plt.xlabel("Time")
plt.ylabel("Total Energy")
plt.title("Energy Decay with Linear Air Resistance (v4)")
plt.grid(True)

plt.figure()
plt.plot(time, logs["max_speed"])
plt.xlabel("Time")
plt.ylabel("Max Speed")
plt.title("Approach to Terminal Velocity (v4)")
plt.grid(True)

plt.figure()
plt.plot(time, logs["penetration"])
plt.xlabel("Time")
plt.ylabel("Max Penetration")
plt.title("Ground Penetration vs Time (v4)")
plt.grid(True)

plt.show()

