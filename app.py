from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    return render_template("index.html")


if __name__ == "__main__":
    # Listen on all interfaces so the devcontainer / host can reach it
    app.run(host="0.0.0.0", port=9000, debug=True)

