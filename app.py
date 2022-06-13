import os
import globals
from flask import (
    Flask, render_template,
    redirect, request, session, url_for)
from game_logic import (
    determine_results,
    validate_word, determine_win)
from classes import Game
if os.path.exists("env.py"):
    import env


app = Flask(__name__)
rapidapi_key = os.environ.get("RAPIDAPI_KEY")


@app.route("/")
@app.route("/home")
def home():
    """
    Displays the start screen 
    """
    return render_template("index.html")


@app.route("/games_screen", methods=["GET", "POST"])
def start_game():
    """
    Processes the submitted word per guess
    """
    game = Game(1, [])
    game.show(33)
    if request.method == "POST":
        answer = ""
        i = 1
        while i <= 5:
            answer += request.form.get("char-"+str(i)).lower()
            i += 1

        print("app.py, line 38.  Player answer is :", answer)
        game.show(42)
        round_results = determine_results(game.word, answer)
        print("app.py, line 41.  Current_round results: ", str(round_results))
        print(round_results.current_results)
        game.show(46)
        return render_template("game_screen.html")

    return render_template("game_screen.html")


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
