import numpy as np
from deap import base, creator, tools, algorithms

chromosome_length = 3

creator.create("FitnessMax", base.Fitness, weights=(1.0,))
creator.create("Individual", np.ndarray, fitness=creator.FitnessMax)

toolbox = base.Toolbox()
toolbox.register("attr_float", np.random.uniform, -10, 10) 
toolbox.register("individual", tools.initRepeat, creator.Individual, toolbox.attr_float, n=chromosome_length)
toolbox.register("population", tools.initRepeat, list, toolbox.individual)

def eval_func(individual):
    x, y, z = individual
    result = 1 / (1 + (x - 2)**2 + (y + 1)**2 + (z - 1)**2)
    return result,

toolbox.register("evaluate", eval_func)

toolbox.register("mate", tools.cxBlend, alpha=0.5)
toolbox.register("mutate", tools.mutGaussian, mu=0, sigma=1, indpb=0.2)

toolbox.register("select", tools.selTournament, tournsize=3)

def main():
    
    population = toolbox.population(n=50)

    cxpb, mutpb, ngen = 0.7, 0.2, 40

    algorithms.eaMuPlusLambda(population, toolbox, mu=50, lambda_=200, cxpb=cxpb, mutpb=mutpb, ngen=ngen, stats=None, halloffame=None, verbose=True)

    best_individual = tools.selBest(population, k=1)[0]
    print("Найкращий індивід: ", best_individual)
    print("Значення фітнес-функції: ", best_individual.fitness.values)

if name == "main":
    main()
