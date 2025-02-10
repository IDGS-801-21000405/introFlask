from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return '<h1>Hola mundo!</h1>'

@app.route("/hola")
def hola():
    return '<h1>modulo 2</h1>'

@app.route("/user/<string:user>")
def user(user):
    return f'<h1>Hola, {user}</h1>'

@app.route("/numero/<int:n>")
def numero(n):
    return f'<h1>Tienes:, ${n}</h1>'

if __name__ == '__main__':
    app.run(debug=True)