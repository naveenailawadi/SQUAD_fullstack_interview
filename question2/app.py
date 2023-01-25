from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def hello():
    print('insert code here')

if __name__ == '__main__':
    app.run(debug=True)