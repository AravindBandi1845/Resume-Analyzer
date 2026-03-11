import os

from skill_extractor import extract_skills
from missing_skills import find_missing_skills
from recommender import recommend_skills
from similarity_engine import ai_similarity_score
from weighted_scorer import weighted_skill_scorer


# ---------- File Paths ----------
BASE_DIR = os.path.dirname(__file__)

resume_file_path = os.path.join(BASE_DIR, "data", "sample_resume.txt")
job_desc_file_path = os.path.join(BASE_DIR, "data", "job_description.txt")


# ---------- Read Resume ----------
with open(resume_file_path, "r") as file:
    resume_text = file.read().lower()

print("\n=== Resume Text ===")
print(resume_text)


# ---------- Skill Extraction ----------
skills_found = extract_skills(resume_text)

print("\n=== Skills Found in Resume ===")
print(skills_found)


# ---------- Weighted Skill Score ----------
weighted_score = weighted_skill_scorer(skills_found)
print(f"\nWeighted Skill Score: {weighted_score:.2f}%")


# ---------- AI Similarity Score ----------
ai_score = ai_similarity_score(resume_text, job_desc_file_path)
print(f"AI Similarity Score: {ai_score:.2f}%")


# ---------- Missing Skills ----------
missing = find_missing_skills(skills_found)
print("\nMissing Skills:", missing)


# ---------- Recommendations ----------
recommendations = recommend_skills(missing)

print("\n=== Recommendations ===")
for rec in recommendations:
    print("-", rec)



