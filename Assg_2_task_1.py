
import pandas as pd
weather_file= '/Users/sahilbhat/Downloads/USweather_history.txt'
weather_data= pd.read_csv(weather_file)


df_weather= pd.DataFrame(data=weather_data)


max_temp= max(df_weather['actual_max_temp'])
print('Maximum temperature is: {0}'.format(max_temp))


min_temp= min(df_weather['actual_min_temp'])
print('Minimum temperature is: {0}'.format(min_temp))

maxa=df_weather[df_weather['actual_max_temp']==max_temp]
df_maxa=pd.DataFrame(maxa)
print(maxa['date'])
mina=df_weather[df_weather['actual_min_temp']==min_temp]
df_mina=pd.DataFrame(mina)
a=(mina['date'].values.tolist())
print(a[0])

max_temperature= df_weather

