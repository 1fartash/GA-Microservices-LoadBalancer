import numpy as np
import random

# Simulation Parameters
NUM_REQUESTS = 100
NUM_SERVICES = 10
POPULATION_SIZE = 50
GENERATIONS = 100
CROSSOVER_RATE = 0.8
MUTATION_RATE = 0.05

# Generate heterogeneous processing times for services
t_matrix = np.random.randint(10, 100, size=(NUM_REQUESTS, NUM_SERVICES))

def calculate_makespan(chromosome):
    loads = np.zeros(NUM_SERVICES)
    for req_idx, service_idx in enumerate(chromosome):
        loads[service_idx] += t_matrix[req_idx, service_idx]
    return np.max(loads)

def fitness(chromosome):
    makespan = calculate_makespan(chromosome)
    return 1.0 / (makespan + 1e-6)

def initialize_population():
    return [np.random.randint(0, NUM_SERVICES, NUM_REQUESTS).tolist() 
            for _ in range(POPULATION_SIZE)]

def crossover(parent1, parent2):
    if random.random() < CROSSOVER_RATE:
        point = random.randint(1, NUM_REQUESTS - 1)
        return parent1[:point] + parent2[point:], parent2[:point] + parent1[point:]
    return parent1[:], parent2[:]

def mutate(chromosome):
    for i in range(NUM_REQUESTS):
        if random.random() < MUTATION_RATE:
            chromosome[i] = random.randint(0, NUM_SERVICES - 1)
    return chromosome

# Main GA Loop
population = initialize_population()
best_fitness_history = []

for gen in range(GENERATIONS):
    # Evaluate Fitness
    fitness_scores = [fitness(chrom) for chrom in population]
    
    # Sort population (Elitism)
    sorted_indices = np.argsort(fitness_scores)[::-1]
    population = [population[i] for i in sorted_indices]
    
    best_fitness_history.append(fitness_scores[sorted_indices[0]])
    new_population = [population[0]] # Keep the best (Elitism)
    
    # Generate new offspring
    while len(new_population) < POPULATION_SIZE:
        p1, p2 = random.choices(population[:10], k=2) # Simple tournament
        o1, o2 = crossover(p1, p2)
        new_population.extend([mutate(o1), mutate(o2)])
        
    population = new_population[:POPULATION_SIZE]

print(f"Final Optimized Makespan: {calculate_makespan(population[0])} ms")
