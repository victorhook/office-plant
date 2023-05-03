#!/usr/bin/env python3

from datetime import datetime
from pathlib import Path
import os
from subprocess import Popen, PIPE
from db import DB

import RPi.GPIO as gpio 


DATETIME_FORMAT = '%Y-%m-%d_%H:%M'
SAMPLE_DIR_NAME = 'samples'
SAMPLE_FORMAT = '{}.jpg'
SAMPLE_BASE_PATH = Path(__file__).absolute().parent.joinpath(SAMPLE_DIR_NAME)
IMAGE_QUALITY = 100
PIN_LED = 12


def create_image_path(timestamp: str) -> str:
    filename = SAMPLE_FORMAT.format(timestamp)
    return SAMPLE_BASE_PATH.joinpath(filename)


def print_banner(msg: str) -> None:
    stdout_width = 60
    msg_start = (60//2) - (len(msg)//2)
    print('*' * stdout_width)
    print()
    print((msg_start * ' ') + msg)
    print()
    print('*' * stdout_width)


class TempSensor:

    TEMP_SENSOR_PATH = '/sys/bus/w1/devices/28-3c01d607adc1/w1_slave'

    @classmethod
    def get_temperature(cls) -> float:
        pipe = Popen(['cat', cls.TEMP_SENSOR_PATH], stdout=PIPE)
        result = pipe.stdout.read().decode('ascii')
        temp = result.split('t=')[-1].strip()
        return int(temp) / 1000


class Led:

    def __init__(self, pin: int) -> None:
        self._pin = pin
        gpio.setup(self._pin, gpio.OUT)
        self.set(0)
        
    def set(self, value: int) -> None:
        gpio.output(self._pin, value)



if __name__ == '__main__':
    print_banner('Sampling started!')    
   
    try:
        db = DB('plant.db')

        # Initialize GPIO
        gpio.setmode(gpio.BCM)
        led = Led(PIN_LED)
        temp_sensor = TempSensor()

        timestamp = datetime.now().strftime(DATETIME_FORMAT)
        output_file = create_image_path(timestamp)

        photo_cmd = f'raspistill -q {IMAGE_QUALITY} -o {output_file}'

        print(f'Taking photo: "{photo_cmd}"')
        led.set(1)
        os.system(photo_cmd)

        print('Taking temperature...')
        temperature = temp_sensor.get_temperature()
        print(f'It\'s {temperature}°C in the office!')

        print('Inserting into database')
        db.insert(0, temperature)

        led.set(0)
        
    finally:
        gpio.cleanup()
        db.close()

    print_banner('Sampling ended!')    
