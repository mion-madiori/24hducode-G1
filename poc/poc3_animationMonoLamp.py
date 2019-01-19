import paho.mqtt.client as mqtt
import time


def on_connect(client, user_data, flags, rc):
    print("Successfully connected with result code" + str(rc))

    client.publish("laumio/status/advertise")

    client.subscribe("laumio/Laumio_10805F/discover")


def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))


client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("mpd.lan", 1883, 60)

client.subscribe("laumio/status/advertise")

client.publish("laumio/Laumio_10805F/animate_rainbow")
time.sleep(3)
client.publish("laumio/Laumio_10805F/fill", payload="{'command': 'fill','rgb': [255, 0, 255]}")
time.sleep(3)
client.publish("laumio/Laumio_10805F/animate_rainbow")
time.sleep(3)
client.publish("laumio/Laumio_10805F/fill", payload="{'command': 'fill','rgb': [255, 0, 255]}")

client.loop_forever()
