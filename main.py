# import "packages" from flask
from flask import Flask, render_template, request

# create a Flask instance
from image import image_data

app = Flask(__name__)


# connects default URL to render index.html
@app.route('/')
def index():
    return render_template("index.html")

@app.route('/minilabs/')
def minilabs():
    return render_template("minilabs.html")

@app.route('/rgbNoah/')
def rgbNoah():
    return render_template("rgbNoah.html", images=image_data())


@app.route('/wireframes/')
def wireframes():
    return render_template("wireframes.html")

@app.route('/sprint/')
def sprint():
    return render_template("sprint.html")

@app.route('/brainWrite/')
def brainwrite():
    return render_template("brainWrite.html")

@app.route('/NoahTanayLucasJournal/')
def NoahTanayLucasJournal():
    return render_template("NoahTanayLucasJournal.html")

@app.route('/AryanPranavJournal/')
def AryanPranavJournal():
    return render_template("AryanPranavJournal.html")

@app.route('/binary/',methods=['GET','POST'])
def binary():
    BITS=12
    if request.method == 'POST':
        BITS = int(request.form['BITS'])
    return render_template("binary.html",BITS=BITS)

@app.route('/rgbNoah/')
def rgbTanay():
    return render_template("rgbNoah.html", images=image_data())

@app.route('/LogicGate/')
def LogicGate():
    return render_template("LogicGate.html")

@app.route('/UnsignedSignedAddition/')
def UnsignedSignedAddition():
    return render_template("UnsignedSignedAddition.html")

@app.route('/main/')
def main():
    return render_template("main.html")

@app.route('/Binarycolor/')
def Binarycolor():
    return render_template("Binarycolor.html")



@app.route('/greetNoah', methods=['GET', 'POST'])
def greetNoah():
    # submit button has been pushed
    if request.form:
        name = request.form.get("name")
        if len(name) != 0:  # input field has content
            return render_template("greetNoah.html", name=name)
    # starting and empty input default
    return render_template("greetNoah.html", name="World")

@app.route('/greetTanay', methods=['GET', 'POST'])
def greetTanay():
    # submit button has been pushed
    if request.form:
        name = request.form.get("name")
        if len(name) != 0:  # input field has content
            return render_template("greetTanay.html", name=name)
    # starting and empty input default
    return render_template("greetTanay.html", name="World")

@app.route('/greetAryan', methods=['GET', 'POST'])
def greetAryan():
    # submit button has been pushed
    if request.form:
        name = request.form.get("name")
        if len(name) != 0:  # input field has content
            return render_template("greetAryan.html", name=name)
    # starting and empty input default
    return render_template("greetAryan.html", name="World")

@app.route('/greetLucas', methods=['GET', 'POST'])
def greetLucas():
    # submit button has been pushed
    if request.form:
        name = request.form.get("name")
        if len(name) != 0:  # input field has content
            return render_template("greetLucas.html", name=name)
    # starting and empty input default
    return render_template("greetLucas.html", name="World")

@app.route('/greetPranav', methods=['GET', 'POST'])
def greetPranav():
    # submit button has been pushed
    if request.form:
        name = request.form.get("name")
        if len(name) != 0:  # input field has content
            return render_template("greetPranav.html", name=name)
    # starting and empty input default
    return render_template("greetPranav.html", name="World")

if __name__ == "__main__":
    app.run(debug=True)


