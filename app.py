from flask import Flask, request, jsonify, render_template
from pyngrok import ngrok

app = Flask(__name__)

# 🧠 AI Logic
def diagnose_problem(problem):
    problem = problem.lower()

    if "no output" in problem or "not working" in problem:
        return {
            "diagnosis": "No Output",
            "causes": ["Power issue", "Loose wiring", "Faulty component"],
            "solution": "Check power supply"
        }

    elif "clipping" in problem or "distortion" in problem:
        return {
            "diagnosis": "Output Clipping",
            "causes": ["High input", "Low voltage"],
            "solution": "Reduce input signal"
        }

    elif "ripple" in problem or "fluctuating" in problem:
        return {
            "diagnosis": "High Ripple",
            "causes": ["Low capacitor", "Bad capacitor"],
            "solution": "Increase capacitor value"
        }

    elif "diode" in problem or "rectifier" in problem:
        return {
            "diagnosis": "Rectifier Issue",
            "causes": ["Wrong diode direction", "Damaged diode"],
            "solution": "Check diode orientation"
        }

    else:
        return {
            "diagnosis": "Unknown Issue",
            "causes": ["Not in database"],
            "solution": "Try another description"
        }

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/diagnose", methods=["POST"])
def diagnose():
    data = request.json
    problem = data.get("problem", "")
    return jsonify(diagnose_problem(problem))

# 🚀 RUN + NGROK
if __name__ == "__main__":
    public_url = ngrok.connect(5000)
    print("🔥 Public URL:", public_url)

    app.run()