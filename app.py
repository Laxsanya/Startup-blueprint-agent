from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    idea = request.form['idea'].strip()

    # 🧠 Generate a semi-dynamic blueprint using formatting logic
    blueprint = {
        "summary": f"This startup focuses on solving problems related to '{idea}', offering innovative, user-centric digital solutions.",
        "tech_stack": f"A modern stack suited for '{idea}' including Python (Flask), JavaScript (React), MongoDB, and RESTful APIs.",
        "audience": f"Individuals, businesses, or communities affected by or involved in '{idea}' sector.",
        "monetization": f"Revenue can be generated via subscriptions, freemium features, ads, or partnerships relevant to '{idea}'.",
        "launch_steps": [
            f"1. Research the specific needs in '{idea}' space.",
            f"2. Design a Minimum Viable Product tailored for '{idea}' users.",
            f"3. Build a prototype with essential features for '{idea}'.",
            f"4. Test with a small group of real users in '{idea}' area.",
            f"5. Launch public beta and gather feedback.",
            f"6. Iterate, scale, and expand based on response in '{idea}' domain."
        ]
    }

    return render_template('index.html', idea=idea, blueprint=blueprint)

if __name__ == '__main__':
    app.run()
