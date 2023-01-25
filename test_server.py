#!/bin/python
#Test progrramm for NTP server test


import sqlite3
import argparse
import time
import os

def init_argparse():
  default_db_name = "NtpSrvTest.db"
  parser = argparse.ArgumentParser("This is NTP server test programm.")
  parser.add_argument('-d','--db-name', type=str, default = default_db_name, help="Database name. Default DB name is: \'"+ default_db_name + "\'")
  parser.add_argument('-a','--address', type=str, , help='Server address')
  #parse arguments
  args = parser.parse_args()
  return args

def init_db(db_name):
  if not (os.path.exists(db_name):
    db_conn = sqlite3.connect(db_name)
    curs = db_conn.cursor()
    curs.execute('''
      CREATE TABLE sens_data (
        record_id INTEGER PRIMARY KEY AUTOINCREMENT,
        db_timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
        timestamp REAL
        offset REAL,
        staratum INTEGER)
    
    ''')
  
