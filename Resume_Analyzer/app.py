import os
from flask import Flask, render_template, request
from skill_extractor import extract_skills
from missing_skills import find_missing_skills
from recommender import recommend_skills
from similarity_engine import ai_similarity_score
from weighted_scorer import weighted_skill_scorer
import pdfplumber

app = Flask(__name__)

# ---------- Base folder & job description ----------
BASE_DIR = os.path.dirname(__file__)
JOB_DESC_FILE = os.path.join(BASE_DIR, "data", "job_description.txt")


# ---------- Function to read TXT or PDF resume ----------
def read_resume(file_path):
    """
    Reads resume text from TXT or PDF file
    """
    if file_path.endswith(".txt"):
        with open(file_path, "r", encoding="utf-8") as f:
            return f.read()
    elif file_path.endswith(".pdf"):
        text = ""
        with pdfplumber.open(file_path) as pdf:
            for page in pdf.pages:
                page_text = page.extract_text()
                if page_text:
                    text += page_text + "\n"
        return text
    else:
        return ""


# ---------- Flask Route ----------
@app.route("/", methods=["GET", "POST"])
def index():
    result = {}
    if request.method == "POST":
        uploaded_file = request.files.get("resume")
        if uploaded_file:
            file_path = os.path.join(BASE_DIR, "data", uploaded_file.filename)
            uploaded_file.save(file_path)

            # Read resume text
            resume_text = read_resume(file_path).lower()

            # Extract skills
            skills_found = extract_skills(resume_text)

            # Calculate scores
            weighted_score = weighted_skill_scorer(skills_found)
            ai_score = ai_similarity_score(resume_text, JOB_DESC_FILE)

            # Find missing skills
            missing = find_missing_skills(skills_found)

            # Generate recommendations
            recommendations = recommend_skills(missing)

            # Prepare results
            result = {
                "resume_text": resume_text,
                "skills_found": skills_found,
                "weighted_score": round(weighted_score, 2),
                "ai_score": round(ai_score, 2),
                "missing_skills": missing,
                "recommendations": recommendations,
            }

    return render_template("index.html", result=result)


# ---------- Run Flask App ----------
if __name__ == "__main__":
    app.run(debug=True)

