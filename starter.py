import requests
from flask import Blueprint, render_template
from algorithm.image import image_data
from PIL import Image

from pathlib import \
    Path  # https://medium.com/@ageitgey/python-3-quick-tip-the-easy-way-to-deal-with-file-paths-on-windows-mac-and-linux-11a072b58d5f

app_starter = Blueprint('starter', __name__,
                        url_prefix='/starter',
                        template_folder='templates',
                        static_folder='static',
                        static_url_path='assets')


@app_starter.route('/binary/')
def binary():
    return render_template("starter/binary.html")


@app_starter.route('/rgb/')
def rgb():
    path = Path(app_starter.root_path) / "static" / "img"
    return render_template('starter/rgb.html', images=image_data(path))


@app_starter.route('/joke', methods=['GET', 'POST'])
def joke():
    """
    # use this url to test on and make modification on you own machine
    url = "http://127.0.0.1:5222/api/joke"
    """
    url = "https://csp.nighthawkcodingsociety.com/api/joke"
    response = requests.request("GET", url)
    return render_template("starter/joke.html", joke=response.json())


@app_starter.route('/jokes', methods=['GET', 'POST'])
def jokes():
    """
    # use this url to test on and make modification on you own machine
    url = "http://127.0.0.1:5222/api/jokes"
    """
    url = "https://csp.nighthawkcodingsociety.com/api/jokes"

    response = requests.request("GET", url)
    return render_template("starter/jokes.html", jokes=response.json())


@app_starter.route('/covid19', methods=['GET', 'POST'])
def covid19():
    url = "https://corona-virus-world-and-india-data.p.rapidapi.com/api"
    headers = {
        'x-rapidapi-key': "dec069b877msh0d9d0827664078cp1a18fajsn2afac35ae063",
        'x-rapidapi-host': "corona-virus-world-and-india-data.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers)

    """
    # uncomment this code to test from terminal
    world = response.json().get('world_total')
    countries = response.json().get('countries_stat')
    print(world['total_cases'])
    for country in countries:
        print(country["country_name"])
    """

    return render_template("starter/covid19.html", stats=response.json())

@app_starter.route('/nbaapi', methods=['GET', 'POST'])
def nbaapi():
    url = "https://free-nba.p.rapidapi.com/players"

    querystring = {"page":"0","per_page":"25"}

    headers = {
    'x-rapidapi-host': "free-nba.p.rapidapi.com",
    'x-rapidapi-key': "93746869c3msh83c9cc7d1d2ed0ap1ee0aajsnac6643923a7b"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    print(response.text)