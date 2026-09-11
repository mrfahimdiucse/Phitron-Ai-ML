n=5
fact=1
for i in range(1,n+1):
    fact=fact*i
print("Factorial of", n, "is:", fact)

print("************************")

def factorial(n):
    fact=1
    for i in range(1,n+1):
        fact=fact*i     
    return fact

result = factorial(5)
print("Factorial of 5 is:", result)