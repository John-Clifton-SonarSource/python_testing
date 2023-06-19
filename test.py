# trying to trigger https://next.sonarqube.com/sonarqube/coding_rules?open=pythonsecurity:S5334&rule_key=pythonsecurity:S5334

from flask import request

@app.route("/")
def example():
    operation = request.args.get("operation")
    eval(f"product_{operation}()") # Noncompliant
    return "OK"

@app.route("/")
def example2():
    operation = request.args.get("operation")
    eval(f"product_{operation}()") # Noncompliant
    return "OK"


@app.route("/")
def example3():
    operation = request.args.get("operation")
    eval(f"product_{operation}()") # Noncompliant
    return "OK"

test_var = 5
print(test_var)
