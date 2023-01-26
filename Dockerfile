FROM python:3.8-slim

WORKDIR /NTP_TEST

RUN cp -s /usr/local/bin/python3.8 /bin/python &&\
    pip install --upgrade pip &&\
    pip install ntplib

COPY test_server.py .

CMD ["./test_server.py","-d", "ntp_test.db","-a","192.168.2.1","-l","$TEST_VERBOSE"]
