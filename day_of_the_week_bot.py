import tweepy
import requests
import os
from datetime import datetime
from decouple import config

DIAS = [
    'SEGUNDA-FEIRA',
    'TERÇA-FEIRA',
    'QUARTA-FEIRA',
    'QUINTA-FEIRA',
    'SEXTA-FEIRA',
    'SÁBADO',
    'DOMINGO'
]

def main():
    message = check_date()
    url = taking_photo(message)
    tweet_post(url, message)

def check_date():
    dia = datetime.today().weekday()
    dia_da_semana = DIAS[dia]
    print(dia_da_semana)
    return dia_da_semana

def twitter_api_keys():
    api_key = config('API_KEY')
    api_secret_key = config('API_SECRET_KEY')
    access_token = config('ACCESS_TOKEN')
    access_secret_token = config('ACCESS_SECRET_TOKEN')

    auth = tweepy.OAuthHandler(api_key, api_secret_key)
    auth.set_access_token(access_token, access_secret_token)
    api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

    try:
        api.verify_credentials()
        print("Authentication OK")
    except:
        print("Error during authentication")

    return api

def tweet_post(url, message):
    api = twitter_api_keys()

    filename = 'day.jpg'
    request = requests.get(url, stream=True)
    if request.status_code == 200:
        with open (filename, 'wb') as image:
            for chunk in request:
                image.write(chunk)

        api.update_with_media(filename, status=message)
        os.remove(filename)
    else:
        print('Unable to download image')

def taking_photo(dia_da_semana):
    if dia_da_semana == 'SEGUNDA-FEIRA':
        url = "https://bityli.com/vC522"
        return url

    elif dia_da_semana == 'TERÇA-FEIRA':
        url = "https://bityli.com/ANbzm"
        return url

    elif dia_da_semana == 'QUARTA-FEIRA':
        url = "encurtador.com.br/hmwCT"
        return url

    elif dia_da_semana == 'QUINTA-FEIRA':
        url = "encurtador.com.br/efrxN"
        return url

    elif dia_da_semana == 'SEXTA-FEIRA':
        url = "encurtador.com.br/drsO8"
        return url

    elif dia_da_semana == 'SÁBADO':
        url = "encurtador.com.br/guAJO"
        return url

    elif dia_da_semana == 'DOMINGO':
        url = "encurtador.com.br/jyM46"
        return url
    
    else:
        url = ""
        return url

# início da execução do programa
#-----------------------------------------------------
if __name__ == '__main__': # chamada da funcao principal
    main() # chamada da função main