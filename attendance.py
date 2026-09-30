def attendance_manager():
    print("\n===== ATTENDANCE MANAGER =====")

    total_classes = int(input("Enter total classes: "))
    attended_classes = int(input("Enter attended classes: "))

    if attended_classes > total_classes:
        print("Invalid input!")
        return

    attendance = (attended_classes / total_classes) * 100

    print("\n===== ATTENDANCE RESULT =====")
    print("Total Classes:", total_classes)
    print("Attended Classes:", attended_classes)
    print("Attendance:", round(attendance, 2), "%")

    if attendance >= 75:
        print("Status: Attendance is sufficient")
    else:
        print("Status: Attendance is below 75%")

    