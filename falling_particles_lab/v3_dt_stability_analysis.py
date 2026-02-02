# PHYSICS MICRO-PROJECT
# Falling Particles under Gravity
# v3 – Time-Step Sweep & Numerical Stability Analysis
# Evaluates energy drift, penetration error, and stability vs timestep
# This version evaluates numerical stability only; no new physical effects are introduced.

# Methodology:
# Hypothesis → Experiment → Measurement → Falsification
#
# Focus:
# - Effect of timestep (dt) on numerical stability
# - Energy drift, penetration error, stability limits
# - Dimensionless stability parameter alpha
#
# Reproducibility:
# - Fixed random seed
# - Identical initial conditions for all dt runs

import numpy as np
import matplotlib.pyplot as plt

# Initial conditions (fixed for reproducibility) 

# All simulations use identical physics; observed differences arise solely from timestep discretization.

SEED = 42                   # A fixed random seed is used to ensure identical initial conditions across all dt runs.
np.random.seed(SEED)

n = 10                      # number of particles
g = np.array([0.0, -9.8])   # gravity
restitution = 1.0           # elastic collisions (important for v3)
steps = 500                 # timesteps per run
sim_time = None             # derived per dt

# dt sweep (log-spaced, intentional)
dt_values = [1e-3, 2e-3, 5e-3,
             1e-2, 2e-2, 5e-2,
             1e-1]

# Hypotheses:
# H1: Energy drift increases with dt
# H2: Penetration error increases nonlinearly with dt
# H3: There exists a dt_crit beyond which the simulation becomes unstable
# H4: For sufficiently small dt, results converge


# Simulation core function

def run_simulation(dt, steps, pos0, vel0):
    """
    Runs a single simulation with fixed dt.
    Returns logged measurements.
    """
    # The core simulation is defined as a function to enable controlled, repeatable experiments
    # where only the timestep (dt) varies while all initial conditions remain identical.

    pos = pos0.copy()
    vel = vel0.copy()

    energy_log = []
    penetration_log = []
    max_speed_log = []

    for _ in range(steps):
        # integration (Euler)
        vel = vel + g * dt
        pos = pos + vel * dt

        # collision detection
        hit_ground = pos[:, 1] < 0

        # penetration measurement (BEFORE correction)
        penetration = -pos[hit_ground, 1]
        max_penetration = np.max(penetration) if np.any(hit_ground) else 0.0

        # collision response
        vel[hit_ground, 1] *= -restitution          # Ground collisions are handled via discrete position correction, which introduces timestep-dependent error.
        pos[hit_ground, 1] = 0.0

        # measurements
        kinetic = 0.5 * np.sum(vel**2, axis=1)
        potential = -g[1] * pos[:, 1]   # m = 1
        total_energy = np.sum(kinetic + potential)

        speeds = np.linalg.norm(vel, axis=1)

        # logging
        energy_log.append(total_energy)
        penetration_log.append(max_penetration)
        max_speed_log.append(np.max(speeds))

        # Note: Bounce count is intentionally excluded in v3 since it depends strongly on timestep discretization
        # and does not serve as a reliable metric for numerical stability in a dt sweep.

    return {
        'energy': np.array(energy_log),
        'penetration': np.array(penetration_log),
        'max_speed': np.array(max_speed_log)
    }

# Experiment driver (dt sweep)
#==============================

# fixed initial conditions for reproducibility
pos_init = np.random.rand(n, 2) * 10
vel_init = np.zeros((n, 2))

results = {}

for dt in dt_values:
    logs = run_simulation(dt, steps, pos_init, vel_init)

    # derived quantities
    T = dt * steps
    energy_drift = logs["energy"][-1] - logs["energy"][0]
    max_penetration = np.max(logs["penetration"])

    # dimensionless stability parameter
    # alpha = g * dt / v_impact (use max speed as proxy)
    v_char = np.max(logs["max_speed"])
    alpha = (abs(g[1]) * dt / v_char) if v_char > 0 else 0.0

    results[dt] = {
        "logs": logs,
        "energy_drift": energy_drift,
        "energy_drift_rate": energy_drift / T,
        "max_penetration": max_penetration,
        "alpha": alpha
    }

# Analysis plots (v3-specific)

dts = np.array(list(results.keys()))
energy_drift_rates = np.array([results[dt]["energy_drift_rate"] for dt in dts])
max_penetrations = np.array([results[dt]["max_penetration"] for dt in dts])
alphas = np.array([results[dt]["alpha"] for dt in dts])

# Energy drift vs dt
plt.figure()
plt.loglog(dts, np.abs(energy_drift_rates), marker='o')
plt.xlabel("dt")
plt.ylabel("|Energy drift rate|")
plt.title("Energy Drift vs Timestep")
plt.grid(True)

# Penetration vs dt
plt.figure()
plt.loglog(dts, max_penetrations, marker='o')
plt.xlabel("dt")
plt.ylabel("Max penetration")
plt.title("Penetration Error vs Timestep")
plt.grid(True)

# Stability vs alpha
plt.figure()
plt.plot(alphas, max_penetrations, marker='o')
plt.xlabel("alpha (dimensionless)")
plt.ylabel("Max penetration")
plt.title("Stability vs Dimensionless Parameter α")
plt.grid(True)

plt.show()
