import paho.mqtt.client as mqtt
import time
import json


def on_connect(client, userdata, flags, rc):
    print("Successfully connected with result code " + str(rc))

    client.subscribe("laumio/status/advertise")

    print("Liste des laumios :")
    client.publish("laumio/all/discover")
    client.subscribe("atmosphere/temperature")

    client.publish("laumio/Laumio_0FC168/json", payload="{'command': 'fill','rgb': [255, 0, 255]}")


def on_message(client, userdata, msg):
    try:
        print(msg.topic+" "+str(msg.payload))
        print("?? " + msg.topic + ">= atmosphere/temperature")
        if str(msg.topic) == "atmosphere/temperature":
            print(int.from_bytes(msg.payload))
            if int.from_bytes(msg.payload) >= 25:
                print("coucou")
                client.publish("laumio/Laumio0FC168/json", payload="{'command': 'color_wipe', 'duration', 3, 'rgb': [255, 50, 50]}")
    except Exception as e:
        print("Oupsi, error detected: " + repr(e))




def on_publish(client, user_data, rc):
    pass


client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.on_publish = on_publish

client.connect("mpd.lan", 1883, 60)

client.loop_forever()
