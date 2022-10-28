import numpy as np
import math as mt
import matplotlib.pyplot as plt

#Закон зміни похибки – експонентційний, рівномірний;
#Закон зміни досліджуваного процесу – квадратичний, постійна.

def uniform(n):
    distribution = np.random.rand(n)
    print(distribution)
    stats(distribution)
    plt.xlabel('Uniform Distribution')
    plt.hist(distribution, bins=20, facecolor="blue", alpha=0.5)
    plt.show()
    return distribution

def exponential(n):
    distribution = np.random.exponential(size = n)
    print(distribution)
    stats(distribution)
    plt.xlabel('Exponential Distribution')
    plt.hist(distribution, bins=20, facecolor="blue", alpha=0.5)
    plt.show()
    return distribution

def square(n, distribution, error, label): # квадратична модель
    distribution_1 = np.zeros(n)
    distribution_2 = np.zeros(n)
    for i in range(n):
        distribution_2[i] = (error * (i * i))
        distribution_1[i] = distribution_2[i] + distribution[i]
    plt.xlabel(label)
    plt.plot(distribution_1)
    plt.plot(distribution_2)
    plt.show()
    return distribution_1, distribution_2

def constant(n, const, error, distribution, label): # динаміка постійної модель, але треба лінійна
    masdistribution_3 = distribution_0 = np.zeros(n)
    for i in range(n):
        distribution_0[i] = (error * i)*const
        masdistribution_3[i] = distribution_0[i] + distribution[i]
    plt.xlabel(label)
    plt.plot(masdistribution_3)
    plt.plot(distribution_0)
    plt.show()
    return masdistribution_3, distribution_0

def stats(distribution):
    median_distribution = np.median(distribution)
    print("Mедіана - ", median_distribution)
    std_distribution = np.var(distribution)
    print("Дисперсія - ", std_distribution)
    skv_distribution = mt.sqrt(std_distribution)
    print("СКВ - ", skv_distribution)

def assessment(n, distribution_1, distribution_3, distribution_0, distribution, label):
    distribution_4 = np.zeros(n)
    for i in range(n):
        distribution_4[i] = (distribution_3[i] - distribution_0[i])
    plt.xlabel(label)
    plt.hist(distribution, bins=20, alpha=0.5, label='distribution')
    plt.hist(distribution_1, bins=20, alpha=0.5, label='distribution_1')
    plt.hist(distribution_3, bins=20, alpha=0.5, label='distribution_3')
    plt.hist(distribution_4, bins=20, alpha=0.5, label='distribution_4')
    plt.show()


n = 17500
dsigm = 5
dm = 5
error = 0.0000005
distribution = np.random.randn(n)
const = 5

uniform_distribution = uniform(n)
exponential_distribution = exponential(n)

#==============================================================================================
square_uniform, distribution_2 = square(n, uniform_distribution, error, "Динаміка Рівномірна - Квадратична")

plt.xlabel("гістограми законів розподілу Рівномірна - Квадратична")
plt.hist(uniform_distribution, label='distribution')
plt.hist(distribution, label='distribution_1')
plt.hist(square_uniform, label='distribution_3')
plt.show()
stats(square_uniform)

assessment(n, distribution, square_uniform, distribution_2, uniform_distribution, "оцінка статистичних характеристик Рівномірна - Квадратична")

#==============================================================================================
square_exponential, distribution_2 = square(n, exponential_distribution, error, "Динаміка Експоненційна - Квадратична")

plt.xlabel("гістограми законів розподілу Експоненційна - Квадратична")
plt.hist(exponential_distribution, bins=20, alpha=0.5, label='distribution')
plt.hist(distribution, bins=20, alpha=0.5, label='distribution_1')
plt.hist(square_exponential, bins=20, alpha=0.5, label='distribution_3')
plt.show()
stats(square_exponential)

assessment(n, distribution, square_exponential, distribution_2, uniform_distribution, "оцінка статистичних характеристик Експоненційна - Квадратична")

#==============================================================================================
normal_constant, distribution_2 = constant(n, const, error, uniform_distribution, "Динаміка розподілу Рівномірна - Статична")

plt.xlabel("гістограми законів розподілу Рівномірна - Статична")
plt.hist(uniform_distribution, bins=20, alpha=0.5, label='distribution')
plt.hist(distribution, bins=20, alpha=0.5, label='distribution_1')
plt.hist(normal_constant, bins=20, alpha=0.5, label='distribution_3')
plt.show()
stats(normal_constant)

assessment(n, distribution, normal_constant, distribution_2, uniform_distribution, "оцінка статистичних характеристик Рівномірна - Cтатична")

#==============================================================================================

exponential_constant, distribution_2  = constant(n, const, error, exponential_distribution, "Динаміка розподілу Експоненційна - Статична")

plt.xlabel("гістограми законів розподілу Експоненційна - Статична")
plt.hist(exponential_distribution, bins=20, alpha=0.5, label='distribution')
plt.hist(distribution, bins=20, alpha=0.5, label='distribution_1')
plt.hist(exponential_constant, bins=20, alpha=0.5, label='distribution_3')
plt.show()
stats(exponential_constant)

assessment(n, distribution, exponential_constant, distribution_2, uniform_distribution, "оцінка статистичних характеристик Експоненційна - Квадратична")