#! flask/bin/python
from flask import Flask

app = Flask(__name__,static_url_path='')

@app.route('/')
def index():
    return app.send_static_file('index.html')
    #return "Hello, World!"

@app.route('/moviedetails/')
def movie():
    return '[{"title":"The Pianist"}]'

if __name__ == '__main__':
    app.run(debug=True)
