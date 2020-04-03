import pandas as pd

df = pd.read_csv('time_series_covid_19_recovered.csv', usecols=['Country/Region', '4/1/20'])

print(df)
































































# import numpy as np
# import pandas as pd

# def header(msg):
#     print(msg)

# header("1.load hard-coded data int df")
# filename = 'time_series_covid_19_recovered.csv'
# df = pd.read_csv(filename, usecols=['Country/Region', '4/1/20'], dtype={'4/1/20':str})
# print(df.tail(5))
# print(df.columns.tolist())
# print(df.columns.tolist())
# proviceState = df['Province/State'].values.tolist()
# proviceState.append('Morocco')

# print(proviceState)

#display the first rows in the table
# print(df.head(3))
#display the last rows in the table
# print(df.tail(3))
#number of rows and column
# print(df.shape)
#index, Datatype, and Memory information
# print(df.info())
#view unaue values and counts
# print(df.apply(pd.Series.value_counts))


