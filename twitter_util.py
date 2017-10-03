import tweepy
import datetime
import time
import os
def main(): 
    now = datetime.datetime.now()
    consumer_key = ''
    consumer_secret = ''
    access_token = ''
    access_token_secret = ''

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    api = tweepy.API(auth)
    api_id = api.me().id

    latest = api.user_timeline(id = api_id, count = 1)[0]
    text = (latest.text)
    monthnumber = now.month
    monthword = time.strftime('%B', time.struct_time((0, monthnumber, 0,)+(0,)*6))
    niceday = str(now.day)
    niceyear = str(now.year)
    nicehour = now.hour
    niceminute = now.minute
    if (nicehour > 12):
        amorpm = "PM"
        nicehour+=-12
        nicesthour = "0" + str(nicehour)
    elif (nicehour < 12):
        amorpm = "AM"
        nicesthour = "0" + str(nicehour)
    if (niceminute < 10):
        nicestminute = "0" + str(niceminute)
    boilertext = "This tweet is an API link." + " " + monthword + " " + niceday + ", " + niceyear + " at " + nicesthour + ":" + nicestminute + amorpm
    print text
    print boilertext
    if (boilertext == text):
        os.system("sudo apt-get update && sudo apt-get autoremove")
        os.system("sudo apt-get upgrade && sudo apt-get autoclean")
        print "Trigger received"
    else: 
        print "No trigger yet"
while True:
    main()
    time.sleep(5)
