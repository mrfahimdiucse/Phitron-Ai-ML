name=str(input("Enter your name: "))
age=int(input("Enter your age: "))
print(f"Hello {name}, you are {age} years old.")

a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
print(f"Sum: {a + b}")
print(f"Difference: {a - b}")
print(f"Product: {a * b}")
print(f"Quotient: {a / b}")

a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
c=float(input("Enter a float number: "))
print("Sum: ", a+b+c)
a=float(a)
b=float(b)
c=float(c)
sum=a+b+c
print("Sum: ", sum)
print("Avg: ", sum/3)
print(type(a))
print(type(b))
print(type(c))

string=str(input("Enter a string: "))
print("The string is: ", string)
print(type(string))
string1=int(string)
print(type(string1))
string2=float(string)
print(type(string2))

x=10+3*2**2
print(x)

a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
temp=a
a=b
b=temp
print("After swapping: ")
print("First number: ", a)
print("Second number: ", b)


celsius=str(input("Enter temperature in Celsius: "))
c=float(celsius)
farenheit=(c*9/5)+32
print(farenheit)

PI=3.14
r=float(input("Enter the radius of the circle: "))
area=PI*r**2
print(area)

p=(input("Enter a number: "))
r=(input("Enter the rate of interest: "))
t=(input("Enter the time in years: "))
principal=float(p)
rate=float(r)
time=float(t)
simple_interest=(principal*rate*time)/100
print(simple_interest)

num=input("Enter a number: ")
int_part,frac_part=num.split(".")
print("Integer part: ", int_part)
print("Fractional part: ", frac_part)
