from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/show', methods=['POST'])
def show():

    data = {
        'name': request.form['name'],
        'email': request.form['email'],
    }

    return render_template('show.html', user=data)

@app.route('/list', methods=['GET', 'POST'])
def list():
    if request.method == 'POST':
        data = {
            'name': request.form['name'],
            'email': request.form['email'],
        }

        return render_template('list.html', user=data)

    data = {
        'name': 'Sem nome',
        'email': 'Sem e-mail',
    }
    return render_template('list.html', user=data)

if __name__ == '__main__':
    app.run()
