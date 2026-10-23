def getMark():
    marks = []
    # Removed the unused 'i' variable that caused a NameError
    mark = int(input("Enter mark (-1 to stop):  "))
    while mark != -1:
        marks.append(mark)
        mark = int(input("Enter mark (-1 to stop): "))
    return marks

def print_list_size(marks):
    print(f"Our list has {len(marks)} elements")

def print_marks_size(marks):
    for x in range(len(marks)):
        print(f"Mark {x+1} is {marks[x]}")
        
def get_sum_of_marks(marks):
    total_sum = 0 # Avoid using 'sum' as a variable name since it is a built-in function
    for x in range(len(marks)):
        mark = marks[x]
        total_sum = total_sum + mark
    return total_sum # Moved return outside the loop so it sums everything before returning

def determine_highest(marks):
    if not marks: # Handle empty list scenario
        print("No marks entered yet.")
        return
        
    highest = marks[0]
    for i in range(len(marks)):
        current_mark = marks[i] # Fixed typo: changed 'mark[i]' to 'marks[i]'
        if current_mark > highest:
            highest = current_mark
    print(f"The highest mark is {highest}") # Added 'f' to make it an f-string

# Main Program Loop
entered_marks = []
menu = ('\nPress 1: Capturing marks\n'
        'Press 2: Check number of marks\n'
        'Press 3: To calculate sum of marks\n'
        'Press 4: To find the highest mark\n'
        'Press -1: To exit\n')

# Wrapped in a while loop so the user can actually use the menu options sequentially
while True:
    print(menu)
    choice = int(input(': Make a choice '))

    if choice == 1:
        entered_marks = getMark()
    elif choice == 2:
        print_list_size(entered_marks)
    elif choice == 3:
        calc_sum = get_sum_of_marks(entered_marks)
        print('Sum of all marks =  ', calc_sum)
    elif choice == 4:
        determine_highest(entered_marks) # Added the missing function call
    elif choice == -1: # Fixed exit choice to match the menu description
        print('Thank you for using the App')
        break
    else:
        print('Not on the menu')
