#Autor Alexandre P. Teixeira

#use o comando abaixo para instalar a lib
#pip3 install tweepy
import tweepy

#você obtém os dados abaixo através do link: https://developer.twitter.com 
consumer_key = ""
consumer_secret = ""

def autentica_app():
    try:
        auth_app = tweepy.AppAuthHandler(consumer_key, consumer_secret)
        return tweepy.API(auth_app)
    except Exception as e: 
        print("Ocorreu um erro ao conectar a API do Twitter, verifique sua consumer_key e consumer_secret")
        return None

def executa_captura(termo):
    app = autentica_app()
    if app:
        for resultados in tweepy.Cursor(app.search, q=termo, count=100, tweet_mode='extended').pages():
            for tweet in resultados:
                #O objeto tweet possui diversas informações sobre a mensagem, como a data, autor, quantidade de seguidores, etc
                print("-" * 50)
                print("Autor: " + tweet.author.screen_name + " | Tweet: " + tweet.full_text)

def inicia():
    print('Qual hashtag você quer capturar? (Ex: #python)')
    termo = input()
    executa_captura(termo)

inicia()

