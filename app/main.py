from flask import Flask, request, render_template
import pdfplumber
from app.parser import extract_skills
from app.scorer import calculate_score

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    score = None

    if request.method == "POST":

        if "resume_file" in request.files:
            file = request.files["resume_file"]

            if file.filename != "":
                with pdfplumber.open(file) as pdf:
                    text = ""
                    for page in pdf.pages:
                        text += page.extract_text()

                found_skills = extract_skills(text)

                required_skills = ["python", "sql", "django"]
                score = calculate_score(found_skills, required_skills)

    return render_template("index.html", score=score)

if __name__ == "__main__":
    app.run(debug=True)