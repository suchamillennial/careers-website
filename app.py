from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
  return "Hello World"

  print(__name__)


# Code to have it run on the local development server
if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
