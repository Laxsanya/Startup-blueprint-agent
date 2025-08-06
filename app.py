from flask import Flask, render_template
import random

app = Flask(__name__)

# Sample blueprint data
blueprints = [
    {
        "industry": "HealthTech",
        "idea": "An AI-powered virtual health assistant for chronic illness management.",
        "steps": [
            "Research patient pain points",
            "Design chatbot MVP",
            "Partner with local clinics"
        ]
    },
    {
        "industry": "EdTech",
        "idea": "A gamified mobile app that teaches coding to teenagers.",
        "steps": [
            "Build prototype with basic games",
            "Test with school students",
            "Apply for incubator funding"
        ]
    },
    {
        "industry": "AgriTech",
        "idea": "IoT-based smart irrigation systems for small farms.",
        "steps": [
            "Design low-cost sensors",
            "Pilot in rural areas",
            "Approach government schemes"
        ]
    }
]

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/generate")
def generate():
    result = random.choice(blueprints)
    return render_template("result.html", blueprint=result)

if __name__ == "__main__":
    app.run()
