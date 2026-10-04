def process_student(name, marks):
    total = sum(marks)
    average = total / len(marks)
    
    if average >= 80:
        grade = "A"
    elif average >= 70:
        grade = "B"
    elif average >= 60:
        grade = "C"
    else:
        grade = "F"

    print(name, total, average, grade)
    
    with open("student_results.txt", "a") as file:
        file.write(f"{name}, {grade}\n")
        
    return grade