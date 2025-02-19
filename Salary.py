#Загружаем библиотеку Pandas
import pandas as pd

#Создаем датафрейм и считываем в него датасет
df = pd.read_csv('dz.csv')

#Смотрим первые 5 записей
print(df.head())
#Смотрим последние 5 записей
print("\n", df.tail())
#Смотрим базовую информацию
print("\n", df.info())
#Смотрим общую статистику
print("\n", df.describe())

#Группируем по городу и рассчитываем среднюю зарплату в них
print("\n", df.groupby('City')['Salary'].mean())
