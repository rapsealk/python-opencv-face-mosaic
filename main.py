#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
from flask import Flask, request, jsonify
from werkzeug.utils import secure_filename
import time
from multiprocessing import Process

from utils import ImageProcess

app = Flask(__name__)


@app.route('/api/frame', methods=['POST'])
def process_frame():
    """
    입력된 얼굴 사진을 RESTful API 방식으로 전달하면 서버에서 해당 이미지를 분석해서
    결과를 JSON 형태로 리턴해주는 API입니다.
    """
    # if request.method == 'POST'
    frame = request.files['frame']
    filename = secure_filename(f'{str(int(time.time()))}.jpg')
    frame.save(filename)

    ImageProcess.detect_face(filename)

    return jsonify({'code': 200})


@app.route('/api/face_recognition', methods=['POST'])
def face_recognition():
    return jsonify({'code': 200})


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
