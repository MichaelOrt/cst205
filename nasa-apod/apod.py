from flask import Flask, render_template
import requests, json
from flask_bootstrap import Bootstrap

app = Flask(__name__)
bootstrap = Bootstrap(app)

# better to replace this with your own key from https://api.nasa.gov/
my_key = 'DEMO_KEY'

payload = {
  'api_key': 'USE YOUR KEY HERE',
  'start_date': '2018-10-15',
  'end_date': '2018-10-15'
}

endpoint = 'https://api.nasa.gov/planetary/apod'

@app.route('/')
def main():
    try:
        r = requests.get(endpoint, params=payload)
        data = r.json()
    except:
        print('please try again')
    return render_template('home.html', data=data)
