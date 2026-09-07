from flask import Flask, render_template, request
import json
import urllib.parse
import urllib.request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def details():
    if request.method == 'GET':
        return render_template('index1.html')
    
    location = request.form.get('location', '').strip()
    if not location:
        return render_template('index1.html', error='Give the correct location.')
    
    try:
        q = urllib.parse.quote(location)

        url = f"https://photon.komoot.io/api/?q={q}&limit=1"
        req = urllib.request.Request(url, headers={"User-Agent": "FlaskGeocoder/1.0"})

        source = urllib.request.urlopen(req).read()
        responseData = json.loads(source)

        features = responseData.get('features', [])
        if not features:
            return render_template('index1.html', error='Location not found.')

        lon, lat = features[0]['geometry']['coordinates']
