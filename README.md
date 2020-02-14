# MaQiaTTo
Experimenting with MQTT

## Use
First, use the script to initialize the database file:

    $ python init_database.py

this will create the file *storage.db*

Then, open a terminal to run the Publisher -where you can write the messages
you want to publish- and execute the subscriber in another terminal.
Publisher and subscriber are set to exchange message on the same topic.
Publisher stops if you insert value 0.
The subscriber will also add entries to the db using databaseHandler.py
(you don't have to execute this file).

At any time, by using:

    $ python plotData.py

you can obtain the plot of the data currently in the database file.

## Prerequisites
You need to have *paho-mqtt* installed to use these python sources.
Use:

    $ pip install paho-mqtt

or refer to: https://pypi.org/project/paho-mqtt/