#!/bin/python
#Test progrramm for NTP server test

import sqlite3
import ntplib
import argparse
import time
import os

#log levels
ll_name=["critical","error","warning","info","debug"]

def init_argparse():
  try:
    default_db_name = "NtpSrvTest.db"
    parser = argparse.ArgumentParser("This is NTP server test programm.")
    parser.add_argument('-d','--db-name', type=str, default = default_db_name,
                         help="Database name. Default DB name is: \'"
                         + default_db_name + "\'")
    parser.add_argument('-a','--address', type=str, help='Server address')
    parser.add_argument('-l','--log-level', type=int, default = 1, help='Logging level from 0(critical) to 7(debug). Default = 1(error)')
    #parse arguments
    args = parser.parse_args()
    return args
  except Exception as err:
#    log_message(1, "Function : init_argparse(). Someting goes wrong! Error message : " + str(err))
    return False

#Функция создания\открытия БД SQLITE
def init_db(db_name):
  try:
    if not (os.path.exists(db_name)):
      #Если БД отсутствует - создаем ее и создаем в ней пустую таблицу для данных.
      db_conn = sqlite3.connect(db_name)
      curs = db_conn.cursor()
      curs.execute('''
        CREATE TABLE ntp_test (
          record_id INTEGER PRIMARY KEY AUTOINCREMENT,
          db_timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
          offset REAL,
          stratum INTEGER);
      ''')
      # Коммитим изменения в БД и возвращаем маркеры БД и курсора
      db_conn.commit()
      return db_conn, curs
    else:
      # в другом случае - пытаемся открыть БД и вернуть маркеры.
      db_conn = sqlite3.connect(db_name)
      curs = db_conn.cursor()
      db_conn.commit()
      return db_conn, curs
  except Exception as err:
#    log_message(1, "Function : init_db(). Someting goes wrong! Error message : " + str(err))
    return False
    
# Функция записи информации offset и startum в БД
def write_db(db_conn, curs, offset, stratum):
  try:
    curs.execute('''
      INSERT INTO ntp_test(offset, stratum)
      VALUES (\'''' + str(offset) + '''\', \'''' + str(stratum) + '''\') 
    ''')
    db_conn.commit()
    return True
  except Exception as err:
#    log_message(1, "Function : write_db(). Someting goes wrong! Error message : " + str(err))
    return False

# Функция опроса NTP
def get_ntp_data(address):
  try:
    ntp_data = ntplib.NTPClient().request(address)
    return ntp_data
  except Exception as err:
#    log_message(1, "Function : get_db_data(). Someting goes wrong! Error message : " + str(err))
    return False

def log_message(message_level,message):
  try:
    if(message_level <= args.log_level):
      print(time.asctime(time.localtime()) + " : " + str(ll_name[message_level]).upper() + " : " + str(message))
    return True
  except Exception as err:
    print("Someting broke in log_message() function. Error message is: " + str(err))
    return False

if __name__ == "__main__":
  try:
    log_message(4,"Start script. Parsing arguments.")
    args = init_argparse()
    log_message(4,"Trying to open DB.")
    db_conn, curs = init_db(args.db_name)
    log_message(4,"DB is opend, geting data from NTP server.")
    db_conn, curs = init_db(args.db_name)
    while True:
      ntp_data = get_ntp_data(args.address)
      log_message(5, "Data from server recieved.")
      write_db(db_conn, curs, ntp_data.offset, ntp_data.stratum)
      log_message(5, "Data writed to DB. Wait for 1 sec.")
      time.sleep(1)
  except Exception as err:
    db_conn.commit()
    db_conn.close()
    log_message(1, "Someting goes wrong! Error message : ")
  except KeyboardInterrupt:
    db_conn.commit()
    db_conn.close()
    log_message(4, "Normal stop.")


