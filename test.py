from flask import make_response, request
import json
from flask import Flask, redirect

# trying to trigger https://next.sonarqube.com/sonarqube/coding_rules?languages=py&types=VULNERABILITY&open=pythonsecurity%3AS5131

@app.route('/xss')
def index():
    json = json.dumps({ "data": request.args.get("input") })
    return make_response(json)


# same as above, trying a different bit of code

@app.route('/xss2')
def index():
    return make_response(request.args.get("input"))


# trying to trigger https://next.sonarqube.com/sonarqube/coding_rules?open=pythonsecurity:S5334&rule_key=pythonsecurity:S5334

@app.route("/")
def example():
    operation = request.args.get("operation")
    eval(f"product_{operation}()") # Noncompliant
    return "OK"

@app.route("/2")
def example2():
    operation = request.args.get("operation")
    eval(f"product_{operation}()") # Noncompliant
    return "OK"

@app.route("/3")
def example3():
    allowed = ["add", "remove", "update"]
    operation = allowed[request.args.get("operationId")]
    eval(f"product_{operation}()")
    return "OK"


@app.route("/4")
def example4():
    operation = request.args.get("operation")
    eval(f"product_{operation}()") # Noncompliant
    return "OK"

# trying to trigger https://next.sonarqube.com/sonarqube/coding_rules?languages=py&types=VULNERABILITY&open=pythonsecurity%3AS5146
# removed use of 'Flask' to try to avoid it triggering a hotspot instead
# changed function name and API endpoint to not be 'redirect' so that it didn't collide with the import of 'redirect'

@app.route("/redirecting")
def redirecting():
    url = request.args["url"]
    return redirect(url) # Noncompliant


a = 10
b =+ a

