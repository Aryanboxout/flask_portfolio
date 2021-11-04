# import "packages" from flask
from flask import Flask, render_template, request
from API.teamsapi import api_bp
from API.athletesapi import api_bp

import requests
import json
# create a Flask instance
from image import image_data


app = Flask(__name__)
app.register_blueprint(api_bp)



# connects default URL to render index.html
@app.route('/')
def index():
    return render_template("index.html")

@app.route('/historypage')
def historypage():
    return render_template("historypage.html")

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

@app.route('/sportsinfo/')
def sportsinfo():
    return render_template("sportsinfo.html")

@app.route('/basketball/')
def basketball():
    return render_template("basketball.html")

@app.route('/KobeTribute/')
def KobeTribute():
    return render_template("KobeTribute.html")

@app.route('/football/')
def football():
    return render_template("football.html")

@app.route('/soccer/')
def soccer():
    return render_template("soccer.html")

@app.route('/baseball/')
def baseball():
    return render_template("baseball.html")

@app.route('/sportsdata/')
def sportsdata():
    return render_template("sportsdata.html")

@app.route('/movie/')
def movie():
    return render_template("movie.html")

@app.route('/joke/')
def joke():
    return render_template("joke.html")

@app.route('/calculator/')
def calculator():
    return render_template("calculator.html")

@app.route('/rockpaperscissors/')
def rockpaperscissors():
    return render_template("rockpaperscissors.html")

@app.route('/tipcalculator/')
def tipcalculator():
    return render_template("tipcalculator.html")

@app.route('/RandomTeamGenerator/')
def RandomTeamGenerator():
    return render_template("RandomTeamGenerator.html")

@app.route('/googleform/')
def googleform():
    return render_template("googleform.html")

@app.route('/photoedit/')
def photoedit():
    return render_template("photoedit.html")

@app.route('/imagemanipulation/')
def imagemanipulation():
    return render_template("imagemanipulation.html")

@app.route('/NBAPI/')
def NBAPI():
    return render_template("NBAPI.html")
import requests




@app.route('/portal/')
def portal():
    url = "https://coinranking1.p.rapidapi.com/stats"

    headers = {
        'x-rapidapi-host': "coinranking1.p.rapidapi.com",
        'x-rapidapi-key': "a53d1a4acemsh90db192dc27d5f7p1028a2jsn2e483944f85c"
    }

    response = requests.request("GET", url, headers=headers)
    output=json.loads(response.text)
    return render_template("portal.html",data=output)

@app.route('/searchbar/')
def searchbar():
    return render_template("searchbar.html")

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

@app.route('/team/', methods=['GET', 'POST'])
def team():
    url = "http://127.0.0.1:5000/api/team"

    response = requests.request("GET", url)
    return render_template("team.html", team=response.json())

@app.route('/athlete/', methods=['GET', 'POST'])
def athlete():
    url = "http://127.0.0.1:5000/api/athlete"

    response = requests.request("GET", url)
    return render_template("athlete.html", athlete=response.json())



if __name__ == "__main__":
    app.run(
        debug=True,
        host="127.0.0.1",
        port=5000
    ),