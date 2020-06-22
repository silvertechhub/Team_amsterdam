from flask import Flask, render_template
import csv

app = Flask(__name__)
File = open("leaderboard.csv")
Reader = csv.reader(File)
Data = list(Reader)


@app.route("/")
@app.route("/ranking")
def index():
    scores = []
    for data in Data:
        scores.append((data[0], data[1], data[2], data[3]))
    scores.sort(key=lambda s: s[3], reverse=True)

    return render_template("ranking.html", scores=scores)


if __name__ == "__main__":
    app.run(debug=True)
