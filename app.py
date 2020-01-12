from flask import Flask, request
from views.nlp_getting_started import NlpGettingStartedApi

app = Flask(__name__)

@app.route('/', methods=['POST'])
def show():
    print(request.get_json()['text'])
    return request.get_json()

app.route('/predict', methods=['GET','POST'])(
    NlpGettingStartedApi.as_view()
)

if __name__=='__main__':
    app.run(debug=True, port=8000)