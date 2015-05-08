#! /Users/sumesh/moviebuzz-api/flask/bin/python
from __future__ import absolute_import, print_function
from threading import Timer
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import sys
import os
import time

consumer_key="UywPMW6g2rqR2OsvhJvk2Vhil"
consumer_secret="Wv2ogw7ZVTGyGBcmcDVgrlpSTkQTfMMgVMganwkVJmwKMJUHdP"
access_token="974180316-ms2unyAqqt9XEAhWKMBf5GyelV3wGp3J7p00aML8"
access_token_secret="sBF4tc4apqDZUuiNvLfcdqbdktIutzOpqf9ZoRmlYHtEI"

class Watchdog:
    def __init__(self, timeout, userHandler=None):
        self.timeout = timeout
        self.handler = userHandler if userHandler is not None else self.defaultHandler
        self.timer = Timer(self.timeout, self.handler)
        self.timer.start()
    def reset(self):
        self.timer.cancel()
        self.timer = Timer(self.timeout, self.handler)
        self.timer.start()
    def stop(self):
        self.timer.cancel()
    def defaultHandler(self):
        raise self

class StdOutListener(StreamListener):
    def on_data(self, data):
        a = str(data)
        f.write(a)
        f.write("\n")
        return True
    def on_error(self, status):
        print(status)

def timeoutHandler():
    f.close()
    stream.disconnect()
    time.sleep(50)
    #exit program
    os._exit(0)
            
if __name__ == '__main__':
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    global f
    timestr = time.strftime("%Y%m%d-%H%M%S")
    f = open('/Users/sumesh/moviebuzz-api/tweets/'+timestr+'_tweets.txt', 'a')
    global stream
    stream = Stream(auth, l)
    try:
        watchdog = Watchdog(300,timeoutHandler)
        stream.filter(track=["The Longest Ride","thelongestride","longestride","Ex Machina","ExMachina","Desert Dancer","DesertDancer","Clouds of Sils Maria","CloudsOfSilsMaria","Kill Me Three Times","KillMeThreeTimes","Lost River","LostRiver","While We're Young","selma","Danny Collins","DannyCollins","The Second Best Exotic Marigold Hotel","Fifty Shades of Grey","FiftyShades","Into the Woods","IntotheWoods","The Imitation Game","TheImitationGame","Seventh Son","SeventhSon","The SpongeBob Movie: Sponge Out of Water","SpongeBobMovie","Paddington","American Sniper","AmericanSniper","Night at the Museum: Secret of the Tomb",'cinderella','furious7','the gunman','thegunman','do you believe','run all night','kingsman','insurgent','insurgentmovie','chappie','chappiemovie','chappiethemovie','focus movie','gethard','home movie','homemovie','DreamWorksHOME','woman in gold','itfollows','itfollowsfilm','get hard','gethard'],languages=['en'])
    except:
        f.close()
        stream.disconnect()
        sys.exit(0)