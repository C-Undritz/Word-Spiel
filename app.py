import os
from flask import (
    Flask, render_template,
    redirect, request, session, url_for)
from game_logic import (
    generate_word, determine_results,
    validate_word)
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
    i = 1
    answer = ""
    global STARTED

    if request.method == "POST":
        while i <= 5:
            answer += request.form.get("char-"+str(i)).lower()
            i += 1

        print(answer)

        if validate_word(answer):
            results = determine_results(answer)
            STARTED = True
            print('result', str(results))
            return render_template("game_screen.html", STARTED=STARTED, results=results)
        else:
            print("That is not word you FOOL!!!")

        return redirect(url_for("start_game"))

    return render_template("game_screen.html", STARTED=STARTED)


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
