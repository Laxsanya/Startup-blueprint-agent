from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])  # ← ✅ FIXED: Added methods=['POST']
def generate():
    idea = request.form['idea']

    blueprint = {
        "summary": f"This startup aims to solve problems in the domain of '{idea}'.",
        "tech_stack": "Python, Flask, MongoDB, React",
        "audience": "Young entrepreneurs, tech enthusiasts, startups",
        "monetization": "Freemium model, ads, premium features",
        "launch_steps": [
            "1. Research the market",
            "2. Build MVP",
            "3. Launch beta",
            "4. Collect feedback",
            "5. Scale"
        ]
    }

    return render_template('index.html', idea=idea, blueprint=blueprint)

if __name__ == "__main__":
    app.run()
