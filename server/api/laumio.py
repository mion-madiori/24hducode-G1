import paho.mqtt.client as mqtt

adresseMpd = "mpd.lan"
portMdp = 1883
keepAlive = 60

######################
# FONCTION GENERIQUE #
######################

# Fonction d'écoute après connexion
def on_connect(client, user_data, flags, rc):
    print("Successfully connected with result code" + str(rc))

# Fonction d'écoute des messages
def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))

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

#client.publish("laumio/status/advertise")

#client.subscribe("laumio/all/discover")

#client.subscribe("laumio/status/advertise")

#client.publish("laumio/all/animate_rainbow")

#client.loop_forever()
