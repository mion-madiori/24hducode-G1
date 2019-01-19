import paho.mqtt.client as mqtt


def on_connect(client, user_data, flags, rc):
    print("Successfully connected with result code" + str(rc))

    client.publish("laumio/status/advertise")

    # Connexion
    client.subscribe("laumio/Laumio_10805F/discover")
    
    


def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))


client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("mpd.lan", 1883, 60)

# Execution
#client.publish("/laumio/NNAAMMEE/color_wipe", "00 80 00 1000")
#client.publish("/laumio/Laumio_10805F/fill", "00 80 00")
client.publish("/laumio/Laumio_10805F/animate_rainbow")
#client.publish("/laumio/Laumio_10805F/fill", "0000FF")
1
client.loop_forever()
