#Загружаем библиотеку Pandas
import pandas as pd

#Создаем датафрейм и считываем в него датасет
df = pd.read_csv('English Premier League.csv')

df.info()

#Вывод отдельных столбцов
#print(df['HomeTeam'])
#print(df[['HomeTeam', 'AwayTeam', 'Result']])

#Вывод отдельных строк и столбцов
#print(df.loc[100])
#print(df.loc[100:105, 'Date':'AwayTeam'])

#Вывод строк по условию
#print(df[df['Result']=='D'])

#Добавление столбцов
df['Test'] = [new for new in range(12790)]
df['TestX'] = [new for new in range(12790)]
# print(df)

# #Удаление столбцов
dfx = df.drop('Test', axis=1, inplace=False)
# print(df,dfx)

# #Удаление строк
dfx.drop(12788, axis=0, inplace=True)
# print(dfx)

#Замена NaN на значение
#df.fillna(0, inplace=True)
#print(df)

#Удаление строк с NaN
#df.dropna(inplace=True)
#print(df)

#Использование группировок
group = df.groupby('HomeTeam')['HomeGoals'].mean()
print(group)

#Сохранение датафрейма в файл
dfx.to_csv('dfx.csv', index=False)
