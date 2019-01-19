import paho.mqtt.client as mqtt


def on_connect(client, user_data, flags, rc):
    print("Successfully connected with result code" + str(rc))

    client.publish("laumio/status/advertise")

    # Connexion
    client.subscribe("laumio/all/discover")

    #client.publish("laumio/Laumio_0FC168/fill", bytes(b'\x255', b'\x0', b'\x255'))
    #client.publish("laumio/Laumio_0FC168/fill", bytes(b'\x255', b'\x255', b'\x03'))
    #client.publish("laumio/Laumio_0FC168/fill", bytes(b'\x0255', b'\x0255', b'\x03'))
    #client.publish("laumio/Laumio_0FC168/fill", bytes(b'255', b'255', b'0'))
    client.publish("laumio/Laumio_0FC168/fill", bytes([255,255,255]))
    
    


def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))


client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("mpd.lan", 1883, 60)

# Execution
#client.publish("/laumio/NNAAMMEE/color_wipe", "00 80 00 1000")
#client.publish("/laumio/Laumio_10805F/fill", "00 80 00")
#client.publish("/laumio/Laumio_0FC168/animate_rainbow")
#client.publish("/laumio/Laumio_10805F/fill", "0000FF")

client.loop_forever()

