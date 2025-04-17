from loguru import logger

def collect_student_data():
    student_info = {}

    while True:
        name = input("Enter student name: ").strip()

        if name in student_info:
            choice = input("Name already exists. Overwrite? (yes/no): ").strip().lower()
            if choice != 'yes':
                continue

        marks = []
        for i in range(1, 5):
            while True:
                try:
                    mark = int(input(f"Enter marks for Subject {i} (0-100): "))
                    if 0 <= mark <= 100:
                        marks.append(mark)
                        break
                    else:
                        logger.error("Marks should be between 0 and 100.")
                except ValueError:
                    logger.error("Invalid input. Please enter a number.")

        student_info[name] = marks

        more = input("Do you want to add another student? (yes/no): ").strip().lower()
        if more != "yes":
            break

    return student_info


# Call the function and store the result
students = collect_student_data()

print("\nFinal Student Records:")
for student, marks in students.items():
    print(f"{student}: {marks}")
