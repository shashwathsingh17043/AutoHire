from flask import Flask, render_template, request
import pdfplumber
from app.parser import extract_skills
from app.scorer import calculate_score

app = Flask(__name__)

def hiring_decision(score):
    if score >= 70:
        return "✅ Shortlisted"
    elif score >= 40:
        return "⚠ Review"
    else:
        return "❌ Rejected"

@app.route("/", methods=["GET", "POST"])
def index():
    candidates = []

    if request.method == "POST":
        files = request.files.getlist("resumes")

        for idx, file in enumerate(files, start=1):
            text = ""

            with pdfplumber.open(file) as pdf:
                for page in pdf.pages:
                    page_text = page.extract_text()
                    if page_text:
                        text += page_text

            skills = extract_skills(text.lower())
            score = calculate_score(skills, ["python", "sql", "django"])
            decision = hiring_decision(score)

            candidates.append({
                "name": file.filename,
                "score": score,
                "skills": skills,
                "decision": decision
            })

        candidates = sorted(candidates, key=lambda x: x["score"], reverse=True)

    return render_template("index.html", candidates=candidates)

if __name__ == "__main__":
    app.run(debug=True)