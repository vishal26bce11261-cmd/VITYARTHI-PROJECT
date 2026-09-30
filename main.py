from student import student_profile
from marks2 import marks_manager
from attendance import attendance_manager
from tasks import task_manager
from calculation import average, percentage, maximun
from validation import valid_marks
print("========================================")
print("       STUDENT MANAGMENT SYSTEM")
print("========================================")

while True:
    print("\n1. student profile")
    print("2. marks manager")
    print("3. attendance manager")
    print("4. study tasks")
    print("5. exit")

    choice=input("enter your choice:")

    if choice=="1": 
        student_profile()
    elif choice=="2":
        marks_manager()
    elif choice=="3":
        attendance_manager()
    elif choice=="4":
        task_manager()
    elif choice=="5":
        print("thankyou for using student managment system")
        break
    else:
        print("invalid choice")


from marks2 import marks_manager

