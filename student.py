from file_manager import save_data, load_data

def student_profile():
    print("\n===== STUDENT PROFILE =====")

    name = input("Enter your name: ")
    roll_number = input("Enter your roll number: ")
    branch = input("Enter your branch: ")
    year = input("Enter your year: ")

    data = name + "," + roll_number + "," + branch + "," + year
    save_data("student.txt", data)

    print("\n===== PROFILE =====")
    print("Name:", name)
    print("Roll Number:", roll_number)
    print("Branch:", branch)
    print("Year:", year)
    print("Profile saved successfully!")