first = int(input("First number:"))
second = int(input("Second number:"))

if first < second:
    factor = first
else:
    factor = second
        
while first % factor!=0 or second % factor !=0:
        factor=factor -1
print("The highest common factor is ",factor)
