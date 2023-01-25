from flask import Flask, render_template

# create a flask app
app = Flask(__name__)


# make a route to index.html
@app.route('/')
def page():
    return render_template('index.html')


# run on main
if __name__ == '__main__':
    app.run(debug=True, threaded=True, port=5000)
