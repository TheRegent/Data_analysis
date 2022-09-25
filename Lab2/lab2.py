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
    print(f"Оскільки гіпотеза одностороння використовуюємо p_value/2: {(p_value_var/2)}")
    if p_value_var/2 > 0.05:
        print("Нульову гіпотезу відхилено!")
    else:
        print("Нульову гіпотезу не відхилено!")

data = pd.read_csv("possum.csv")
eye_size = np.array(data['eye'])

#   1. Знайти розмір, який не перевищують очі 25% опосумів.[eye]
print(f"Розмір, який не перевищують очі 25% опосумів: {np.percentile(eye_size, 75)}")

#   2. Перевірити чи нормально розподілена довжина тіла.[totlngth]
lenght = np.array(data['totlngth'])
normality_check(lenght)

#   3. Чи є зв’язок між довжиною тіла і віком опосума?[totlngth/age]
age = np.array(data['age'])
pearson = sc.pearsonr(lenght, age)
spearman = sc.spearmanr(lenght, age)
kendalltau = sc.kendalltau(lenght, age)

correlation = np.mean([pearson[0], spearman[0], kendalltau[0]])
pValue = np.mean([pearson[1], spearman[1], kendalltau[1]])

print(f"\nКоефіцієнт кореляції: {correlation}")
print(f"P-коефіцієнт кореляції: {pValue}\nТому скоріш за все кореляції немає")

#   4. Чи відрізняється загальна довжина тіла опосумів Вікторії
#   та інших провінцій? (за допомогою статистичних гіпотез)[totlngth(Vic/other)]

# H0: Довжина тіла опосумів Вікторії <= інших штатів
# H1: Довжина тіла опосумів Вікторії > інших штатів

victoria = data[data['Pop'] == 'Vic']
other = data[data['Pop'] == 'other']

print("\n----------------------\nПеревірка на нормальний розподіл Вікторії")
normality_check(victoria['totlngth'])
print("\n----------------------\nПеревірка на нормальний розподіл інших провінцій")
normality_check(other['totlngth'])
print("\n----------------------\nПеревірка на однаковість дисперсій")
variance_homogeneity_check(victoria['totlngth'], other['totlngth'])
print("\n----------------------\nПеревірка гіпотез на правдивість")
hypothesis_check(victoria['totlngth'], other['totlngth'])
print(f"\nПеревірка ціх значеть середнім арифметичним:\nУ провінції Вікторія: {np.mean(victoria['totlngth'])} \nУ інших провінціях: {np.mean(other['totlngth'])}\nВірно!Все сходиться")

