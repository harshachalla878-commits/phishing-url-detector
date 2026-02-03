from flask import Flask, render_template, request
import re

app = Flask(__name__)

def analyze_url(url):
    score = 0
    reasons = []

    if len(url) > 75:
        score += 2
        reasons.append("URL is too long")

    if not url.startswith("https"):
        score += 1
        reasons.append("No HTTPS security")

    if "@" in url:
        score += 3
        reasons.append("Contains @ symbol")

    if re.search(r"\d+\.\d+\.\d+\.\d+", url):
        score += 3
        reasons.append("Uses IP address instead of domain")

    if "-" in url:
        score += 1
        reasons.append("Contains hyphen in domain")

    if score <= 1:
        result = "Safe"
        color = "green"
    elif score <= 4:
        result = "Suspicious"
        color = "orange"
    else:
        result = "Phishing"
        color = "red"

    return result, score, reasons, color

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        url = request.form["url"]
        result, score, reasons, color = analyze_url(url)
        return render_template(
            "index.html",
            url=url,
            result=result,
            score=score,
            reasons=reasons,
            color=color
        )
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)