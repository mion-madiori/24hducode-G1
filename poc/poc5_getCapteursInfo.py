import paho.mqtt.client as mqtt

def pseudo_byte_to_int(byte_value):
    str_value = ""

    for char in str(byte_value):
        if char not in ['b', '\'']:
            str_value += char

    return float(str_value)


def on_connect(client, userdata, flags, rc):
    print("Successfully connected with result code " + str(rc))

    client.subscribe("laumio/status/advertise")

    print("Liste des laumios :")
    client.publish("laumio/all/discover")
    # client.subscribe("atmosphere/temperature")
    client.subscribe("distance/value")

    # client.publish("laumio/Laumio_0FC168/json", payload="{'command': 'fill','rgb': [0, 0, 255]}")


def on_message(client, userdata, msg):
    try:
        print(msg.topic+" "+str(msg.payload))
        if str(msg.topic) == "atmosphere/temperature":
            print(type(msg.payload))
            print(pseudo_byte_to_int(msg.payload))
            if pseudo_byte_to_int(msg.payload) >= 30:
                print("coucou")
                client.publish("laumio/Laumio_0FC168/json", payload="{'command': 'fill', 'rgb': [255, 50, 50]}")
            elif pseudo_byte_to_int(msg.payload) < 30 and pseudo_byte_to_int(msg.payload) >= 20:
                client.publish("laumio/Laumio_0FC168/json", payload="{'command': 'fill', 'rgb': [255, 120, 120]}")
            elif pseudo_byte_to_int(msg.payload) < 10:
                client.publish("laumio/Laumio_0FC168/json", payload="{'command': 'fill', 'rgb': [50, 50, 255]}")
        elif str(msg.topic) == "distance/value":
            sec_color = int(255 - pseudo_byte_to_int(msg.payload) * 127)
            print(sec_color)
            main_color = int(255 - pseudo_byte_to_int(msg.payload) * 43)
            print(main_color)
            print("{'command': 'fill', 'rgb': [" + str(sec_color) + ", " + str(sec_color) + ", " + str(main_color) + "]}")
            client.publish("laumio/Laumio_0FC168/json", payload="{'command': 'fill', 'rgb': [0, " + str(main_color) + ", " + str(main_color) + "]}")

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
