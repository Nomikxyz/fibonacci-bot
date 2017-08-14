'''If you're like me and you can't use the Alexa API because of all that AWS stuff, use this. 
Register your Echo with IFTTT and create an applet that posts the message "This is an API link" followed by
the time it was triggered to Twitter, preferably on an account that you don't use very much. Register some
API keys with Twitter and paste them in below. When all is ready, run the script, and it will check Twitter
for the indicator message every minute. If it does find the message, it will do whatever action you want it
to perform (in this case just printing out some text).'''

import tweepy
import datetime
import time
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
    print monthnumber
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
        print("Trigger received.")
    else: 
        print("No trigger detected")
while True:
    main()      
    time.sleep(5)
