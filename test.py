# trying to trigger https://next.sonarqube.com/sonarqube/coding_rules?open=pythonsecurity:S5334&rule_key=pythonsecurity:S5334

from flask import request

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

a = 10
b =+ a

# trying to trigger https://next.sonarqube.com/sonarqube/coding_rules?languages=py&types=VULNERABILITY&open=pythonsecurity%3AS5131

from flask import make_response, request
import json

@app.route('/xss')
def index():
    json = json.dumps({ "data": request.args.get("input") })
    return make_response(json)