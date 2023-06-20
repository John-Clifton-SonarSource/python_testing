from flask import make_response, request
import json
from flask import Flask, redirect

app = Flask(__name__)

# trying to trigger https://next.sonarqube.com/sonarqube/coding_rules?languages=py&types=VULNERABILITY&open=pythonsecurity%3AS5131 - didn't work

@app.route('/xss')
def index():
    json = json.dumps({ "data": request.args.get("input") })
    return make_response(json)


# same as above, trying a different bit of code

@app.route('/xss2')
def index2():
    return make_response(request.args.get("input"))


# trying to trigger https://next.sonarqube.com/sonarqube/coding_rules?open=pythonsecurity:S5334&rule_key=pythonsecurity:S5334 - worked

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

# trying to trigger https://next.sonarqube.com/sonarqube/coding_rules?languages=py&types=VULNERABILITY&open=pythonsecurity%3AS5146 - didn't work
# removed use of 'Flask' to try to avoid it triggering a hotspot instead - raised dogfooding on this
# changed function name and API endpoint to not be 'redirect' so that it didn't collide with the import of 'redirect' - raised PR to fix this

@app.route("/redirecting_orig")

def redirecting_orig():
    url = request.args["url"]
    return redirect(url) # Noncompliant

@app.route("/redirecting2")

def redirecting2():
    url = request.args["url"]
    return redirect(url_for(url))



# trying to trigger https://next.sonarqube.com/sonarqube/coding_rules?languages=py&types=VULNERABILITY&open=pythonsecurity%3AS3649

@app.route('/example')
def get_users():
    user = request.args["user"]
    sql = """SELECT user FROM users WHERE user = \'%s\'"""

    conn = sqlite3.connect('example')
    conn.cursor().execute(sql % (user)) # Noncompliant

a = 10
b =+ a

