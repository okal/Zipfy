import redis

from hashlib import sha1
from flask import Flask, request, abort, render_template, make_response
from zipfy import Corpus
from json.encoder import JSONEncoder

app = Flask(__name__)
app.debug = True
try:
    from bundle_config import config
    r = redis.Redis(
        host = config['redis']['host'],
        port = int(config['redis']['port']),
        db = 0,
        password = config['redis']['password']
    )
except:
    r = redis.StrictRedis(host='localhost', port=6379, db=0)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        site_hash = sha1(request.form['url']).hexdigest()
        zipf_profile = r.get(site_hash)
        if zipf_profile: 
            return zipf_profile
        else:
            try:
                corpus = Corpus(request.form['url'])
            except:
                return "Hello, Post!" 
        
        e = JSONEncoder()
        zipf_profile = e.encode(corpus.freq_list)
        r.set(site_hash, zipf_profile)
        resp = make_response(zipf_profile)
        return resp
    elif request.method == 'GET':
        return render_template("index.html")

#@app.route('/<site_hash>/')
#def from_slug(site_hash):
#    zipf_profile = r.get(site_hash)
#    if zipf_profile:
#        return render_template("index.html", zipf_profile=zipf_profile)
    
if __name__ == "__main__":
    app.run()
