'''Takes a number of news articles, runs a sentiment analysis on them, and tweets about whether they are good or bad'''
import tweepy
import requests
import json
bbc = requests.get(url='https://newsapi.org/v1/articles?source=bbc-news&sortBy=top&apiKey=')
cnn = requests.get(url='https://newsapi.org/v1/articles?source=cnn&sortBy=top&apiKey=')
reuters = requests.get('https://newsapi.org/v1/articles?source=reuters&sortBy=top&apiKey=')
consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
i = 0
while i<=9:
     bbctitles = bbc.json()['articles'][i]['title']
     bbcdesc = bbc.json()['articles'][i]['description']
     bbcsentraw = requests.post("http://text-processing.com/api/sentiment/", data={'text': bbcdesc})
     bbcsent = bbcsentraw.json()
     bbclabel = bbcsent['label']
     if bbclabel == "pos":
         bbclabel = "Positive news: "
         api.update_status(bbclabel + " " + bbctitles)
         print ("Sent tweet about positive news")
     elif bbclabel == "neg":
         bbclabel = "Negative news: "
         api.update_status(bbclabel + " " + bbctitles)
         print ("Sent tweet about negative news")
     cnntitles = cnn.json()['articles'][i]['title']
     cnndesc = cnn.json()['articles'][i]['description']
     cnnsentraw = requests.post("http://text-processing.com/api/sentiment/", data={'text': cnndesc})
     cnnsent = cnnsentraw.json()
     cnnlabel = cnnsent['label']
     if cnnlabel == "pos":
         cnnlabel = "Positive news: "
         api.update_status(cnnlabel + " " + cnntitles)
         print ("Sent tweet about positive news")
     elif cnnlabel == "neg":
         cnnlabel = "Negative news: "
         api.update_status(cnnlabel + " " + cnntitles)
         print ("Sent tweet about negative news")
     reuterstitles = reuters.json()['articles'][i]['title']
     reutersdesc = reuters.json()['articles'][i]['description']
     reuterssentraw = requests.post("http://text-processing.com/api/sentiment/", data={'text': reutersdesc})
     reuterssent = reuterssentraw.json()
     reuterslabel = reuterssent['label']
     if reuterslabel == "pos":
         reuterslabel = "Positive news: "
         api.update_status(reuterslabel + " " + reuterstitles)
         print ("Sent tweet about positive news")
     elif reuterslabel == "neg":
         reuterslabel = "Negative news: "
         api.update_status(reuterslabel + " " + reuterstitles)
         print ("Sent tweet about negative news")
     i+=1
