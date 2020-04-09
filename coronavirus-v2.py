import pandas as pd

#selecting the first 5 rows
df = pd.read_csv('time_series_covid_19_recovered.csv')
# print(df.head(3))
















# Data types trick
# print(df.dtypes.value_counts())
















# select a specific columns
# print(df.select_dtypes(include=['object', 'float64']))

























#copy dataframe

dfCopy = df.copy()
print('Befor making changes')
print(df['4/1/20'].head(3))


dfCopy['4/1/20'] = dfCopy['4/1/20'] + 1

print('print dfCopy -- after making changes')
print(dfCopy['4/1/20'].head(3))

print('After copying --- df after making changes')
print(df['4/1/20'].head(3))


















# Data types trick

# print(df.dtypes.value_counts())
# print(df.select_dtypes(include=['float64', 'int64']))


#copy dataframe

# dfCopy = df
# dfCopy['4/1/20'] = dfCopy['4/1/20'] + 1
# print dfCopy
# print('print dfCopy')
# print(dfCopy['4/1/20'].head(3))
# print df
# print('print df')
# print(df['4/1/20'].head(3))






















