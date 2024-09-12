import math
import random
from solver.cost_computation import *
from solver.Starting_Sol import *

def simulated_annealing(Vehicles, Requests, initial_solution, RemovedPassengers, G, initial_temp=1000, final_temp=1, alpha=0.95, max_iter=1000):
    """
    Simulated Annealing to solve the DARPT.
    """
    # Start with the initial solution
    current_solution = initial_solution
    current_cost = cost_function(HopSequences(Vehicles, Requests, current_solution, G), RemovedPassengers, G, Requests)
    best_solution = current_solution
    best_cost = current_cost

    temp = initial_temp
    costs = [current_cost]  # Track the cost over iterations

    for iteration in range(max_iter):
        # Generate a neighbor solution
        neighbor_solution = generate_neighbor(current_solution, Vehicles)

        # Calculate the cost of the neighbor solution
        neighbor_cost = cost_function(HopSequences(Vehicles, Requests, neighbor_solution, G), RemovedPassengers, G, Requests)

        # Calculate the acceptance probability
        if neighbor_cost < current_cost:
            acceptance_prob = 1.0  # Accept if the cost is lower
        else:
            #It uses the Boltzmann factor to accept the neighbor (with a higher prob) eventhough it has a higher cost than before
            acceptance_prob = math.exp((current_cost - neighbor_cost) / temp)  # Accept with some probability if cost is higher

        # Decide whether to accept the neighbor solution
        if acceptance_prob > random.random(): # probabilistically decides whether to accept the new solution
            current_solution = neighbor_solution
            current_cost = neighbor_cost

            # Update the best solution found
            if current_cost < best_cost:
                best_solution = current_solution
                best_cost = current_cost

        costs.append(current_cost)  # Save the current cost
        
        # Decrease the temperature
        temp *= alpha

        # Stop if the temperature is low enough
        if temp < final_temp:
            break

    return best_solution, best_cost, costs


def generate_neighbor(solution, Vehicles):
    """
    Generate a neighboring solution by randomly swapping requests between vehicles.
    """
    neighbor_solution = [list(sol) for sol in solution]  # Copy the current solution
    # Choose two random vehicles
    vehicle1, vehicle2 = random.sample(range(len(solution)), 2) # Picks to random vehicles from the ones available on the solution

    if neighbor_solution[vehicle1] and neighbor_solution[vehicle2]: # Checks that both of the vehicles have a request assigned
        
        request1 = random.choice(neighbor_solution[vehicle1]) # Picks randomly a request from the list of vehicle1
        request2 = random.choice(neighbor_solution[vehicle2]) # Picks randomly a request from the list of vehicle2

        # Swap the requests between vehicles
        neighbor_solution[vehicle1].remove(request1)
        neighbor_solution[vehicle2].remove(request2)

        neighbor_solution[vehicle1].append(request2)
        neighbor_solution[vehicle2].append(request1)

    return neighbor_solution
