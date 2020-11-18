import requests
url = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_US.csv'
res = requests.get(url, allow_redirects=True)
with open('covid_data.csv','wb') as file:
    file.write(res.content)
# covid_data = pd.read_csv('covid_data.csv')