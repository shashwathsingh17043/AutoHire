from flask import Flask, request, render_template
from app.parser import extract_skills
from app.scorer import calculate_score

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    score = None

    if request.method == "POST":
        resume_text = request.form["resume"]
        found_skills = extract_skills(resume_text)

        required_skills = ["python", "sql", "django"]
        score = calculate_score(found_skills, required_skills)

    return render_template("index.html", score=score)

if __name__ == "__main__":
    app.run(debug=True)