inputNumber = input("Enter a positive integer: ")

for i in range(1,int(inputNumber)+1):
    remainder = int(inputNumber) % i
    if remainder == 0:
        print(f"{i} is a factor of {inputNumber}")