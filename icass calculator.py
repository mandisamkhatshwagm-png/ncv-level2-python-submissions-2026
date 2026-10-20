# ICASS Calculator - Fixed version of Scratch project
# Calculates Total ICASS and Percentage

def main():
    student_name = input("Enter student name: ")
    student_num = input("Enter student number: ")

    test1 = float(input("Enter test 1: "))
    test2 = float(input("Enter test 2: "))
    ass1 = float(input("Enter ass1: "))
    ass2 = float(input("Enter ass2: "))

    icass_mark = test1 + test2 + ass1 + ass2
    total = icass_mark
    percent = (total / 400) * 100  # CORRECT: (total / 400) * 100, NOT total / (400*100)

    print(f"\nName: {student_name}")
    print(f"Student Number: {student_num}")
    print(f"Total Icass: {total}")
    print(f"Percentage: {percent}%")

if __name__ == "__main__":
    main()