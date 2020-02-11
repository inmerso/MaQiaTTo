from paho.mqtt.client import Client

if __name__ == "__main__":

    client = Client("localhost:1883")
    client.connect("localhost")

    while True:
        a = input()
        if a != "0":
            client.publish("DummyTopic", a)
        else:
            break

    client.disconnect()
