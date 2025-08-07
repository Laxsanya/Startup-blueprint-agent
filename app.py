from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    idea = request.form['idea'].strip()

    blueprint = {
        "summary": f"This startup aims to solve challenges in the '{idea}' space using innovative and user-centric digital solutions. The goal is to simplify, automate, or enhance experiences related to '{idea}'.",
        "tech_stack": f"A scalable tech stack tailored for '{idea}', including Python (Flask) for backend, ReactJS for frontend, MongoDB for database, and REST APIs for communication.",
        "audience": f"Individuals, businesses, or communities that are actively involved in or affected by the '{idea}' domain.",
        "monetization": f"Revenue streams can include freemium services, premium subscriptions, in-app purchases, B2B licensing, or affiliate models — all tailored to the '{idea}' industry.",
        "launch_steps": [
            f"Conduct market research to identify key pain points in '{idea}'.",
            f"Define user personas and use cases for your '{idea}' solution.",
            f"Design a clean, minimal MVP focused on the core need.",
            f"Build backend and frontend using modern, scalable tools.",
            f"Launch a beta version and collect feedback.",
            f"Iterate, optimize, and go for a public launch!"
        ]
    }

    return render_template('index.html', idea=idea, blueprint=blueprint)

if __name__ == "__main__":
    app.run()
