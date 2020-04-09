import pandas as pd

df = pd.read_csv('time_series_covid_19_recovered.csv', usecols=['Country/Region', '4/1/20'])

print(df)
