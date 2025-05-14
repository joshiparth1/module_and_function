def Factorial(n):

    if(n<2):
        return 1
    else:
        return n*(Factorial(n-1))
num=int(input("Enter a number:"))
print(f"Factorial of {num} is: {Factorial(num)}")