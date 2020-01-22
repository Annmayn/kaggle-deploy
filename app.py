from flask import Flask, request
from views.nlp_getting_started import NlpGettingStartedApi

app = Flask(__name__)

@app.route('/', methods=['GET'])
def show():
    return "Hello world"

app.route('/nlp-getting-started/predict', methods=['POST'])(
    NlpGettingStartedApi.as_view()
)

if __name__=='__main__':
    app.run(debug=True, port=8000)