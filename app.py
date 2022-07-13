import os
from flask import (
    Flask, render_template,
    redirect, request, session, url_for)
from game.classes import Game
from game.game_logic import determine_results
if os.path.exists("env.py"):
    import env


app = Flask(__name__)
rapidapi_key = os.environ.get("RAPIDAPI_KEY")
game = Game(0, [], False)


@app.route("/")
@app.route("/home")
def home():
    """
    Displays the start screen.  Resets the instantiated Game class should the
    user quit to the start screen during a game.
    """
    game.reset()
    return render_template("index.html")


@app.route("/games_screen", methods=["GET", "POST"])
def start_game():
    """
    Processes the submitted answer against the word and updates required Game
    class attributes as required.
    """
    if request.method == "POST":
        answer = ""
        i = 1
        while i <= 5:
            answer += request.form.get("char-"+str(i)).lower()
            i += 1

        round_results = determine_results(game.word, answer)
        game.add_results(round_results)
        game.increment_count(1)
        game.determine_win(round_results.win)

        return render_template("game_screen.html", game=game)

    return render_template("game_screen.html", game=game)


@app.route("/play_again", methods=["GET", "POST"])
def play_again():
    '''
    Resets the game should the player select to play again and directs to the
    game screen.
    '''
    if request.method == "POST":
        game.reset()
        return redirect(url_for("start_game"))


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
