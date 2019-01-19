import paho.mqtt.client as mqtt


def on_connect(client, user_data, flags, rc):
    print("Successfully connected with result code" + str(rc))

    


def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))


client.publish("laumio/status/advertise")

client.subscribe("laumio/all/discover")

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("mpd.lan", 1883, 60)

client.subscribe("laumio/status/advertise")

client.publish("laumio/all/animate_rainbow")

client.loop_forever()
