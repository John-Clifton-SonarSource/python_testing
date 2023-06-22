import json
from flask import Flask, make_response, request
from flask_wtf import CSRFProtect
from django.http import HttpResponseRedirect

app = Flask(__name__)
csrf = CSRFProtect()
csrf.init_app(app)

counter = 10
counter =+ 8

print(counter)

@app.route('/xss2')
def index2():
    return make_response(request.args.get("input"))

def redirect_again():
    url = request.GET.get("url", "/testing_redirect")
    return HttpResponseRedirect(url)

def counter():

    current_total = 0

    if current_total + 11 <= 21:
        return 11
    else:
        return 1