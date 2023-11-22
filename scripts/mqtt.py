from paho.mqtt import client as mqtt


def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to MQTT broker")
        client.connected.flag = True
    else:
        print("Bad connection to MQTT broker, returned code = ", rc)


def on_message(client, userdata, msg):
    print("msg: " + str(msg))


def on_publish(client, userdata, mid):
    print("mid: " + str(mid))


def get_mqtt_client():
    client = mqtt.Client()
    client.connected_flag = False
    client.on_connect = on_connect
    client.on_publish = on_publish
    return client
