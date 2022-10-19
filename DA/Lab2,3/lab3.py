import pandas as pd
#1. Виділити один зі стовпців (на вибір) з файлу як об’єкт Series, виділити з
#нього підмасив. Задати назви індексів цього об’єкту. Виділити підмасиви
#за допомогою прямої та непрямої індексацій.
df = pd.read_csv('possum.csv', index_col=0)
print(df.head())

df_temp = df['totlngth']
print(id(df_temp))
print(id(df['totlngth']))

df_temp = df.iloc[:, 4]
print(id(df_temp))

df_temp = df.loc[:, 'totlngth']
print(id(df_temp))

df_temp = df.iloc[1:5]
print(id(df_temp))

df_temp.index = ['a', 'b', 'c', 'd']
print(df_temp)

print(df_temp.loc[['a', 'd']])
#2. До об’єкту DataFrame, в який записано вміст файлу, додати новий
#стовпець, що є результатом операцій над іншими стовпцями. Також
#продемонструвати додавання та видалення рядків, видалення стовпців.

df['new'] = df['totlngth'] * df['age']
print(df.head())

df = df.append(df.loc[2])
print(df.tail())

df = df.drop(columns=['new'], index=[2])
print(df)

#3. Встановити один зі стовпців індексом. Визначити основні статистичні
#характеристики та типи даних всіх стовпців. Змінити тип даних для
#одного з стовпців. Згрупувати дані за одним зі стовпців, застосувати
#кілька агрегуючих функцій, виділити підмасив за певними ознаками.

df.set_index('pres.abs')

print(df.dtypes)

print(df.describe())

df['totlngth'] = df['totlngth'].astype('str')
print(df.dtypes['totlngth'])

print(df.groupby('pres.abs').agg({'chest':['mean', 'sum'], 'belly': 'std'}))

print(df[df['pres.abs'] == 0])

#4. Створити декілька власних об’єктів DataFrame за такою ж тематикою, що
#й файл. Наприклад, якщо тема файлу – жаби, можна створити об’єкти,
#що містять розміри жаб, вагу, стать, кількість особин в популяції і т.д.
#Використати описані в теоретичних відомостях параметри методів merge
#та concat для різних видів злиття та об’єднання даних цих об’єктів.

