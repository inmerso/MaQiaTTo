#!/usr/bin/env python

from paho.mqtt.client import Client
from databaseHandler import db_add

def connect_callback(client, userdata, flags, rc):
    print("Successfully connected")

def message_callback(client, userdata, message):
    # print("Received Message: " + str(message.payload))
    db_add(message.topic, message.payload)

def disconnect_callback(client, userdata, rc):
    print("Disconnected")

if __name__ == "__main__":
    
    client = Client("localhost")

    client.on_connect = connect_callback
    client.on_message = message_callback
    client.on_disconnect = disconnect_callback

    client.connect("localhost")
    client.subscribe("DummyTopic")

    client.loop_start()

    while True:
        a = input()
        try:
            a = int(a)
        except ValueError as identifier:
            print("type 0 to stop")
            continue
        if a == 0:
            client.loop_stop()
            client.disconnect()
            exit()
