from flask import Flask, render_template, url_for, request, jsonify, redirect
from methods.linear_search import linear_search
from random import sample

app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        firstSeek  = request.form['Submit']
        print(firstSeek)
    return render_template("index.html")

@app.route('/data', methods=['POST', 'GET'])
def data():
    data = {
        'first': request.form['primeiraBusca'], 
        'second': request.form['segundaBusca']
    }
    print(data['first'])

    return render_template("index.html", data=data)
    #return redirect(url_for('index'))

@app.route('/ajax', methods=['POST', 'GET'])
def ajax():
    return jsonify({'results' : sample(range(1, 10), 5)})

if __name__ == '__main__':
    app.run(debug=True)