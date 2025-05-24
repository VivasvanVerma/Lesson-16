
def cube():
    cubed = num**3
    return cubed

def divisible():
    if num % 3 == 0:
        a = cube()
        print("Cube of ", num, "is ",a)
    else:
        print("Number is not divisible by 3")

num = int(input("Enter a number: "))
divisible()
