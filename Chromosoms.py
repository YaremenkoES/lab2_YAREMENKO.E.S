import random

def eval_func(chromosome):
    x, y, z = chromosome
    fitness = 1 / (1 + (x - 2)**2 + (y + 1)**2 + (z - 1)**2)
    return fitness,

def initialize_population(population_size, chromosome_length):
    return [(random.uniform(-10, 10), random.uniform(-10, 10), random.uniform(-10, 10)) for _ in range(population_size)]

def crossover(parent1, parent2):
    crossover_point = random.randint(0, 2)
    child = parent1[:crossover_point] + parent2[crossover_point:]
    return child

def mutate(chromosome, mutation_rate):
    mutated_chromosome = list(chromosome)
    for i in range(3):
        if random.random() < mutation_rate:
            mutated_chromosome[i] += random.uniform(-1, 1)
    return tuple(mutated_chromosome)

def genetic_algorithm(population_size, generations, mutation_rate, chromosome_length):
    population = initialize_population(population_size, chromosome_length)

    for generation in range(generations):
        population = sorted(population, key=eval_func, reverse=True)

        parents = population[:population_size // 2]

        offspring = []
        while len(offspring) < population_size - len(parents):
            parent1, parent2 = random.sample(parents, 2)
            child = crossover(parent1, parent2)
            child = mutate(child, mutation_rate)
            offspring.append(child)

        population = parents + offspring

# Max 
    best_solution = max(population, key=eval_func)
    return best_solution, eval_func(best_solution)

if __name__ == "__main__":
    population_size = 100
    generations = 50
    mutation_rate = 0.1
    chromosome_length = 3  # Довжина хромосоми

    best_solution, best_fitness = genetic_algorithm(population_size, generations, mutation_rate, chromosome_length)

    print("Best Solution:", best_solution)
    print("Best Fitness:", best_fitness)
