# Falling-Particles-Lab
A research-style physics micro-project investigating particle dynamics, numerical discretization, and simulation stability through incremental experiments.

This project is intentionally structured as a sequence of versions, each relaxing assumptions or adding analytical capability, mirroring how small-scale physics and simulation research is often conducted.

## Project Motivation

The goal of this project is not visual realism, but **understanding**:
- how physical models are discretized
- how numerical choices affect simulated behavior
- where and why simulations fail
- how dissipation alters system dynamics
- how to reason about systems, not just equations

It also serves as a personal lab notebook documenting my progression in physics modeling, numerical simulation, and system-level thinking.

## Version Overview

- **v1 – Basic Simulation**  
  2D particles under gravity using Euler integration and real-time visualization.

- **v2 – Measurements & Logging**  
  Adds structured measurement of total energy, velocity, penetration, and collision events.

- **v3 – Time-Step Sweep & Stability Analysis**  
  Treats the simulator itself as the subject of study by sweeping timestep values and analyzing numerical stability, energy drift, and collision error.

- **v4 - Linear Air Resistance**
  Introduces Linear drag , while retaining Euler Integration
  Analyzes energy dissipation, terminal velocity emergence, interaction between physical damping and numerical collision artifacts

- **v4.5 - Drag Sweep**
  Extends v4 by sweeping multiple drag coefficients to compare energy decay rates, terminal velocity scaling, penetration behaviour across damping regimes

Each version is self-contained and runnable as a standalone Python script.

## Project Structure
falling-particles-lab
├─ v1_basic_sim
├─ v2_measurements
├─ v3_dt_sweep
├─ v4_linear_drag
├─ v4_5_drag_sweep



## Notes

- All simulations use identical physics; observed differences in v3 arise solely from timestep discretization.
- Numerical validation is prioritized over visual fidelity.
- This project prioritizes conceptual clarity and numerical reasoning over performance or physical completeness.
- v1–v3 use conservative physics; deviations arise from discretization.
- v4+ introduce physical dissipation.
- Future versions (v5+) will introduce convergence testing, analytic validation, and integrator comparison.

---

*This project is a learning and experimentation space rather than a polished physics engine.*

