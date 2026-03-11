course_map = {
    "python": "Python for Everybody (Coursera)",
    "machine learning": "Machine Learning by Andrew Ng",
    "data analysis": "IBM Data Analyst Professional Certificate",
    "sql": "SQL for Data Science",
    "flask": "Flask Web Development",
    "aws": "AWS Cloud Practitioner"
}

def recommend_skills(missing_skills):
    recommendations = []
    for skill in missing_skills:
        course = course_map.get(skill, "Explore online resources")
        recommendations.append(f"{skill.title()} → {course}")
    return recommendations

