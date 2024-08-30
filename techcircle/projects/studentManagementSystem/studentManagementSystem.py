import json

filePath = "studentDB.json"

subjects = ["Mathematics", "English", "Biology", "Physics", "Chemistry"]

def getAllStudents():
    try:
        with open(filePath, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

def saveStudents(students):
    with open(filePath, "w") as file:
        json.dump(students, file, indent=4)

def determinePassFail(scores):
    return "Pass" if scores >= 50 else "Fail"

def calculateAverage(totalScore, numOfSubjects):
    return totalScore / numOfSubjects

def getSubjectsInfo(subjects):
    subject_details = {}
    totalScore = 0
    for subject in subjects:
        score = int(input(f"Score for {subject}: "))
        totalScore += score
        grade = getGrade(score)
        subject_details[subject] = {"score": score, "grade": grade}
    
    return subject_details, totalScore

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

def addStudent(name, totalScore, subject_details, age, level):
    students = getAllStudents()
    average = calculateAverage(totalScore, len(subject_details))
    grade = getGrade(totalScore)
    students[name] = {"subjects": subject_details, "average": average, "grades": grade, "age": age, "class" : level}
    saveStudents(students)
    print(f"{name} added successfully")

def deleteStudent(name):
    students = getAllStudents()
    if name in students:
        del students[name]
        saveStudents(students)
        print(f"{name} deleted successfully")
    else:
        print(f"No records found for {name}")

def viewAllStudents():
    students = getAllStudents()
    if students:
        print("\n-- Student List --")
        for name, details in students.items():
            status = determinePassFail(details["average"])
            print(f"Name: {name}")
            print(f"Average: {details['average']:.2f}")
            print(f"Status: {status}")
            print("Subjects:")
            for subject, subDetails in details["subjects"].items():
                print(f"  {subject}: {subDetails['score']} ({subDetails['grade']})")
            print("-" * 20)
    else:
        print("No Students Found")

def findStudent(name):
    students = getAllStudents()
    for student_name, details in students.items():
        if student_name.lower() == name.lower():
            print(f"\nName: {student_name}")
            print(f"Average: {details['average']:.2f}")
            print("Subjects:")
            for subject, subDetails in details["subjects"].items():
                print(f"  {subject}: {subDetails['score']} ({subDetails['grade']})")
            status = determinePassFail(details["average"])
            print(f"Status: {status}")
            return
    print(f"No records found for {name}")


def modifyStudent(name):
    students = getAllStudents()
    findStudent(name)
    print("1. modify name")
    print("2. modify grade")
    print("3. modify average")
    print("4. modify age")
    print("5. modify class")
    print("6. sibject information")

while True:
    print("\n-- StudentDB Menu --\n")
    print("1. Add Student")
    print("2. View All Students")
    print("3. Search for a Student")
    print("4. modify a Student")
    print("5. Delete a Student")
    print("6. Quit")

    choice = input("Choose an option (1 - 6 ): ")

    if choice == "1":
        name = input("Enter name: ")
        age = int(input("Enter age: "))
        level = input("Enter class: ")
        subject_details, totalScore = getSubjectsInfo(subjects)
        addStudent(name, totalScore, subject_details, age, level)

    elif choice == "2":
        viewAllStudents()
    elif choice == "3":
        name = input("Enter name: ")
        findStudent(name)
    elif choice == "4":
        print("Feature not yet available")
    elif choice == "5":
        name = input("Enter a name: ")
        cho = input(f"Are you sure you want to delete {name}: ")
        if cho.lower() == "y" or cho.lower() == "yes":
            deleteStudent(name)
    elif choice == "6":
        print("Goodbye!")
        break
    else:
        print("invalid operation number")
