#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import psycopg2

con = psycopg2.connect(database="team_a", user="digi2-postgres", password="digi2-2023", host="20.199.100.235", port="5432")
cursor = con.cursor()
    
# Change table's name.
cursor.execute('CREATE TABLE IF NOT EXISTS "WELD_SAMPLES" (\
       "id" serial, \
       "time_start" float, \
       "time_end" float, \
       "environment_t" float, \
       "motor_bearing_t" float, \
       "spindle_bearing_t" float, \
       "counter" int, \
       "sdintensity" float, \
       "times" float ARRAY, \
       "angular_velocity" float ARRAY, \
       "force" float ARRAY, \
       "displacement" float ARRAY\
    )')

con.commit()
cursor.close()
con.close()
