import numpy as np
import matplotlib.pyplot as plt
from instance_generation.instance_gen import *
from solver.Starting_Sol import *
from solver.cost_computation import cost_function, HopSequences
from solver.simulated_an import *
from solver.TabuSearch import *
import time


# -------PARAMETERS--------
# Algorithm parameters to generate the instance (requests and vehicles)

nb_passengers = 10        # Number of passengers  
nb_transfers = 3            # Number of vehicles -> consider a capacity from 2 to 12
min_distance = 1            # min distance weight for edges
max_distance = 10			# max distance weight for edges
min_time = 5                # min time weight for edges
max_time = 30               # max time weight for edges
min_degree = 2              # min degree of graph's nodes

# General parameter for simualation
max_iter = 1000

# Parameters for Simulated Annealing 
initial_temp = 1000
final_temp = 0.1
alpha = 0.95 # Reduction factor to pass from initial to final temperature after each iteration

# Parameters for Tabu Search
tabu_size = 0.1*max_iter # 10% of the max iteration size

# ------- END PARAMETERS--------

# Instance creation
Vehicles, Requests, Nodes, RemovedPassengers = generate_data(nb_passengers, nb_transfers)

G = createGraphInstance(Nodes, min_distance, max_distance, min_time, max_time, min_degree)
pos = nx.spring_layout(G)  # Generate layout for nodes


StartingSol = GenerateStartingSolution(Requests, Vehicles)

path_vector = HopSequences(Vehicles, Requests, StartingSol, G)


print("Available Vehicles: ", len(Vehicles), "--> Capacities: ", list(vehicle[1] for vehicle in Vehicles))
print("Number of requests: ", len(Requests))
print("Initial Solution: ", StartingSol)
print("Initial Solutions Cost: ", cost_function(path_vector, RemovedPassengers, G, Requests))
#visualize_graph(G, Vehicles, Requests)


# Running the Simulated Annealing algorithm
print("-----------")
print("SIMULATED ANNEALING")

start_time = time.time()
optimized_solution, optimized_cost, sa_costs = simulated_annealing(Vehicles, Requests, StartingSol, RemovedPassengers, G, initial_temp, final_temp, alpha, max_iter)
end_time = time.time()
print(f"Optimized solution: {optimized_solution}")
print(f"Optimized cost: {optimized_cost} with simulation time {end_time-start_time}")



plt.plot(sa_costs, label='Simulated Annealing')
plt.xlabel('Iteration')
plt.ylabel('Cost')
plt.title('Simulated Annealing Cost Over Iterations')
plt.legend()
plt.show()


# Running the Tabu Search Algorithm
print("--------")
print("TABU SEARCH")


start_time = time.time()
tabu_optimized_sol, tabu_optimized_cost, tabu_costs = tabu_search(Vehicles, Requests, G, StartingSol, RemovedPassengers, tabu_size, max_iter)
end_time = time.time()
print(f"Optimized solution TABU: {tabu_optimized_sol}")
print(f"Optimized cost TABU: {tabu_optimized_cost} with simulation time {end_time-start_time}")

plt.plot(tabu_costs, label='Tabu Search')
plt.xlabel('Iteration')
plt.ylabel('Cost')
plt.title('Tabu Search Cost Over Iterations')
plt.legend()
plt.show()

print("--------")
print("DIFFERENT PARAMS")
# Define the range for number of passengers and vehicles
passenger_range = [10, 15, 20]
vehicle_range = [3, 5]

# Initialize a dictionary to store results
results = {}

# Loop over each combination of passengers and vehicles
for nb_passengers in passenger_range:
    for nb_transfers in vehicle_range:
        print(f"Running for {nb_passengers} passengers and {nb_transfers} vehicles...")
        
        # Instance creation
        Vehicles, Requests, Nodes, RemovedPassengers = generate_data(nb_passengers, nb_transfers)
        G = createGraphInstance(Nodes, min_distance, max_distance, min_time, max_time, min_degree)
        StartingSol = GenerateStartingSolution(Requests, Vehicles)
        path_vector = HopSequences(Vehicles, Requests, StartingSol, G)
        init_cost = cost_function(path_vector, RemovedPassengers, G, Requests)
        # print("Initial Solutions Cost: ", init_cost)

        
        # Run Simulated Annealing
        sa_solution, sa_cost, sa_costs = simulated_annealing(
            Vehicles, Requests, StartingSol, RemovedPassengers, G, 
            initial_temp, final_temp, alpha, max_iter
        )
        
        # Run Tabu Search
        tabu_solution, tabu_cost, tabu_costs = tabu_search(
            Vehicles, Requests, G, StartingSol, RemovedPassengers, 
            tabu_size, max_iter
        )
        
        # Store results in the dictionary
        results[(nb_passengers, nb_transfers)] = {
        	'init_cost': init_cost,
            'sa_solution': sa_solution,
            'sa_cost': sa_cost,
            'sa_costs': sa_costs,
            'tabu_solution': tabu_solution,
            'tabu_cost': tabu_cost,
            'tabu_costs': tabu_costs
        }


print("Results summary:")
for (nb_passengers, nb_transfers), data in results.items():
    print(f"Passengers: {nb_passengers}, Vehicles: {nb_transfers}")
    print(f"Inital Cost: {data["init_cost"]}, SA Cost: {data['sa_cost']}, Tabu Cost: {data['tabu_cost']}")
    print("---")

