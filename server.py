from flask import Flask, request
import base64
import json

app = Flask(__name__)

@app.route('/emotions', methods=['POST'])
def emotions_api():

    # IF MIMETYPE FORM
    ###
    #if 'file' not in request.files:
    #    return 'Missing voice (POST) data.', 400
    #else:
    #    file = request.files['file']
    #    return json.dumps({
    #        'formfilename': file.filename,
    #        'b64_data': base64.b64encode(file.read)
    #    })
    #

    # ELSE (mimetype something else)
    # content = request.data
    # to-define

    return 'Placeholder'

if __name__ == '__main__':
    app.run(host= '0.0.0.0', port=9999, debug=False)
