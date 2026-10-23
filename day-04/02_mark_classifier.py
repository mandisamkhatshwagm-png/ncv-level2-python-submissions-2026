mark = int(input("Enter mark (0-100): ").strip())

# Exactly ONE classification - use elif chain, highest threshold last when using <=
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

# Extension - Second decision: Did learner reach Competent or above?
if 0 <= mark <= 100:
    if mark >= 50:
        print("Competent or above: Yes")
    else:
        print("Competent or above: No")