from __future__ import absolute_import, print_function

from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

# Go to http://apps.twitter.com and create an app.
# The consumer key and secret will be generated for you after
consumer_key="UywPMW6g2rqR2OsvhJvk2Vhil"
consumer_secret="Wv2ogw7ZVTGyGBcmcDVgrlpSTkQTfMMgVMganwkVJmwKMJUHdP"

# After the step above, you will be redirected to your app's page.
# Create an access token under the the "Your access token" section
access_token="974180316-ms2unyAqqt9XEAhWKMBf5GyelV3wGp3J7p00aML8"
access_token_secret="sBF4tc4apqDZUuiNvLfcdqbdktIutzOpqf9ZoRmlYHtEI"

class StdOutListener(StreamListener):
    """ A listener handles tweets are the received from the stream.
    This is a basic listener that just prints received tweets to stdout.

    """
    def on_data(self, data):
        a = str(data)
        #print(a)
        f.write(a)
        f.write("\n")
##        firstIndex = a.index(',"text"')
##        firstIndex = firstIndex + 9
##        secondIndex = a.index(',"source"')
##        secondIndex = secondIndex - 1
##        print(i,": ",a[firstIndex:secondIndex])
        #i = i+1
        return True

    def on_error(self, status):
        print(status)

if __name__ == '__main__':
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    global f
    f = open('insurgent1.txt', 'w')
    global i
    i = 1
    
    stream = Stream(auth, l)
    try:
        stream.filter(track=['#insurgent'])
    except:
        f.close()
        stream.disconnect()
