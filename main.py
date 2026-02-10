n = int(input("Enter Number: "))

if n < 0:
print(f"Factorial of {n} is Not Defined")
else:
fact = 1
for i in range(1, n + 1):
fact *= i
print(f"Factorial of {n} is {fact}")
