from flask import Flask, render_template, url_for, request, jsonify, redirect, json
from methods.linear_search import linear_search
from random import sample

app = Flask(__name__)

def parameters(method):
    if method == 'Linear':
        array = [1, 2, 3, 4, 7, 8]
        counter = linear_search(array, 7)
        print(counter)

@app.route('/', methods=['POST', 'GET'])
def index():

    value = [12, 1, 11, 1, 2, 4]

    if request.method == 'POST':
        forms = {
            'first': request.form['primeiraBusca'], 
            'second': request.form['segundaBusca']
        }

        print(forms['first'])
        searchMeth = forms['first']

        return render_template("index.html", value=json.dumps(value), searchMeth=searchMeth)
    
    return render_template("index.html", value=json.dumps(value))

#ed2

@app.route('/ajax', methods=['POST', 'GET'])
def ajax():
    return jsonify({'results' : sample(range(1, 10), 5)})


if __name__ == '__main__':
    app.run(debug=True)