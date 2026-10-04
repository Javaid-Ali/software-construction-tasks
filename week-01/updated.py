def calculate_result(marks):
    total = sum(marks)
    average = total / len(marks)
    return total, average

def check_grade(average):
    if average >= 80:
        return "A"
    elif average >= 70:
        return "B"
    elif average >= 60:
        return "C"
    return "F"

def present_result(name, total, average, grade):
    print(name, total, average, grade)
    with open("student_results.txt", "a") as file:
        file.write(f"{name}, {grade}\n")

def calculate_and_present_student(name, marks):
    total, average = calculate_result(marks)
    grade = check_grade(average)
    present_result(name, total, average, grade)
    return grade

if __name__ == "__main__":
    student_name = input("Enter student name: ")
    student_marks = [
        float(mark)
        for mark in input("Enter marks separated by spaces: ").split()
    ]
    calculate_and_present_student(student_name, student_marks)