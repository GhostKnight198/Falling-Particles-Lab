# PHYSICS MICRO-PROJECT
# Falling Particles under Gravity
# v4.5 – Drag Coefficient Sweep & Damping Regimes

# Focus:
# Study how linear air resistance alters system behavior by sweeping drag coefficients.
# Analyze energy dissipation, terminal velocity emergence, and collision penetration trends.

# Hypotheses:
# H1: Higher drag coefficients lead to faster energy dissipation.
# H2: Terminal velocities decrease with increasing drag.
# H3: Penetration depth decreases as drag increases.
# H4: Distinct damping regimes emerge across drag values.

import numpy as np
import matplotlib.pyplot as plt

# Reproducibility
SEED = 42
np.random.seed(SEED)

# Simulation parameters
n = 10
g = np.array([0.0, -9.8])
restitution = 0.8
dt = 1e-2
steps = 500
drag_coeffs = [0.05, 0.1, 0.2, 0.5]

# Initial conditions (shared across runs)
pos_init = np.random.rand(n, 2) * 10
vel_init = np.zeros((n, 2))


def run_simulation(dt, steps, c, pos0, vel0):
    pos = pos0.copy()
    vel = vel0.copy()

    energy_log = []
    penetration_log = []
    max_speed_log = []

    for _ in range(steps):
        # acceleration: gravity + linear drag
        a = g - c * vel

        # Euler integration
        vel += a * dt
        pos += vel * dt

        # collision detection
        hit_ground = pos[:, 1] < 0

        # penetration measurement (before correction)
        penetration = -pos[hit_ground, 1]
        max_penetration = np.max(penetration) if np.any(hit_ground) else 0.0

        # collision response
        vel[hit_ground, 1] *= -restitution
        pos[hit_ground, 1] = 0.0

        # measurements
        kinetic = 0.5 * np.sum(vel**2, axis=1)
        potential = -g[1] * pos[:, 1]  # m = 1
        total_energy = np.sum(kinetic + potential)

        max_speed = np.max(np.linalg.norm(vel, axis=1))

        # logging
        energy_log.append(total_energy)
        penetration_log.append(max_penetration)
        max_speed_log.append(max_speed)

    return {
        "energy": np.array(energy_log),
        "penetration": np.array(penetration_log),
        "max_speed": np.array(max_speed_log)
    }


# Run parameter sweep
results = {}
for c in drag_coeffs:
    results[c] = run_simulation(dt, steps, c, pos_init, vel_init)



# Analysis Plots
# -------------------------------

time = np.arange(steps) * dt

# Energy vs time
plt.figure()
for c in drag_coeffs:
    plt.plot(time, results[c]["energy"], label=f"c = {c}")
plt.xlabel("Time")
plt.ylabel("Total Energy")
plt.title("Energy Dissipation vs Drag Coefficient")
plt.legend()
plt.grid(True)

# Max speed vs time
plt.figure()
for c in drag_coeffs:
    plt.plot(time, results[c]["max_speed"], label=f"c = {c}")
plt.xlabel("Time")
plt.ylabel("Max Speed")
plt.title("Velocity Damping vs Drag Coefficient")
plt.legend()
plt.grid(True)

# Penetration vs time
plt.figure()
for c in drag_coeffs:
    plt.plot(time, results[c]["penetration"], label=f"c = {c}")
plt.xlabel("Time")
plt.ylabel("Max Penetration")
plt.title("Collision Penetration vs Drag Coefficient")
plt.legend()
plt.grid(True)

plt.show()
