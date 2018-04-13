from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def show():

    data = {
        'name': request.form['name'],
        'email': request.form['email'],
    }

    return render_template('show.html', data=data)
