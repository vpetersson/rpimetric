#!/usr/bin/env python
import time
import requests
import os
from sh import vcgencmd
from sense_hat import SenseHat

# Set this to the target endpoint, such as:
# http://1.2.3.4:9091/metrics/job/iot-lab
API_ENDPOINT = os.getenv('API_ENDPOINT')
sense = SenseHat()


def push_data(payload):
    if not payload.endswith('\n'):
        payload += '\n'

    r = requests.put(
        API_ENDPOINT,
        data=payload,
    )
    return r.status_code


def get_cpu_temp():
    read_temp = str(vcgencmd('measure_temp'))
    return read_temp.replace('temp=','').replace('\'C','').strip()


def main():
    while True:
        payload = []
        get_reading = sense.get_gyroscope()

        payload.append('rpi_pitch {}'.format(get_reading['pitch']))
        payload.append('rpi_roll {}'.format(get_reading['roll']))
        payload.append('rpi_yaw {}'.format(get_reading['yaw']))
        payload.append('rpi_humidity {}'.format(sense.humidity))
        payload.append('rpi_pressure {}'.format(sense.pressure))
        payload.append('rpi_temp {}'.format(sense.temp))
        payload.append('rpi_cpu_temp {}'.format(get_cpu_temp()))

        print push_data('\n'.join(payload))

        time.sleep(5)

if __name__ == "__main__":
    main()
