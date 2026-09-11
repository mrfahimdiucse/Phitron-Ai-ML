salary=float(input("Enter the salary: "))
if salary<30000:
    tax=salary*0.05
    print("The tax is:", tax)
elif salary>=30000 and salary<70000:
    tax=salary*0.15
    print("The tax is:", tax)
elif salary>=700000:
    tax=salary*0.25
    print("The tax is:", tax)
else:
    print("No tax applicable.")

def allEvenNumbers(a,b):
    for i in range(a,b+1):
        if i%2==0:
            print(i)

x=int(input("Enter the starting number: "))
y=int(input("Enter the ending number: "))
allEvenNumbers(x, y)



def print_digit(number):
    digits = []
    while number > 0:
        digits.append(number % 10)
        number = number // 10
    for digit in reversed(digits):
        print(digit)

print_digit(312)

def print_digit_count(number):
    count = 0
    digits = []
    while number > 0:
        digits.append(number % 10)
        number = number // 10
    for digit in reversed(digits):
        count += 1
    print("Number of digits:", count)
print_digit_count(312)

def print_digit(number):
    sum = 0
    digits = []
    while number > 0:
        digits.append(number % 10)
        number = number // 10
    for digit in reversed(digits):
       sum += digit
    return sum

sum=print_digit(312)
print("Sum of digits:", sum)

def divisable(a, b):
    for i in range(a, b + 1):
        if i % 5 == 0 and i % 3 == 0:
            print(i)
divisable(1,100)


print("The Arithmetic Calculator")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
option=int(input("Enter your option: "))
match option:
    case 1:
        a=int(input("Enter the first number: "))
        b=int(input("Enter the second number: "))
        print("The sum is:", a+b)
    case 2:
        a=int(input("Enter the first number: "))
        b=int(input("Enter the second number: "))
        print("The difference is:", a-b)
    case 3:
        a=int(input("Enter the first number: "))
        b=int(input("Enter the second number: "))
        print("The product is:", a*b)
    case 4:
        a=int(input("Enter the first number: "))
        b=int(input("Enter the second number: "))
        print("The quotient is:", a/b)

while True:
    user_input = input("Enter a number (or type 'Quit' to stop): ")

    # Check if the user wants to quit
    if user_input.strip().lower() == "quit":
        print("Program stopped.")
        break

    try:
        # Convert input to float (handles both integers and decimals)
        number = float(user_input)

        if number > 0:
            print("Positive")
        elif number < 0:
            print("Negative")
        else:
            print("Zero (Neither positive nor negative)")

    except ValueError:
        print("Invalid input! Please enter a valid number or 'Quit'.")



def is_prime(n):
    # Prime numbers must be greater than 1
    if n < 2:
        return False

    # Check if n is divisible by any number in range [2, n-1]
    for i in range(2, n):
        if n % i == 0:
            return False  # Found a factor, so it's non-prime

    return True  # No factors found, so it's prime


# Example usage:
print(is_prime(9))  # Returns False (divisible by 3)
print(is_prime(7))  # Returns True
        