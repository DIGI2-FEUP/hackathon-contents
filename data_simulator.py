#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from paho.mqtt.client import Client
import json
import time
import os

# @reboot sleep 30 && /bin/python3 /home/digi2/hackathon/data_simulator.py

folder_files = '/home/eliseu/Mega/projects/reclaim/reclaim-dev/hackathon/welding_samples'
file_path = '/home/eliseu/Mega/projects/reclaim/reclaim-dev/hackathon/welding_samples/weld_{}.json'
delay_seconds = 20  # delay between weldings
broker_ip = '192.168.0.120'
broker_port = 1883
machine_name = 'spot_weld_0'
mqtt_topic = '{0}/sensor_data'.format(machine_name)

"""
# %% reads the file
file_path = '/home/eliseu/Mega/projects/reclaim/reclaim-dev/HWH_weld_analysis/simulated_data/simulatedWeldingDataWithDisplacement_4.json'
with open(file_path, 'r') as f:
    json_data = json.load(f)

print('# weldings:', len(json_data))

# %% saves welding samples as json
for i, we in enumerate(json_data):
    with open(.format(i), 'w') as f:
        json.dump(we, f)
"""

# %% mqtt client creation
mqtt_client = Client(machine_name, clean_session=False)
mqtt_client.connect(broker_ip, broker_port)
mqtt_client.loop_start()

# %% simulates the data generation
n_we = len(os.listdir(folder_files))
i = 0
while i < n_we:
    # builds the path
    path = file_path.format(i)
    # reads the json
    with open(path, 'r') as f:
        we = json.load(f)
    # publishes the messages
    we_str = json.dumps(we)
    mqtt_client.publish(mqtt_topic, we_str)
    print(path)
    # waits the simulated time
    time.sleep(delay_seconds)
    i += 1
    # restarts sending the first samples
    if i == n_we:
        i = 0
