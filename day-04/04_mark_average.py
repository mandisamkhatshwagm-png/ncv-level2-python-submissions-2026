total = 0
count = 0

while True:
    mark = int(input("Enter mark 0-100 (-1 to stop): ").strip())
    
    if mark == -1:
        break  
    
    if 0 <= mark <= 100:
        total = total + mark
        count = count + 1
    else:
        print(f"Reject {mark}")  

if count == 0:
    print("No valid marks entered.")
else:
    average = total / count
    print(f"Average: {average:.2f}")