import paho.mqtt.client as mqtt


def on_connect(client, user_data, flags, rc):
    print("Successfully connected with result code" + str(rc))

    client.subscribe("laumio/status/advertise")

    print("Liste des laumios :")
    client.publish("laumio/all/discover")
    client.subscribe("/distance/value")

    client.publish("laumio/Laumio_439BA9/fill", [0,0,255])


def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))



client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("mpd.lan", 1883, 60)

client.loop_forever()
