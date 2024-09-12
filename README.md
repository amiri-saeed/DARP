# DARP

# Dial-a-Ride Problem (DARP) Optimization

This repository contains code to solve a Dial-a-Ride Problem (DARP) using Simulated Annealing and Tabu Search algorithms. The code generates problem instances and runs optimization experiments across different parameter settings for the number of passengers and vehicles.

## Prerequisites

- Python 3.x
- Required packages:
  ```bash
  pip install numpy matplotlib networkx

## Running the Experiments
1. Clone this repository:

```bash
git clone https://github.com/amiri-saeed/DARP.git
```

2. Run the main script:

```bash
python main.py
```
The script will generate problem instances, run Simulated Annealing and Tabu Search algorithms, and display plots of costs over iterations. Results for different combinations of passengers and vehicles will also be printed.

## Output
- Initial and optimized costs for both algorithms.
- Plots of cost over iterations for each algorithm.
- Results summary for different configurations of passengers and vehicles.
