import pandas as pd
import numpy as np
import scipy.stats as sc


def normality_check(arg):
    test_stat_var, p_value_var = sc.shapiro(arg)
    print(f"\nP-значення для перевірки гіпотези: {p_value_var}")
    if p_value_var > 0.05:
        print("Вибірка розподілена за НОРМАЛЬНИМ законом розподілом!")
    else:
        print("Вибірка розподілена НЕ за нормальним законом розподілом!")

def variance_homogeneity_check(groupA, groupB):
    test_stat_var, p_value_var= sc.levene(groupA,groupB)
    print(f"\nP-значення для перевірки гіпотези: {p_value_var}")
    if p_value_var > 0.05:
        print("Дисперсія вибірок однакова!")
    else:
        print("Дисперсія вибірок не однакова!")

def hypothesis_check(groupA, groupB):
    test_stat_var, p_value_var = sc.ttest_ind(groupA, groupB)
    print(f"P-значеннядля перевірки гіпотези: {(p_value_var)}")
    if p_value_var > 0.05:
        print("Нульову гіпотезу НЕ відхилено!")
    else:
        print("Нульову гіпотезу відхилено!")

data = pd.read_csv("possum.csv")
eye_size = np.array(data['eye'])

#   1. Find the size that does not exceed the eyes of 25% of opossums. [eye]
print(f"Розмір, який не перевищують очі 25% опосумів: {np.percentile(eye_size, 25)}")

#   2. Check whether body length is normally distributed.[totlngth]
lenght = np.array(data['totlngth'])
normality_check(lenght)

#   3. Is there a relationship between body length and opossum age?[totlngth/age]
age = np.array(data['age'])
correlation, pValue = sc.pearsonr(lenght, age)

print(f"\nКоефіцієнт кореляції: {correlation}")
print(f"P-значення кореляції: {pValue}\nТому скоріш за все кореляції немає")

#   4. Is there a difference in total body length between opossums in Victoria
#   and other provinces? (using statistical hypotheses)[totlngth(Vic/other)]

# H0: There is no statistically significant difference between the lengths of the bodies of the provinces
# H1: A statistically significant difference between the lengths of the bodies of the provinces is recognized

victoria = data[data['Pop'] == 'Vic']
other = data[data['Pop'] == 'other']

print("\n----------------------\nПеревірка на нормальний розподіл Вікторії:")
normality_check(victoria['totlngth'])
print("\n----------------------\nПеревірка на нормальний розподіл інших провінцій:")
normality_check(other['totlngth'])
print("\n----------------------\nПеревірка на однаковість дисперсій:")
variance_homogeneity_check(victoria['totlngth'], other['totlngth'])
print("\n----------------------\nПеревірка гіпотез на правдивість:")
hypothesis_check(victoria['totlngth'], other['totlngth'])
print(f"\nПеревірка ціх значеть середнім арифметичним:\nУ провінції Вікторія: {np.mean(victoria['totlngth'])} \nУ інших провінціях: {np.mean(other['totlngth'])}\nВірно!Все сходиться")

