
n = int(input("Enter positive whole number n: ").strip())

if n < 1:
    print("Rejection message - n must be 1 or more")
else:
    total = 0
    for i in range(1, n + 1):
        cube = i ** 3
        print(cube, end=" ")
        total += cube
    
    print(f"\nTotal: {total}")