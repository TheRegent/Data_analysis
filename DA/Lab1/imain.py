import random
from math import *


def combination(K, N):
    return (factorial(N)) / (factorial(N - K) * (factorial(K)))


m = 10000
n = 0
while m > 0:
    m -= 1
    attempts = []
    counter = 0
    for i in range(6):
        attempts.append(random.randint(1, 6))

    for j in attempts:
        if j == 6:
            counter += 1
    #print(attempts)
    if counter >= 2:
        n += 1

P_not_A = combination(0, 6) * pow((1 / 6), 0) * pow((5 / 6), 6) + combination(1, 6) * (1 / 6) * pow((5 / 6), 5)
P_A = 1 - P_not_A

print(f"-----Practical method----- \n n: {float(n)} \n m: {float(10000)} \n result: {n / 10000}")

print(f"\n -----Theoretical method----- \n result: {round(P_A, 4)}")

print(f"\n -----Error percent----- \n Error: {abs((n / 10000)-P_A)}")