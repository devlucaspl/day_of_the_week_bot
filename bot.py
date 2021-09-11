import tweepy
import requests
import os
import time
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
    api = twitter_api_keys()
    while True:
        message = check_date()
        url = taking_photo(message)
        tweet_post(api, url, message)
        time.sleep(86400)

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

def tweet_post(api, url, message):

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
        url = "https://res.cloudinary.com/dnq6f7apl/image/upload/v1627068614/bots/day_of_the_week/segunda_lvltvh.jpg"
        return url

    elif dia_da_semana == 'TERÇA-FEIRA':
        url = "https://res.cloudinary.com/dnq6f7apl/image/upload/v1627068615/bots/day_of_the_week/terca_u5ymkt.jpg"
        return url

    elif dia_da_semana == 'QUARTA-FEIRA':
        url = "https://res.cloudinary.com/dnq6f7apl/image/upload/v1627068614/bots/day_of_the_week/quarta_w5npjs.jpg"
        return url

    elif dia_da_semana == 'QUINTA-FEIRA':
        url = "https://res.cloudinary.com/dnq6f7apl/image/upload/v1627068614/bots/day_of_the_week/quinta_byfn1l.jpg"
        return url

    elif dia_da_semana == 'SEXTA-FEIRA':
        url = "https://res.cloudinary.com/dnq6f7apl/image/upload/v1627068615/bots/day_of_the_week/sexta_buanxo.jpg"
        return url

    elif dia_da_semana == 'SÁBADO':
        url = "https://res.cloudinary.com/dnq6f7apl/image/upload/v1627068615/bots/day_of_the_week/sabado_vraoir.jpg"
        return url

    elif dia_da_semana == 'DOMINGO':
        url = "https://res.cloudinary.com/dnq6f7apl/image/upload/v1627068615/bots/day_of_the_week/domingo_fvbx7k.jpg"
        return url
    
    else:
        url = ""
        return url    
    
# início da execução do programa
#-----------------------------------------------------
if __name__ == '__main__': # chamada da funcao principal
    main() # chamada da função main