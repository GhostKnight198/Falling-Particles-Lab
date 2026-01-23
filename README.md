# Falling-Particles-Lab
A research-style physics micro-project investigating particle dynamics, numerical discretization, and simulation stability through incremental experiments.

This project is intentionally structured as a sequence of versions, each relaxing assumptions or adding analytical capability, mirroring how small-scale physics and simulation research is often conducted.

## Project Motivation

The goal of this project is not visual realism, but **understanding**:
- how physical models are discretized
- how numerical choices affect simulated behavior
- where and why simulations fail
- how to reason about systems, not just equations

It also serves as a personal lab notebook documenting my progression in physics modeling, numerical simulation, and system-level thinking.

## Version Overview

- **v1 – Basic Simulation**  
  2D particles under gravity using Euler integration and real-time visualization.

- **v2 – Measurements & Logging**  
  Adds structured measurement of total energy, velocity, penetration, and collision events.

- **v3 – Time-Step Sweep & Stability Analysis**  
  Treats the simulator itself as the subject of study by sweeping timestep values and analyzing numerical stability, energy drift, and collision error.

Each version is self-contained and runnable as a standalone Python script.

## Project Structure
falling-particles-lab/
├─ v1_basic_sim/
├─ v2_measurements/
├─ v3_dt_sweep/



## Notes

- All simulations use identical physics; observed differences in v3 arise solely from timestep discretization.
- Numerical validation is prioritized over visual fidelity.
- Later versions (v4+) will introduce dissipation, improved integration schemes, and feedback/control mechanisms.

---

*This project is a learning and experimentation space rather than a polished physics engine.*

