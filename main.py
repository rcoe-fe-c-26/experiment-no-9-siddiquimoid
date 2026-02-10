n = int(input("Enter Number: "))

if n < 0:
    print("Factorial of", n, "is not defined")
else:
    fact = 1
    for i in range(1, n + 1):
        fact = fact * i
    print("Factorial of", n, "is", fact)
