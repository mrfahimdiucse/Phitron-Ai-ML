# normal formatting
from operator import index


a=5
b=10
print("The value of a is {} and the value of b is {}".format(a,b))

# value based formatting
a=5     
b=10
print("The value of a is {0} and the value of b is {1}".format(a,b))

# index based formatting
a=5 
b=10
print("The value of a is {1} and the value of b is {0}".format(a,b))


# f string formatting
a=5
b=10
print(f"The sum of {a} and {b} is {a+b}")