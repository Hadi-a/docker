from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Baby Shark do doo dooo doo'

@app.route('/more')
def health():
    return 'Wheel on the bus goes round and round'
