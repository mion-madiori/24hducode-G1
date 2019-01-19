from flask import render_template
import connexion

# Création de l'instance de l'application
app = connexion.App(__name__, specification_dir='./')

# Lecture du fichier swagger.yml pour configurer les endpoints
app.add_api('swagger.yml')

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