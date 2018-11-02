from flask import Flask, request
from flask_cors import CORS, cross_origin
import base64
import json

app = Flask(__name__)
CORS(app, support_credentials=True)
FORM_INPUT_NAME = 'audio_data'

@app.route('/emotions', methods=['POST'])
@cross_origin(supports_credentials=True)
def emotions_api():

    # IF MIMETYPE FORM
#    a = []
#    for k in request.files:
#        a.append(k)
#    return json.dumps(a)
    if FORM_INPUT_NAME not in request.files:
        return 'Missing voice (POST) data.', 400
    else:
        file = request.files[FORM_INPUT_NAME]
        return json.dumps({
            'audioname': file.filename,
            'data_type': file.content_type,
            'data_in_b64': str(base64.b64encode(file.read()))
        })
    
    # ELSE (mimetype something else)
    # content = request.data
    # to-define

if __name__ == '__main__':
    app.run(host= '0.0.0.0', port=9999, debug=False)
