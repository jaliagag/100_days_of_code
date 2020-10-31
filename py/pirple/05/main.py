# Fizz Buzz

# Write a program that prints the numbers from 1 to 100

# for multiples of three print "Fizz" and for the multiples of five print "Buzz"


for i in range(1,101):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
        # continue #(?)
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    elif i % 2 != 0 and i % 3 != 0 and i % 5 != 0:
        print("Prime")
    else:
        print(i)

