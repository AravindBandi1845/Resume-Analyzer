import os
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def ai_similarity_score(resume_text, job_desc_path):
    if not os.path.exists(job_desc_path):
        raise FileNotFoundError("Job description file not found")

    with open(job_desc_path, "r", encoding="utf-8") as file:
        job_text = file.read().lower()

    documents = [resume_text.lower(), job_text]

    vectorizer = TfidfVectorizer()
    tfidf = vectorizer.fit_transform(documents)

    similarity = cosine_similarity(tfidf[0:1], tfidf[1:2])[0][0]
    return similarity * 100

