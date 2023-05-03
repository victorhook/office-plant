from flask import Flask, jsonify
from flask_cors import CORS
import os
from db import DB

app = Flask(__name__)
CORS(app)


class Camera:

    def __init__(self, output_dir: str) -> None:
        self.output_dir = output_dir

    def take_picture(self, quality: int) -> None:
        print(f'Taking picture with quality: {quality}/100')
        os.system(f'raspistill -q {quality} -o {self.output_dir}/test.jpg -t 500')



camera = Camera('images')
db = DB('plant.db')


API_BASE = '/api'


@app.route(f'{API_BASE}/take_picture', methods=['POST'])
def take_picture():
    camera.take_picture(100)
    return 'OK'


@app.route(f'{API_BASE}/samples')
def samples():
    return jsonify(db.get_samples_all())
