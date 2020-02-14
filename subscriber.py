from paho.mqtt.client import Client
from databaseHandler import db_add

def my_on_connect(client, userdata, flags, rc):
    print("Successfully connected")

def my_on_message(client, userdata, message):
    print("Received Message: " + str(message.payload))
    db_add(message.topic, message.payload)


if __name__ == "__main__":
    
    client = Client("localhost")

    client.on_connect = my_on_connect
    client.on_message = my_on_message

    client.connect("localhost")
    client.subscribe("DummyTopic")

    client.loop_forever()
