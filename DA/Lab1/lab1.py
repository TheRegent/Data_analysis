import numpy as np
import pandas as pd


class Lab1():
    def __init__(self, gener):
        self.gener = gener

    def array_generate(self):
        # 1. Generates random and non-random arrays in various ways specified in the theoretical information.

        print("-----------------------------Перше завдання-----------------------------\n")
        do_dict = {"array" : (np.array([1, 2, 3, 4, 5, 6, 7, 8, 9], dtype=float)),
                   "ranged" : (np.arange(1,34,3)),
                   "integers" : (np.ones(11, dtype=int)),
                   "zeros" : (np.zeros((3,5), dtype=float)),
                   "linspace" : (np.linspace(0, 20, 5)),
                   "random" : (np.random.random((5, 4))),
                   "randint" : (np.random.randint(0, 100, (5, 5))),
                   "empty" : (np.empty(5))}
        keys = do_dict.keys()
        if self.gener in keys:
            print(do_dict[self.gener])
        else:
            print("Помилка! Перевірте правильність введенняю команди.")


        # 2. Demonstrates accessing array elements by index,
        # including negative selection of subarrays of both one-dimensional and multidimensional arrays.

        print("\n-----------------------------Друге завдання-----------------------------\n")
        g = do_dict[self.gener]
        if self.gener == "zeros" or self.gener == "random" or self.gener == "randint":
            index1 = int(input("Введіть індекс 1 для звернення до масиву:"))
            index2 = int(input("Введіть індекс 2 для звернення до масиву:"))
            print(g[index1, index2])
        else:
            index = int(input("Введіть індекс для звернення до масиву:"))
            print(g[index])

        start = int(input("Введіть початок зрізу:"))
        end = int(input("Введіть кінець зрізу:"))
        step = int(input("Введіть крок:"))
        print(g[start:end:step])


    # 3. Demonstrates basic arithmetic operations on arrays, as well as the work of reduce, accumulate, outer methods.

        print("\n-----------------------------Третє завдання-----------------------------\n")
        operation = input("Введіть знак арифметичної операції(+, -, *, /, **, %, reduce, accumulate, outer):")
        num = int(input("Введіть число з яким будете працювати:"))

        operators = ["+", "-", "*", "/", "**", "%", "reduce", "accumulate", "outer"]
        if operation in operators:
            print({"+" : lambda g, num: g + num,
                   "-" : lambda g, num: g - num,
                   "*" : lambda g, num: g * num,
                   "/" : lambda g, num: g / num,
                   "**" : lambda g, num: g ** num,
                   "%" : lambda g, num: g % num,
                   "reduce" : lambda g, num: np.add.reduce(g),
                   "accumulate" : lambda g, num: np.add.accumulate(g),
                   "outer" : lambda g, num: np.multiply.outer(g, g)}[operation](g, num))
        else:
            print("Помилка! Перевірте правильність введенняю знаку.")


    # 4. Calculates statistical characteristics, namely, minimum and maximum value, sample mean,
    # variance, standard deviation, median and 25th and 75th percentiles, petal width (petal_width)
    # values from iris flower data set (iris.csv).

    def statistic(self):
        print("\n-----------------------------Четверте завдання-----------------------------\n")
        data = pd.read_csv(r"C:\Users\fidde\Downloads\iris.csv")
        petal = np.array(data['petal_width'])
        print(f"Мінімальне значення: {petal.min()}\nМаксимальне значення: {petal.max()}\nCереднє значення: {petal.mean()}\nДисперсія: {petal.var()}\nСередньоквадратичне відхилення: {petal.std()}\nМедіану: {np.median(petal)}\n25 Персентилі: {np.percentile(petal, 25)}\n75 Персентилі: {np.percentile(petal, 75)}")


numeratePy = input("Введіть назву дії(array, ranged, integers, zeros, linspace, random, randint, empty):")
a = Lab1(numeratePy).array_generate()
b = Lab1(numeratePy).statistic()


