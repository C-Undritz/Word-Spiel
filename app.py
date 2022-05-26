import os
from flask import (
    Flask, render_template,
    redirect, request, session, url_for)
from game_logic import (
    generate_word, determine_results,
    validate_word, determine_win)
if os.path.exists("env.py"):
    import env


app = Flask(__name__)
STARTED = False


@app.route("/")
@app.route("/home")
def home():
    """
    Displays the start screen 
    """
    generate_word()

    return render_template("index.html")


@app.route("/games_screen", methods=["GET", "POST"])
def start_game():
    """
    Processes the submitted word per guess
    """
    global STARTED
    
    i = 1
    answer = ""
    if request.method == "POST":
        while i <= 5:
            answer += request.form.get("char-"+str(i)).lower()
            i += 1

        print(answer)
        valid_word = validate_word(answer)

        if valid_word:
            results = determine_results(answer)
            win = determine_win(answer)
            STARTED = True

            return render_template("game_screen.html",
                                   results=results,
                                   valid=valid_word,
                                   win=win,
                                   started=STARTED)
        else:
            if STARTED:  # If word is not valid but beyond round 1 (STARTED = True)
                results = determine_results(answer)
                win = determine_win(answer)
                STARTED = True
                return render_template("game_screen.html",
                                       results=results,
                                       valid=valid_word,
                                       win=win,
                                       started=STARTED)
            else:  # If word is not valid but only on round 1 (STARTED = False)
                win = determine_win(answer)
                return render_template("game_screen.html",
                                       valid=valid_word,
                                       win=win,
                                       started=STARTED)

    return render_template("game_screen.html", STARTED=STARTED)


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
