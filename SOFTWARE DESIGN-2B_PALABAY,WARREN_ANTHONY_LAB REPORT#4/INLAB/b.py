def product(m, n):
    if n == 0:
        return 0
    else:
         return m + product(m, n-1)
n = int(input("Enter a Number: "))
m = int(input("Enter a Number to multiply by the first number: "))
print("The product of the two number is: ", product(m,n))

