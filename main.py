# import "packages" from flask
from flask import Flask, render_template, request

# create a Flask instance
app = Flask(__name__)


# connects default URL to render index.html
@app.route('/')
def index():
    return render_template("index.html")


# connects /kangaroos path to render kangaroos.html
@app.route('/kangaroos/')
def kangaroos():
    return render_template("kangaroos.html")


@app.route('/walruses/')
def walruses():
    return render_template("walruses.html")


@app.route('/hawkers/')
def hawkers():
    return render_template("hawkers.html")


@app.route('/stub/')
def noah():
    return render_template("stub.html")

@app.route('/noah/')
def var():
    return render_template("noah.html")

@app.route('/aryan/')
def aryan():
    return render_template("aryan.html")

@app.route('/tanay/')
def tanay():
    return render_template("tanay.html")

@app.route('/lucas/')
def lucas():
    return render_template("lucas.html")

@app.route('/greetNoah', methods=['GET', 'POST'])
def greet():
    # submit button has been pushed
    if request.form:
        name = request.form.get("name")
        if len(name) != 0:  # input field has content
            return render_template("greetNoah.html", name=name)
    # starting and empty input default
    return render_template("greetNoah.html", name="World")

if __name__ == "__main__":
    app.run(debug=True, port="5001")