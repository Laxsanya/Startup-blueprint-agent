@app.route('/generate', methods=['POST'])
def generate():
    idea = request.form['idea']

    # mock blueprint logic
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
