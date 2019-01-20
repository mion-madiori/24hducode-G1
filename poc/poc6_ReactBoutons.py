# coding=UTF-8

import paho.mqtt.client as mqtt

bp1on = False
bp2on = False
bp3on = False

def on_connect(client, user_data, flags, rc):
    print("Successfully connected with result code " + str(rc))

    client.subscribe("capteur_bp/binary_sensor/bp1/state")
    client.subscribe("capteur_bp/binary_sensor/bp2/state")
    client.subscribe("capteur_bp/binary_sensor/bp3/state")
    client.subscribe("laumio/status/advertise")

    print("Liste des laumios :")
    client.publish("laumio/all/discover")


def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))

    if(msg.topic=="capteur_bp/binary_sensor/bp1/state"):
        if(msg.payload=="ON" and not bp1on):
            client.publish("laumio/Laumio_107DA8/json", payload="{'command': 'fill','rgb': [0, 0, 255]}")
            bp1on = True
        elif(msg.payload=="ON" and bp1on):
            client.publish("laumio/Laumio_107DA8/json", payload="{'command': 'fill','rgb': [0, 0, 255]}")
            bp1on = False

    if(msg.topic=="capteur_bp/binary_sensor/bp2/state"):
        if(msg.payload=="ON" and not bp2on):
            client.publish("laumio/Laumio_88813D/json", payload="{'command': 'fill','rgb': [0, 255, 0]}")
            bp2on = True
        elif(msg.payload=="ON" and bp2on):
            client.publish("laumio/Laumio_88813D/json", payload="{'command': 'fill','rgb': [0, 128, 0]}")
            bp2on = False

    if(msg.topic=="capteur_bp/binary_sensor/bp3/state"):
        if(msg.payload=="ON" and not bp3on):
            client.publish("laumio/Laumio_CD0522/json", payload="{'command': 'fill','rgb': [256, 0, 0]}")
            bp3on = True
        elif(msg.payload=="ON" and bp3on):
            client.publish("laumio/Laumio_CD0522/json", payload="{'command': 'fill','rgb': [128, 0, 0]}")
            bp3on = False

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("mpd.lan", 1883, 60)

client.loop_forever()
