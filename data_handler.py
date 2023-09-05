#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from paho.mqtt.client import Client
import psycopg2
import json

# connect to the broker
client = Client()
client.connect("20.199.100.235", 1883)

# connect to database
con = psycopg2.connect(database="testdb", user="digi2-postgres", password="digi2-2023", host="20.199.100.235", port="5432")
insert_statement = (
        'INSERT INTO "WELD_SAMPLES" (\
            time_start, \
            time_end, \
            environment_t, \
            motor_bearing_t, \
            spindle_bearing_t, \
            counter, \
            sdintensity, \
            times, \
            angular_velocity, \
            force, \
            displacement\
            ) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
   )

def on_message(client, userdata, msg):
    print(f"Received message from `{msg.topic}` topic")
    # Variable type of message is string, meaning that needs handling.
    received_data = msg.payload.decode()
    # Converts the str to dict.
    values_dict = json.loads(received_data)
    values_list = list(values_dict.values())
    # inserts into DB
    cursor_obj = con.cursor()
    cursor_obj.execute(insert_statement, values_list)
    con.commit()
    cursor_obj.close()
    

# subscribes to the topic
client.subscribe("spot_weld_0/sensor_data")
client.on_message = on_message
client.loop_forever()
