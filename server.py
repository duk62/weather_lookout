from flask import Flask, render_template
from flask import request
from weather import get_current_weather
from waitress import serve
from pprint import pprint


app = Flask(__name__)
app.debug = True


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/weather')
def current_weather():

    city = request.args.get('city')

    if not bool(city.strip()):
        city = "Honolulu"

    current_weather_data = get_current_weather(city)

    if not current_weather_data['cod'] == 200:
        return render_template('city-not-found.html')

    return render_template(

        "weather.html",
        title=current_weather_data["name"],
        status=current_weather_data["weather"][0]["description"].capitalize(),
        temp=f"{current_weather_data['main']['temp']:.1f}",
        humidity=current_weather_data['main']['humidity'],
        feels_like=f"{current_weather_data['main']['feels_like']:.1f}"

    )


if __name__ == "__main__":

    serve(app, host="0.0.0.0", port=8000)
