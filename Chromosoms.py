import numpy as np
from deap import base, creator, tools, algorithms

# Задаємо довжину хромосоми (3 параметри x, y, z)
chromosome_length = 3

# Визначаємо тип хромосом та фітнес-функції
creator.create("FitnessMax", base.Fitness, weights=(1.0,))
creator.create("Individual", np.ndarray, fitness=creator.FitnessMax)

# Ініціалізація параметрів генетичного алгоритму
toolbox = base.Toolbox()
toolbox.register("attr_float", np.random.uniform, -10, 10)  # Вибираємо значення з діапазону [-10, 10]
toolbox.register("individual", tools.initRepeat, creator.Individual, toolbox.attr_float, n=chromosome_length)
toolbox.register("population", tools.initRepeat, list, toolbox.individual)

# Визначаємо функцію оцінки (fitnes-функцію)
def eval_func(individual):
    x, y, z = individual
    result = 1 / (1 + (x - 2)**2 + (y + 1)**2 + (z - 1)**2)
    return result,

# Реєструємо функцію оцінки в toolbox
toolbox.register("evaluate", eval_func)

# Реєструємо кросовер та мутацію
toolbox.register("mate", tools.cxBlend, alpha=0.5)
toolbox.register("mutate", tools.mutGaussian, mu=0, sigma=1, indpb=0.2)

# Реєструємо вибірку для відбору
toolbox.register("select", tools.selTournament, tournsize=3)

def main():
    # Створюємо початкову популяцію
    population = toolbox.population(n=50)

    # Встановлюємо параметри еволюції
    cxpb, mutpb, ngen = 0.7, 0.2, 40

    # Викликаємо еволюційний процес
    algorithms.eaMuPlusLambda(population, toolbox, mu=50, lambda_=200, cxpb=cxpb, mutpb=mutpb, ngen=ngen, stats=None, halloffame=None, verbose=True)

    # Отримуємо найкращий індивід
    best_individual = tools.selBest(population, k=1)[0]
    print("Найкращий індивід: ", best_individual)
    print("Значення фітнес-функції: ", best_individual.fitness.values)

if name == "main":
    main()
