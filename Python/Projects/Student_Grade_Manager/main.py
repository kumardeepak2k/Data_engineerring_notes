from loguru import logger

student_list = {}


def student_info():
    while True:
        stu_name = input("Enter the name of the student: ")
        if stu_name in student_list:
            user_input = input(f"Do you override the existing name {stu_name}(Yes/No).").strip().lower()
            if user_input == "no":
                continue

        marks = []
        for i in range(1,5):
            
            while True:
                try:
                    stu_marks = int(input(f"Enter marks for Subject {i}: "))
                    if stu_marks <= 0 or stu_marks <= 100:
                        marks.append(stu_marks)
                        break
                    else:
                        print("Marks should be between 0-100")   
                except ValueError:
                    logger.error("Invalid input. Enter marks ")

        student_list[stu_name] = marks

        user_con = input("Do you want to add another name(Yes/No): ").strip().lower()
        if user_con != "yes":
            break
    return student_list         



# Function to calculate total marks
def total_marks(marks):
    return sum(marks)

# Function to calculate average marks
def average_marks(marks):
    return sum(marks) / len(marks)

# Function to calculate grade
def calculate_grade(average):
    if average >= 90:
        return "A"
    elif average >= 75:
        return "B"
    elif average >= 60:
        return "C"
    else:
        return "D"

# Main code
print("Student Information")

# Get student data
data = student_info()

# Now, print each student info along with their arithmetic calculations
for name, marks in data.items():
    total = total_marks(marks)
    average = average_marks(marks)
    grade = calculate_grade(average)

    print(f"Name: {name}")
    print(f"Marks: {marks}")
    print(f"Total Marks: {total}")
    print(f"Average Marks: {average:.2f}")
    print(f"Grade: {grade}\n")