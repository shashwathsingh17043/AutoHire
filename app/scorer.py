def calculate_score(found_skills, required_skills):

    if not required_skills:
        return 0

    match_count = 0
    missing_skills = []

    for skill in required_skills:
        if skill in found_skills:
            match_count += 1
        else:
            missing_skills.append(skill)

    score = (match_count / len(required_skills)) * 100
    return round(score, 2)