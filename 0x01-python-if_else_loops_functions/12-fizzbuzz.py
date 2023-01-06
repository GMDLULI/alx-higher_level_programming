#!/usr/bin/python3
# Author- Gugulethu Mdluli
"""print the numbers from 1 to 1000 separated by a space
   for multiples of three, print fizz instead of the number
   for multiples of five, print BUzz instead of the number.
   for multiples of both three and five print FizzBuzz instead of the number


   """
def fizzbuzz():
    for number in range(1, 101):
        if number % 3 == 0 and number % 5 == 0:
            print("FizzBuzz ", end="")
        elif number % 3 == 0:
            print("Fizz ", end="")
        elif number % 5 == 0:
            print("Buzz ", end="")
        else:
            print("{} ".format(number), end="")
