from flask import render_template, request, jsonify
import connexion
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