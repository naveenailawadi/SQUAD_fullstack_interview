from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
def hello():
    print('insert code here')


@app.route("/data/<i>")
def data(i):
    try:
        i = int(i)

        if i == 1:
            message = "Data 1"
        elif i == 2:
            message = "Data 2"
        elif i == 3:
            message = "Data 3"
        else:
            message = "Invalid index"
    except TypeError:
        message = "Invalid Data Type"

    return jsonify({'message': message})


if __name__ == '__main__':
    app.run(debug=True, port=5001)
