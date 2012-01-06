from flask import Flask, request, abort, render_template, make_response
from zipfy import Corpus
from json.encoder import JSONEncoder

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def hello_world():
    if request.method == 'POST':
        try:
            corpus = Corpus(request.form['url'])
        except:
            return "Hello, Post!" 

        e = JSONEncoder()
        resp = make_response(e.encode(corpus.freq_list))
        return resp
    elif request.method == 'GET':
        return render_template("index.html")

if __name__ == "__main__":
    app.run()
