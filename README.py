# Twitter_for_SMs_computer.py
import sys, os, time
import tweepy
keys = dict(
consumer_key='goaPYXDhXdPd4E845lVarMTQP',
consumer_secret='1ZUkEalRYupKLHhvwLpFIrvuT0AT7TRnUbCzQWxIzqBN19WcMf',
access_token='3307061003-rMfNBj0QlUVMQG1Hcob3Xpa0UtiEu0q81uICpbD', 
access_token_secret='nueq05KsarX1MswLg7HTiQQQxyqN76sGeuw20eUp2xEkQ'
)

user = "@WeStanWally"

auth = tweepy.OAuthHandler(keys['goaPYXDhXdPd4E845lVarMTQP'], keys['1ZUkEalRYupKLHhvwLpFIrvuT0AT7TRnUbCzQWxIzqBN19WcMf'])
auth.set_access_token(keys['3307061003-rMfNBj0QlUVMQG1Hcob3Xpa0UtiEu0q81uICpbD'], keys['nueq05KsarX1MswLg7HTiQQQxyqN76sGeuw20eUp2xEkQ'])
api = tweepy.API(auth)

def tweet():
	message=input("tweet:You thought « twitter for iPhone » was cool ? Get on my level I’m currently trying to delete Mark's name of all the projects groups ")
	api.update_status(message)
	time.sleep(1000)
if __name__ == "__main__":
	while 1:
		tweet()
   
