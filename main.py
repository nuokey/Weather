from flask import Flask
from flask import render_template
from flask import request

import requests

app = Flask(__name__)






@app.route("/")
def index():
    city = request.args.get('city')

    city_req = requests.get(f"http://api.openweathermap.org/geo/1.0/direct?q={city}&limit=1&appid=b7c20233e51a871a2cd9e4f3fbdb0ead")
    city_data = city_req.json()

    # print(city_data)

    lat = city_data[0]['lat']
    lon = city_data[0]['lon']

    req = requests.get(f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid=b7c20233e51a871a2cd9e4f3fbdb0ead")

    data = req.json()
    print(data)

    weather = data["weather"][0]["main"] + " (" + data["weather"][0]["description"] + ")"
    temperature = int(data["main"]["feels_like"] - 273)
    wind = data["wind"]["speed"]
    visibility = data["visibility"]

    return render_template("index.html", city=city, weather=weather, temperature=temperature, wind=wind, visibility=visibility)

app.run()