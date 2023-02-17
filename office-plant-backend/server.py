from flask import Flask
from flask_cors import CORS
import sqlite3
import os

app = Flask(__name__)
CORS(app)


PIN_LED = 24
RUNNING_ON_RPI = os.environ.get('RUNNING_ON_RPI', False)

if RUNNING_ON_RPI:
    print('Running live on raspberry pi')
    import RPi.GPIO as GPIO
    GPIO.setmode(GPIO.BCM)
else:
    print('Running in debug on PC')

# CREATE TABLE plant (timestamp datetime, temperature float); '


class Record:
    timestamp: str # Datetime
    temperature: float

class Database:

    def __init__(self, db: str) -> None:
        self.db = sqlite3.connect(db)
        self.table = 'Plant'

    def insert(self):
        pass

    def fetch(self):
        records = self.db.execute(f'SELECT * FROM {self.table};').fetchall()
        return records


class Camera:

    def __init__(self, output_dir: str) -> None:
        self.output_dir = output_dir

    def take_picture(self, quality: int) -> None:
        if not RUNNING_ON_RPI:
            print('Mocking picture')
            return

        print(f'Taking picture with quality: {quality}/100')
        os.system(f'raspistill -q {quality} -o {self.output_dir}/test.jpg -t 500')


class Led:

    def __init__(self, gpio) -> None:
        if not RUNNING_ON_RPI:
            print('Mocking LED')
            return

        self.gpio = gpio
        GPIO.setup(self.gpio, GPIO.OUT)
        self.set(0)

    def set(self, value: int) -> None:
        if not RUNNING_ON_RPI:
            print(f'Mocking LED: {value}')
            return

        GPIO.output(self.gpio, value)


# Instantiations
camera = Camera('images')
led = Led(PIN_LED)
db = sqlite3.connect('plant.db')


@app.route('/')
def index():
    pass

@app.route('/take_picture', methods=['POST'])
def take_picture():
    camera.take_picture(100)
    return 'OK'