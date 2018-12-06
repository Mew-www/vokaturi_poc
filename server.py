from flask import Flask, request
from flask_cors import CORS, cross_origin
import base64
import json
import random
import argparse
import os
from io import BytesIO
from kowalski import analysis

app = Flask(__name__)
CORS(app, support_credentials=True)

@app.route('/interval', methods=['GET'])
def analysis_interval():
    return '5'

@app.route('/emotions', methods=['POST'])
@cross_origin(supports_credentials=True)
def emotions_api():
    # A loose specification - expect single attachment
    available_files = []
    for name in request.files:
        available_files.append(name)
    presumably_only_filename = available_files[0] if len(available_files) > 0 else None

    # Check at least one exists
    if presumably_only_filename is None:
        return 'Missing voice (POST) data.', 400

    file = request.files[presumably_only_filename]
    analysis_results = analysis(BytesIO(file.read()))
    if analysis_results is not None:
        return json.dumps(analysis_results)
    else:
        return json.dumps({
            'neutral': 100,
            'happy': 0,
            'sad': 0,
            'angry': 0,
            'fear': 0
        })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9999, debug=False, ssl_context=('sslcert.pem', 'sslkey.pem'))
