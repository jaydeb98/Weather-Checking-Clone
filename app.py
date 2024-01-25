from flask import Flask, render_template, request
import requests
import os

app = Flask(__name__, template_folder='Templates')
print("Absolute template path:", os.path.abspath("templates"))

# API Key
api_key = '70dcd7f9dac74b293d8109aa7bb0b935'

@app.route('/')
def show_weather_template():
    return render_template('index.html')

@app.route('/weatherapp', methods=['POST','GET'])
def get_weather_data():
    city = request.form['city']

    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'

    response = requests.get(url)
    data = response.json()

    if response.status_code == 200:
        # Extract relevant information for display
        temperature_kelvin = data['main']['temp']
        temperature_celsius = round(temperature_kelvin - 273.15, 2)
        description = data['weather'][0]['description']
        humidity = data['main']['humidity']
        wind_speed = data['wind']['speed']
        return render_template('result.html', city=city, temperature=temperature_celsius, description=description, humidity=humidity, wind_speed=wind_speed)
    else:
        return render_template('error.html')
        
if __name__ == '__main__':
    app.run(host='0.0.0.0')