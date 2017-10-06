from flask import Flask

app = Flask(__name__)

@app.route("/", endpoint='func1')
def hello_world():
    return "Hello_world"

@app.route("/path", endpoint='func2')
def func2():
    return "Hello"

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=8080)
