
marks_list = []


num_of_marks = int(input("How many marks do you want to enter? "))


for i in range(num_of_marks):
    single_mark = float(input(f"Enter mark {i + 1}: "))
    marks_list.append(single_mark)  


total_sum = sum(marks_list)
count_of_items = len(marks_list)
average_mark = total_sum / count_of_items


print("\n--- Results ---")
print(f"Your entered marks: {marks_list}")
print(f"Average Mark: {average_mark:.2f}")
