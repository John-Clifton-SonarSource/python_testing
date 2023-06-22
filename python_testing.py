import json
from flask import Flask, make_response, request
from flask_wtf import CSRFProtect
from django.http import HttpResponseRedirect

app = Flask(__name__)
csrf = CSRFProtect()
csrf.init_app(app)

def update_and_show_counter(counter):
    counter =+ 8
    print(counter)

counter = 10
update_and_show_counter(counter)

def complicated_code(text):
    a=1
    b=2
    c=3
    d=4

    if a in (a,b,c,d):
        return(c+input)
        if a < b:
            return(b+input)
            if c < d:
                return(d+input)
                if a < c:
                    return(a+input)
                    if a < d:
                        return(d)
                        if c < d:
                            return(a+input)
                            if a > b:
                                return(c)

    return 0

@app.route('/xss2')
def index2():
    
    return make_response(complicated_code(request.args.get("input")))

@app.route("/")
def example():
    operation = request.args.get("operation")
    eval(f"product_{operation}()") # Noncompliant
    return "OK"
