# Dial-a-Ride Problem (DARP) Optimization

This repository contains code to solve a Dial-a-Ride Problem (DARP) using Simulated Annealing and Tabu Search algorithms. The code generates problem instances and runs optimization experiments across different parameter settings for the number of passengers and vehicles.

## Prerequisites

- Python 3.x
- Required packages:

  pip install numpy matplotlib networkx

## Running the Experiments

1. Use the code files contained inside the folder. There should be four files on the root (figs folder, instance_generation folder, solver folder, main.py file)

2. Before running the main script consider the parameters to run the simulation, those could be changed on the top of the main.py file and will represent a direct impact on the instance generation and heuristic solutions. 

** The weights considered on the cost function could also be changed/adjusted as desiered, for doing so, the parameters will need to be adjusted for each function on the the cost_computation.py file at the inside of the solver folder. 

3. Once the parameters have already being set, execute the main and wait to visualize the printed results. 
```
The script will generate problem instances, run Simulated Annealing and Tabu Search algorithms, and display plots of costs over iterations. Results for different combinations of passengers and vehicles will also be printed.

## Output
- Initial and optimized costs for both algorithms.
- Plots of cost over iterations for each algorithm on a single scenario.
- Results summary for different scenarios of passengers and vehicles.
