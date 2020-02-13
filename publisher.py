from paho.mqtt.client import Client
from datetime import datetime
import json

if __name__ == "__main__":

    client = Client("localhost:1883")
    client.connect("localhost")

    message = {}
    message['Sensor'] = "MySensor"

    while True:
        a = input()

        try:
            float(a)
        except ValueError:
            print("ERR: Numbers only!")
            continue

        if a == "0":
            print("Exiting...")
            break
        
        message['Time'] = (datetime.now()).strftime("%d-%b-%Y %H:%M:%S:%f")
        message['Value'] = a
        message_json = json.dumps( message )
        
        client.publish("DummyTopic", message_json)
        
    client.disconnect()
