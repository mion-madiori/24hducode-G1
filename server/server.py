from flask import render_template, request, jsonify
import connexion
import requests
from api.laumio import *


# Création de l'instance de l'application
app = connexion.App(__name__, specification_dir='./')

# Lecture du fichier swagger.yml pour configurer les endpoints
# app.add_api('swagger.yml')



@app.route('/')
def hello():
    return jsonify({'success': True})


@app.route('/rainbow', methods=["POST"])
def rainboww():
    rainbow(request.get_json().name)
    return jsonify(request.get_json())


@app.route('/rainbows')
def rainbows():
    rainbowAll()


@app.route('/fill', methods=["POST"])
def fillz():

    print(request.get_json())
    fill(request.get_json()["name"], request.get_json()["color"])
    return jsonify(request.get_json())

@app.route('/power', methods=["POST"])
def power():
    power_laumio(request.get_json()["name"], request.get_json()["state"])


@app.route('/weather', methods=["POST"])
def weather():
    laumio_color = []
    weather = requests.get("api.openweathermap.org/data/2.5/weather?q="+request.get_json()["city"]+"&appid=8cb904d3cd0bc9019a4515f0626d916d")["weather"]["main"]
    if weather in ["Fog", "Rain", "Mist"]:
        laumio_color = [50, 50, 150]
    elif weather in ["Cloudy"]:
        laumio_color = [255, 255, 255]
    elif weather in ["Sunny"]:
        laumio_color = [255, 255, 0]

    fillAll(laumio_color)

    return jsonify({"response": 200})


# Création d'une route URl dans l'application pour "/"
@app.route('/')
def home():
    """
    This function just responds to the browser ULR
    localhost:5000/

    :return:        the rendered template 'home.html'
    """
    return render_template('home.html')

# Si on execute en mode standalone, exécuter l'application
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)