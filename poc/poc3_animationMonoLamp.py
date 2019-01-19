import paho.mqtt.client as mqtt
import time


def on_connect(client, user_data, flags, rc):
    print("Successfully connected with result code" + str(rc))

    client.subscribe("laumio/Laumio_10805F/discover")
    client.subscribe("laumio/Laumio_0FC168/discover")


def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))


client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("mpd.lan", 1883, 60)

client.subscribe("laumio/status/advertise")

client.publish("laumio/Laumio_10805F/json", payload="{'command': 'fill', 'rgb': [50, 50, 255]}")
client.publish("laumio/Laumio_0FC168/json", payload="{'command': 'fill', 'rgb': [255, 50, 50]}")
time.sleep(1.5)
client.publish("laumio/Laumio_10805F/json", payload="{'command': 'fill', 'rgb': [255, 50, 50]}")
client.publish("laumio/Laumio_0FC168/json", payload="{'command': 'fill', 'rgb': [50, 50, 255]}")
time.sleep(1.5)
client.publish("laumio/Laumio_10805F/json", payload="{'command': 'fill', 'rgb': [50, 50, 255]}")
client.publish("laumio/Laumio_0FC168/json", payload="{'command': 'fill', 'rgb': [255, 50, 50]}")
time.sleep(1.5)
client.publish("laumio/Laumio_10805F/json", payload="{'command': 'fill', 'rgb': [255, 50, 50]}")
client.publish("laumio/Laumio_0FC168/json", payload="{'command': 'fill', 'rgb': [50, 50, 255]}")

client.loop_forever()
