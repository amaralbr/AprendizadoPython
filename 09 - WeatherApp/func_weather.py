import requests
import json
from datetime import date
import urllib.parse
import pprint

accuWeatherAPIKey = 'Fi4y5THwW6uKI7ETGbrK8VztL3h3vdt1'
mapBoxAPIKey = 'pk.eyJ1IjoiYW1hcmFsYnIiLCJhIjoiY2s4dDZ3cHVzMDN1NTNpcWtybmxob3dkaCJ9.10FnPBqG6sV0grrmMDzMUw'
daysOfWeek = ['Domingo', 'Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábado']



def setWeather(lat, long):
    try:
        local = getLocalCode(lat, long)
        climate = getWeatherNow(local['localCode'], local['localName'])
        print('-------------------------------------------------')
        print('Clima atual em: ' + climate['localName'])
        print(climate['textClimate'])
        print('Temperatura: ' + str(climate['temperature']) + '\xb0' + 'C')
    except:
        print('Erro ao obter o clima atual.')

    print('')    
    question1 = input('Deseja ver a previsão para os próximos dias (s/n)? ').lower()
    if question1 == 's':
        print('-------------------------------------------------')
        print('\nCLima para os próximos dias:\n')
        try:
            weather5days = getWeather5Days(local['localCode'])
            for day in weather5days:
                print(day['dayWeek'])
                print('Mínima: '+ str(day['minimum']) + '\xb0' + 'C')
                print('Máxima: '+ str(day['maximum']) + '\xb0' + 'C')
                print(day['iconPhrase'])
                print('-------------------------------------------------')
        except:
            print('Erro ao obter a previsão para os próximos dias.')



def searchNewLocation(newLocal):
    _local = urllib.parse.quote(newLocal)
    newLocation = 'https://api.mapbox.com/geocoding/v5/mapbox.places/'+ _local +'.json?access_token='+ mapBoxAPIKey
    r = requests.get(newLocation)
    if (r.status_code != 200):
        print('Não foi possível encontrar nova localidade.')
        return None
    else:
        try:
            newLocalWeather = json.loads(r.text)
            coordinater = {}
            coordinater['long'] = str(newLocalWeather['features'][0]['geometry']['coordinates'][0])
            coordinater['lat'] = str(newLocalWeather['features'][0]['geometry']['coordinates'][1])
            return coordinater
        except:
            return print('Erro na pesquisa do local.')
            return None



def getCoordinater():
    r = requests.get('http://www.geoplugin.net/json.gp')
    if (r.status_code != 200):
        print('Não foi possível obter a localização.')
        return None
    else:
        try:
            localization = json.loads(r.text)
            coordinater = {}
            coordinater['lat'] = localization['geoplugin_latitude']
            coordinater['long'] = localization['geoplugin_longitude']
            return coordinater
        except:
            return None

def getLocalCode(lat, long):
    locationAPIUrl = 'http://dataservice.accuweather.com/locations/v1/cities/geoposition/search?apikey='+ accuWeatherAPIKey +'&q='+ lat +'%2C%20'+ long +'&language=pt-br'
    r = requests.get(locationAPIUrl)
    if (r.status_code != 200):
        print('Não foi possível obter o código do local.')
        return None
    else:
        try:
            locationResponse = json.loads(r.text)
            infoLocal = {}
            infoLocal['localName'] = locationResponse['LocalizedName'] +', '+ locationResponse['AdministrativeArea']['LocalizedName'] +', '+ locationResponse['Country']['LocalizedName']
            infoLocal['localCode'] = locationResponse['Key']
            return infoLocal
        except:
            return None

def getWeatherNow(localCode, localName):
    CurrentConditionsAPIUrl = 'http://dataservice.accuweather.com/currentconditions/v1/'+ localCode +'?apikey='+ accuWeatherAPIKey +'&language=pt-br'
    r = requests.get(CurrentConditionsAPIUrl)
    if (r.status_code != 200):
        print('Não foi possível obter o clima atual.')
        return None
    else:
        try:
            CurrentConditionsResponse = json.loads(r.text)
            infoClimate = {}
            infoClimate['textClimate'] = CurrentConditionsResponse[0]['WeatherText']
            infoClimate['temperature'] = CurrentConditionsResponse[0]['Temperature']['Metric']['Value']
            infoClimate['localName'] = localName
            return infoClimate
        except:
            return None

def getWeatherNextDays(localCode):
    forecastsAPIUrl = 'http://dataservice.accuweather.com/forecasts/v1/daily/5day/'+ localCode +'?apikey='+ accuWeatherAPIKey +'&language=pt.br'
    r = requests.get(forecastsAPIUrl)
    if (r.status_code != 200):
        print('Não foi possível obter a previsão para os próximos dias.')
        return None
    else:
        forecastsAPIUrl = json.loads(r.text)
        print(forecastsAPIUrl)

def getWeather5Days(localCode):
    forecastsAPIUrl = 'http://dataservice.accuweather.com/forecasts/v1/daily/5day/'+ localCode +'?apikey='+ accuWeatherAPIKey +'&language=pt-br&metric=true'
    r = requests.get(forecastsAPIUrl)
    if (r.status_code != 200):
        print('Não foi possível obter a previsão para os próximos dias.')
    else:
        try:
            forecastsAPIUrl = json.loads(r.text)
            info5days = []
            for day in forecastsAPIUrl['DailyForecasts']:
                climateDay = {}
                day_week = int(date.fromtimestamp(day['EpochDate']).strftime('%w'))
                climateDay['dayWeek'] = daysOfWeek[day_week]
                climateDay['minimum'] = day['Temperature']['Minimum']['Value']
                climateDay['maximum'] = day['Temperature']['Maximum']['Value']
                climateDay['iconPhrase'] = day['Day']['IconPhrase']
                info5days.append(climateDay)
            return info5days
        except:
            return None