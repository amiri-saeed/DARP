from solver.cost_computation import *
import random


def tabu_search(Vehicles, Requests, G, initial_solution, RemovedPassengers, tabu_size, max_iter):
    # Initial setup
    current_solution = initial_solution
    path_vectors = HopSequences(Vehicles, Requests, current_solution, G)
    current_cost = cost_function(path_vectors, RemovedPassengers, graph=G, Requests=Requests)
    best_solution = current_solution
    best_cost = current_cost

    # Tabu list to keep track of recently visited solutions
    tabu_list = []

    costs = [current_cost]  # Track the cost over iterations
    
    for iteration in range(max_iter):
        # Generate a neighboring solution
        neighbor_solution = generate_neighbor(current_solution)
        neighbor_path_vectors = HopSequences(Vehicles, Requests, neighbor_solution, G)
        neighbor_cost = cost_function(neighbor_path_vectors, RemovedPassengers, graph=G, Requests=Requests)

        # Check if the neighbor is the best solution found so far
        if neighbor_cost < best_cost:
            best_solution = neighbor_solution
            best_cost = neighbor_cost

        # Check if the neighbor is better than the current solution or not in the tabu list
        if neighbor_cost < current_cost or (neighbor_solution not in tabu_list):
            current_solution = neighbor_solution
            current_cost = neighbor_cost
            tabu_list.append(current_solution)

        costs.append(current_cost)  # Save the current cost

        # Maintain the size of the tabu list
        if len(tabu_list) > tabu_size:
            tabu_list.pop(0)
    # print("TABU LIST:", tabu_list)
    
    return best_solution, best_cost, costs

def generate_neighbor(solution):
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