# This is a small script for testing NTP servers

It's requests one time per second information from server and sav it to sqlite DB.


### Requests

+ python3.x
+ ntplib (https://pypi.org/project/ntplib/)

### TO DO:
1. Write a manual.


### Маленький подвал

#### Содержание ответа функции ntpclient.request(<address>)
    leap  :  0
    version  :  2
    mode  :  4
    stratum  :  2
    poll  :  0
    precision  :  -20
    root_delay  :  0.0442962646484375
    root_dispersion  :  0.0270233154296875
    ref_id  :  1332713477
    ref_timestamp  :  3883623951.1460996
    orig_timestamp  :  3883624060.239808
    recv_timestamp  :  3883624061.176018
    tx_timestamp  :  3883624061.176056
    dest_timestamp  :  3883624060.240883
#### Скрипт для получения имеющихся параметров объекта (Python)
    for property, value in vars(<theObject>).items():
      print(property, ":", value


