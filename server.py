from flask import Flask, request
from flask_cors import CORS, cross_origin
import base64
import json
import random

app = Flask(__name__)
CORS(app, support_credentials=True)

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
    #return json.dumps({
    #    'audioname': file.filename,
    #    'data_type': file.content_type,
    #    'data_in_b64': str(base64.b64encode(file.read()))
    #})
    # Return pseudodata for the moment - TODO integration to the vokaturi lib
    neutral = random.randint(0, 100)
    happy = random.randint(0, 100-neutral)
    sad = random.randint(0, 100-neutral-happy)
    angry = random.randint(0, 100-neutral-happy-sad)
    fear = 100-neutral-happy-sad-angry
    return json.dumps({
        'neutral': neutral,
        'happy': happy,
        'sad': sad,
        'angry': angry,
        'fear': fear
    })
    
if __name__ == '__main__':
    app.run(host= '0.0.0.0', port=9999, debug=False)
