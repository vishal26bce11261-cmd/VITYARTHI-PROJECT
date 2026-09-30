import validation
from validation import valid_marks


def get_marks(subject):
    while True:
        try:
            marks = float(input(f"Enter {subject} marks (0-100): "))

            if 0 <= marks <= 100:
                return marks

            print("Invalid marks! Please enter marks between 0 and 100.")

        except ValueError:
            print("Invalid input! Please enter marks between 0 to 100.")


def marks_manager():
        maths = get_marks("maths")
        python = get_marks("python")
        english = get_marks("english")

        total = maths + python + english
        percentage = total / 3

        print("\n===== Result =====")
        print("Total marks:", total)
        print("Percentage:", percentage) 

        if percentage >= 90:
            print("Grade A+")
        elif percentage >= 80:
            print("Grade A")
        elif percentage >= 70:
            print("Grade B")
        elif percentage >= 60:
            print("Grade C")
        elif percentage >= 50:
            print("Grade D")
        else:
            print("Grade F")    
