from flask import Flask, render_template, request
from utils.rag_engine import generate_blueprint

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        idea = request.form["idea"]
        result = generate_blueprint(idea)
        return render_template("result.html", result=result, idea=idea)
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
