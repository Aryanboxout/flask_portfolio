import random

from flask import Blueprint, jsonify

api_bp = Blueprint('api', __name__,
                   url_prefix='/api',
                   template_folder='templates',
                   static_folder='static', static_url_path='static/api')


teams = []
team_list = [
    "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQio7RCBFR3l_x48kALmhFK67116XzfvEFGCg&usqp=CAU Barcelona League: La Liga 9th place Star player: Dembele, Depay ",
    "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSD_83DiNBeGqbO0xMxXUrh_NINQ-LADO1fXw&usqp=CAU Real Madrid Star Player: Vinicius jr",
    " https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRiN5fPIaAZQyS3nNBMP3DWDGMVUT3kXDsWJw&usqp=CAU Manchester United Star player:CR7",
    " https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRyeOawtIkf56Ph4TEaLgtcxnndh4Z0DRrt1A&usqp=CAU Juventus League: Serie A 9th place Star Players: Chiesa, Cuadrado, Costa",
    " https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSpED0Bco9ySG5GBIVgPllbjyebuiOQARufOg&usqp=CAU Paris Saint German League: Ligue 1 first place Star Players: Messi, Neymar, Mbappe",

]

def _find_next_id():
    return max(team["id"] for team in teams) + 1

def _init_team():
    id = 1
    for team in team_list:
        teams.append({"id": id, "team": team, "haha": 0, "boohoo": 0})
        id += 1
    print(teams)

@api_bp.route('/team/')
def get_team():
    if len(teams) == 0:
        _init_team()
    return jsonify(random.choice(team_list))

if __name__ == "__main__":
    print(random.choice(team_list))