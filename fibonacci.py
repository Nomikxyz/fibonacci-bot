import tweepy
import time
import datetime

numbers = 500
fib = [1,1]

consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)


i=2
counter = 0
while i < numbers:
    fib.append(fib[-2] + fib[-1])
    i += 1

for n in fib:
    api.update_status("Number " +  '{0:,}'.format(counter) + " in sequence: "+ '{0:,}\n'.format(n))
    currenttime = datetime.datetime.now()
    print ("Sent Tweet at ")
    print (datetime.datetime.now())
    counter+=1
    time.sleep(30)
