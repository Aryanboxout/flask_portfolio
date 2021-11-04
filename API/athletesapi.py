import random

from flask import Blueprint, jsonify

api_bp = Blueprint('api', __name__,
                   url_prefix='/api',
                   template_folder='templates',
                   static_folder='static', static_url_path='static/api')


athletes = []
athlete_list = [
    "https://encrypted-tbn0.gstatic.com/ima ges?q=tbn:ANd9GcRKOd7U1jo8apLY93dd2x1F78yfaxMo2ESvQQ&usqp=CAU",
    "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQyshgQryjxi1koI4wUR4Q4ztktW0-i3cRAAQ&usqp=CAU",
    "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSmIciWWxwtSO8e0dfKPL3V1jEitpvkko0Q8g&usqp=CAU",
    "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQEH6rxjLnL7BpD6EZsidIGO_uu74N60_fimg&usqp=CAU",
    "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRPPEELFC71AYl6OdFhoRipf0YWemKv28WotQ&usqp=CAU",
    "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQRqLbpHRP391yRt1VOLbA2H4ox1twjLp5goA&usqp=CAU",
    "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQII4DmYUgPYQrYWjdDqaeet5fTRzG-4uMvgA&usqp=CAU",
    "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRDhrysw3e3U-cIzJhkGXf4_ERzMmonTi-pEQ&usqp=CAU",
    "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSjo937imrmzS6Ukq_Mkl3jaYP-6CVhK8l2TA&usqp=CAU",
    "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSIV9ulS38YE0_OptSzgQzlQ5Eb7DsFDch9hw&usqp=CAU"
]

def _find_next_id():
    return max(athlete["id"] for athlete in athletes) + 1

def _init_athlete():
    id = 1
    for athlete in athlete_list:
        athletes.append({"id": id, "athlete": athlete, "haha": 0, "boohoo": 0})
        id += 1
    print(athletes)

@api_bp.route('/athlete/')
def get_athlete():
    if len(athletes) == 0:
        _init_athlete()
    return jsonify(random.choice(athlete_list))
    #return jsonify(athletes)

if __name__ == "__main__":
    print(random.choice(athlete_list))