#! flask/bin/python
from flask import Flask
from flask import request
from flask import jsonify
import sys
import anydbm
import re

try:
    import imdb
except ImportError:
    print 'You need to install the IMDbPY'
    sys.exit(1)

app = Flask(__name__,static_url_path='')

@app.route('/')
def index():
    return app.send_static_file('index.html')

@app.route('/barchart/')
def barchart():
    return app.send_static_file('barchart.html')

@app.route('/moviedetails/')
def movie():
    movie_name = request.args.get('movie_name')
    i = imdb.IMDb('sql',uri='mysql://sumesh:future123@localhost/imdb')
    #in_encoding = sys.stdin.encoding or sys.getdefaultencoding()
    #out_encoding = sys.stdout.encoding or sys.getdefaultencoding()
    #movie_name = unicode(movie_name, in_encoding, 'replace')
    try:
    # Do the search, and get the results (a list of Movie objects).
        results = i.search_movie(str(movie_name))
    except imdb.IMDbError, e:
        print "Probably you're not connected to Internet.  Complete error report:"
        print e
        #sys.exit(3)
        
    if not results:
        print 'No matches for "%s", sorry.' % movie_name
        #sys.exit(0)
    
    #fetch the remaining data    
    movie = results[0]
    print movie
    i.update(movie)

    #collect tweet information 
    input_file_name = './twitterdata.txt'
    f1 = open(input_file_name,'r')
    total_tweets = 0
    positive_tweets = 0
    negative_tweets = 0
    for line in f1:
        array = re.split(r'\t+', line)
        if(movie_name == array[0]):
            total_tweets = array[1]
            positive_tweets = array[2]
            negative_tweets = array[3]
            break
    f1.close()

    return jsonify({'Languages':movie.get('languages'),
                    'Runtime':movie.get('runtime'),
                    'Genres':movie.get('genres'),
                    'Cast': [cast['name'] for cast in movie.get('cast')][:2],
                    'Votes':movie.get('votes'),
                    'Rating':movie.get('rating'),
                    'Director':[{'dirname':dirname['name']} for dirname in movie.get('director')],
                    'Title':movie.get('title'),
                    'Tweets':total_tweets,
                    'Positive_Tweets':positive_tweets,
                    'Negative_Tweets':negative_tweets
                    #'Budget':movie.get('budget'),
                    #'Countries':movie.get('countries'),
                    })
    #return '[{"title":"Interstellar"}]'

if __name__ == '__main__':
    app.run(debug=True)
