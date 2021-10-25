import random

from flask import Blueprint, jsonify

api_bp = Blueprint('api', __name__,
                   url_prefix='/api',
                   template_folder='templates',
                   static_folder='static', static_url_path='API/TanayAPI')

x = "jokes"
y = "tanay"
z = 5
print(x + y + z)

sports = []
sports_list = [
    'My favorite sport to play is soccer'
    'Why would you not want to play basketball'
    'Swimming requires the most athleticism'
]

def_sports

if __name__ == "__main__":
    print(random.choice(sports_list))