import os
import json
import numpy as np
from mqtt import get_mqtt_client
from helpers import (
    get_config,
    get_json,
    update_json,
)

# Config file
CONFIG_FILE_PATH = os.getenv("MQTT_CAMERA_CONFIG", "./config.json")
CONFIG = get_config(CONFIG_FILE_PATH)

# Payload data
PAYLOAD_FILE_PATH = os.getenv("MQTT_CAMERA_PAYLOAD", "./payload.json")

# MQTT configurations
MQTT_BROKER = CONFIG["mqtt"]["broker"]
MQTT_PORT = CONFIG["mqtt"]["port"]
MQTT_TOPIC = CONFIG["mqtt"]["topic"]
MQTT_QOS = CONFIG["mqtt"]["QOS"]
MQTT_PAYLOAD = f"{np.random.randint(1, 100)}"

client = get_mqtt_client()


def main():
    get_payload()
    client.connect(MQTT_BROKER, port=MQTT_PORT)
    client.publish(MQTT_TOPIC, payload=json_string, qos=MQTT_QOS, retain=False)


def get_payload():
    global payload
    payload = get_json(PAYLOAD_FILE_PATH)
    global json_string
    json_string = json.dumps(payload)


def toggle_on():
    update_json(PAYLOAD_FILE_PATH, "command", "start")
    main()


def toggle_off():
    update_json(PAYLOAD_FILE_PATH, "command", "stop")
    main()


def algo():
    # update_json_value(PAYLOAD_FILE_PATH, "algo", "3")
    update_json(PAYLOAD_FILE_PATH, "param.algo", np.random.randint(1, 100))
    # main()
