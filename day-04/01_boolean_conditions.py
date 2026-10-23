mark = float(input("Enter mark (0-100): ").strip())

if mark < 0 or mark > 100:
    print("Invalid mark")
elif mark <= 39:
    print("Not achieved")
elif mark <= 49:
    print("Not yet competent")
elif mark <= 69:
    print("Competent")
elif mark <= 79:
    print("Highly competent")
else:
    print("Outstanding")