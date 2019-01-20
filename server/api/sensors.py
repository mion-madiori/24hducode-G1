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


def capteur_bp():
    return None


def remote(key_name):
    return None


def presence():
    client = createClient()


def atmosphere(type):
