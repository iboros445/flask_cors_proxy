from requests import get as requests_get
from flask import Flask, request, Response

app = Flask(__name__)

@app.route('/corsserver/<path:url>')
def proxy(url):
    data = requests_get(url, params=request.args).content
    resp = Response(data)
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp
  

app.run("127.0.0.1", 5000)
