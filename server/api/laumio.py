import paho.mqtt.client as mqtt
import time


adresseMpd = "mpd.lan"
portMdp = 1883
keepAlive = 60
laumios = {}

######################
# FONCTION GENERIQUE #
######################

# Fonction d'écoute après connexion
def on_connect(client, user_data, flags, rc):
    print("Successfully connected with result code" + str(rc))

# Fonction d'écoute des messages
def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))
    # Pour discover
    if(msg.topic=="laumio/all/discover"):
        laumios[msg.payload]=""

# Fonction de connexion avec retour client
def createClient():
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message
    return client

###################
# FONCTIONS d'API #
###################

# API - Animation arc-en-ciel sur une lampe Laumio
def rainbow(nom):
    # Création et connexion du client
    client = createClient()
    client.connect(adresseMpd, portMdp, keepAlive)
    # Exécution du script
    client.publish("laumio/" + nom + "/animate_rainbow")
    

# API - Animation arc-en-ciel sur toutes les lampes
def rainbowAll():
    rainbow("all")

# API - Remplissage couleur sur une lampe Laumio
def fill(nom, couleur):
    # Création et connexion du client
    client = createClient()
    client.connect(adresseMpd, portMdp, keepAlive)
    # Exécution du script
    client.publish("laumio/" + nom + "/json", payload="{'command': 'fill', 'rgb': " + couleur + "}")

# API - Remplissage couleur sur toutes les lampes
def fillAll(couleur):
    fill("all", couleur)

# API - Récupération de toutes les laumios
def allLaumios():
    client = createClient()
    client.subscribe("laumio/status/advertise")
    client.publish("laumio/all/discover")
    time.sleep(1)
    client.unsubscribe("laumio/status/advertise")
    client.disconnect()
    # on récupère les laumios
    return laumios.keys()

# API - Mise en route, ou non, d'une laumio
def power_laumio(laumios, state=False):
    client = createClient()
    client.on_connect = on_connect
    client.on_message = on_message
    client.connect(adresseMpd, portMdp, keepAlive)
    color = [255, 255, 255] if state else [0, 0, 0]
    if isinstance(laumios, list):
        for laumio in laumios:
            client.publish("laumio/" + laumio + "/json", payload="{'command': 'fill', 'rgb': " + str(color) + "}")
    else:
        client.publish("laumio/" + laumios + "/json", payload="{'command': 'fill', 'rgb': " + str(color) + "}")


#client.publish("laumio/status/advertise")

#client.subscribe("laumio/all/discover")


#client.subscribe("laumio/status/advertise")

#client.publish("laumio/all/animate_rainbow")

#client.loop_forever()
