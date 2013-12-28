import datetime
import requests
import os
import sys
import time
import urlparse


# Set to the receiver's IP address
HOSTNAME = '192.168.1.18'

# Connection errors sometimes occur when running immediately after startup.
# Adjust these two values to give your system time to connect to the network.
MAX_RETRIES = 10
RETRY_DELAY = 5


if len(sys.argv) < 2:
    print "Missing input parameter"
    exit()


work_dir = os.path.dirname(os.path.realpath(__file__))
if sys.argv[1] == 'start':
    payload = '<?xml version="1.0" encoding="utf-8"?><YAMAHA_AV cmd="PUT"><Main_Zone><Power_Control><Power>On</Power></Power_Control></Main_Zone></YAMAHA_AV>'
    log_filename = os.path.join(work_dir, 'start_log.txt')
elif sys.argv[1] == 'stop':
    payload = '<?xml version="1.0" encoding="utf-8"?><YAMAHA_AV cmd="PUT"><Main_Zone><Power_Control><Power>Standby</Power></Power_Control></Main_Zone></YAMAHA_AV>'
    log_filename = os.path.join(work_dir, 'stop_log.txt')
else:
    print "Must call this script with either 'start' or 'stop' parameter"
    exit()


with open(log_filename, 'w') as log:
    log.write(str(datetime.datetime.now()) + '\n')

    headers = {'Content-Type':'text/xml;charset="UTF-8"', 'Accept':'text/xml'}
    retry = 0
    while retry < MAX_RETRIES:
        if retry > 0:
            log.write('Retry #%d\n' % retry)
        try:
            url = urlparse.urlunsplit(('http', HOSTNAME, 'YamahaRemoteControl/ctrl', '', ''))
            r = requests.post(url, data=payload)
            log.write(str(r.status_code) + '\n')
            log.write(r.text)
        except requests.exceptions.RequestException, ex:
            log.write(type(ex).__name__ + '\n')
            retry += 1
            time.sleep(RETRY_DELAY)
        else:
            break
