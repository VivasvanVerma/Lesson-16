def factorial(x):
    if x == 0 or x == 1:
        return 1
    else:
        return x*factorial(x-1)

x = int(input("Enter a nummber: "))
a = factorial(x)
print("Factorial of ", x, "is: ", a)