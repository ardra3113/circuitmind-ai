from flask import Flask, render_template, request, jsonify
import os

app = Flask(__name__)

# 🏠 Home route
@app.route("/")
def home():
    return render_template("index.html")


# ⚡ Diagnose route
@app.route("/diagnose", methods=["POST"])
def diagnose():
    try:
        data = request.get_json()
        problem = data.get("problem", "").lower()

        # 🔍 Logic for different inputs

        # LED issues
        if "led" in problem:
            diagnosis = "LED not glowing properly"
            causes = [
                "Reverse polarity connection",
                "Resistor value too high",
                "LED damaged"
            ]
            solution = "Check polarity, use proper resistor (220Ω), replace LED if needed"

        # No output
        elif "no output" in problem:
            diagnosis = "No output detected"
            causes = [
                "Power supply issue",
                "Loose wiring",
                "Component failure"
            ]
            solution = "Check power supply and wiring connections"

        # Clipping
        elif "clipping" in problem:
            diagnosis = "Signal clipping detected"
            causes = [
                "Input signal too large",
                "Op-amp saturation",
                "Insufficient supply voltage"
            ]
            solution = "Reduce input amplitude or increase supply voltage"

        # Fluctuating signal / noise
        elif "fluctuating" in problem or "noise" in problem:
            diagnosis = "Unstable or noisy signal"
            causes = [
                "Loose connections",
                "Electrical interference",
                "Improper grounding"
            ]
            solution = "Secure connections and ensure proper grounding"

        # Diode issues
        elif "diode" in problem:
            diagnosis = "Diode not functioning properly"
            causes = [
                "Reverse bias connection",
                "Diode damaged",
                "Incorrect voltage applied"
            ]
            solution = "Check diode orientation and replace if faulty"

        # General fallback
        else:
            diagnosis = "General circuit issue detected"
            causes = [
                "Loose connections",
                "Incorrect component values",
                "Short circuit"
            ]
            solution = "Inspect circuit carefully and verify all components"

        return jsonify({
            "diagnosis": diagnosis,
            "causes": causes,
            "solution": solution
        })

    except Exception as e:
        return jsonify({
            "diagnosis": "Error occurred",
            "causes": [str(e)],
            "solution": "Check server logs"
        })


# 🚀 Run app (for Render deployment)
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 10000)))