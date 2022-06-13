import os
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
game = Game(0, [])


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
    print(game.word)
    if request.method == "POST":
        answer = ""
        i = 1
        while i <= 5:
            answer += request.form.get("char-"+str(i)).lower()
            i += 1

        round_results = determine_results(game.word, answer)
        game.add_results(round_results)
        game.increment_count(1)
        print(game)
        return render_template("game_screen.html")

    return render_template("game_screen.html")


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
