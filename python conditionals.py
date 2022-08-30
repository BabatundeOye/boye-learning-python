# Learning python conditionals

value = int(input("Enter an integer"))

if value % 4 == 0 and value % 2 ==0:
    print("fizzbuz")
elif value % 4 ==0:
    print("Fizz")
elif value % 2 ==0:
    print("Buzz")
else:
    print(value)
    