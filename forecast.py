from flask import Flask

app = Flask(__name__, '/api')


@app.route('/')
def hello() -> str:
    return 'Hello, World!'


@app.route('/cities', methods=['POST'])
def add_city(city_name):
    pass


app.run()
