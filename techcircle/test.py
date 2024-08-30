subjects = ["Mathematics", "English", "Biology", "Physics", "Chemistry"]

def getGrade(score):
    if score >= 80:
        return "A1"
    elif score >= 65:
        return "B2"
    elif score >= 60:
        return "B3"
    elif score >= 55:
        return "C4"
    elif score >= 50:
        return "C6"
    elif score >= 45:
        return "D7"
    elif score >= 35:
        return "E8"
    else:
        return "F9"

def getSubjectsinfo(sub):
    subjects = {}
    totalScore = 0
    for subject in sub:
        score = int(input(f"Score for {subject}: "))
        totalScore += score
        grade = getGrade(score)
        subjects[subject] = {"score": score, "grade": grade}
    
    return subjects, totalScore


result, score = getSubjectsinfo(subjects)

print(result)

print(score)