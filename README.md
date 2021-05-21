# MaQiaTTo
Experimenting with MQTT.

## Use
First, use the script to initialize the database file:

    $ python3 init_database.py

this will create the file *storage.db*

Then, open a terminal to run the Publisher -where you can write the messages
you want to publish- and execute the subscriber in another terminal.
Publisher and subscriber are configured to exchange messages on the same topic.
Publisher stops when you insert value 0.
The subscriber will also add entries to the database by using a function inside
databaseHandler.py (but you don't have to execute this file).

At any time, by using:

    $ python3 plotData.py

you can obtain the plot of the data currently present in the database file.

## Prerequisites
A MQTT packet broker is required to execute the code in this repository.
You can get one with:

    $ sudo apt install mosquitto

To start the packet broker service, type:

    $ sudo service mosquitto start

You need to have *paho-mqtt* installed to use these python sources.
Use:

    $ pip install paho-mqtt

or refer to: https://pypi.org/project/paho-mqtt/

You can resolve dependencies to run the plotData scirpt with

    $ pip3 install numpy, matplotlib
