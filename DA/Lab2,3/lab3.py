import pandas as pd

srs = pd.read_csv('possum.csv', index_col=0)
print(srs.head())
#1. Виділити один зі стовпців (на вибір) з файлу як об’єкт Series, виділити з
#нього підмасив. Задати назви індексів цього об’єкту. Виділити підмасиви
#за допомогою прямої та непрямої індексацій.

tmp = srs['totlngth']
print(id(tmp))
print(id(srs['totlngth']))

tmp = srs.iloc[:, 4]
print(id(tmp))

tmp = srs.loc[:, 'totlngth']
print(id(tmp))

tmp = srs.iloc[1:5]
print(id(tmp))

tmp.index = ['a', 'b', 'c', 'd']
print(id(tmp))

print(id(tmp.loc[['a', 'd']]))

#2. До об’єкту DataFrame, в який записано вміст файлу, додати новий
#стовпець, що є результатом операцій над іншими стовпцями. Також
#продемонструвати додавання та видалення рядків, видалення стовпців.

srs['new'] = srs['totlngth'] * srs['age']
print(srs.head())

srs = srs.append(srs.loc[2])
print(srs)

srs = srs.drop(columns=['new'], index=[2])
print(srs)

#3. Встановити один зі стовпців індексом. Визначити основні статистичні
#характеристики та типи даних всіх стовпців. Змінити тип даних для
#одного з стовпців. Згрупувати дані за одним зі стовпців, застосувати
#кілька агрегуючих функцій, виділити підмасив за певними ознаками.

srs.set_index('site')

print(srs.dtypes)

print(srs.describe())

srs['totlngth'] = srs['totlngth'].astype('str')
print(srs.dtypes['totlngth'])

print(srs.groupby('site').agg({'chest':['mean', 'sum'], 'belly': 'std'}))

print(srs[srs['site'] == 5])

#4. Створити декілька власних об’єктів DataFrame за такою ж тематикою, що
#й файл. Наприклад, якщо тема файлу – жаби, можна створити об’єкти,
#що містять розміри жаб, вагу, стать, кількість особин в популяції і т.д.
#Використати описані в теоретичних відомостях параметри методів merge
#та concat для різних видів злиття та об’єднання даних цих об’єктів.

types = pd.DataFrame({'possum-par': range(5),'color':['red', 'yellow', 'green', 'black', 'grey']})
print(types)

possum = pd.DataFrame({'name': ['Petro', 'Fedir', 'Ivan', 'Stepan', 'Andriy'], 'type': [3, 2, 4, 0, 1]})
print(possum)

new_possum = pd.DataFrame({'name': ['Lesya'], 'type':[4]})
print(new_possum)

possum = pd.concat([possum, new_possum], axis=0)
print(possum)

possum.merge(types, left_on='type', right_on='possum-par')


