# [SIG Python Task 2] 

"""
TODO: 
a) Write a program to solve a quadratic equation
b) Write the lyrics for '99 bottles of beer' using for loop
c) Solve Fizz Buzz using while loop.

NOTE: Have Fun Coding!
"""


# a) Write a program to solve a quadratic equation
"""
A quadratic equation is of the form ax^2 + bx + c
Take a, b, and c as float inputs from the user
Then calculate the roots of the equation using the determinant [b^2 - 4ac]
Note: import math module for mathematical operations like math.sqrt
"""
# Write you code here
import math

print ("\nQuadratic Equation : ax^2 + bx + c\n")

a = int (input ("Enter a : ") )             # Taking a,b,c as input from user
b = int (input ("Enter b : ") )
c = int (input ("Enter c : ") )

print ("\nThe roots of the equation " + str(a) + "x^2 + " + str(b) + "x + " + str(c) + " are : " , end='')

for i in range (1,-2,-2):                   # Calculation of roots
    
    x = (-b + i * math.sqrt( pow(b,2) - 4*a*c ) ) / (2*a)
    print ( x , end='  ')

print ("\n\n\n")                            # Separating Questions



# b) Write the lyrics for '99 bottles of beer' using for loop
"""
There is a song called '99 bottles of beer'.
Its lyrices are provided here: http://www.99-bottles-of-beer.net/lyrics.html

You will notice that you can easily generate the lyrics for the song
if you use for loops for printing the lyrics in very few lines.
Your task is to print the lyrics for this song, using for loop.
"""
# Write you code here
import random

def nonzero (n):                            # Bottle Count is >=3 and <=99
    
    print (n , " bottles of beer on the wall. " , n , " bottles of beer.")
    a = random.randint (1,2)

    if (a == 1):
        print ("Take one down and pass it around, " , n-1 , " bottles of beer on the wall.\n")
    
    else:
        print ("If one of those bottles should happen to fall, " , n-1 , " bottles of beer on the wall.\n")

def two ():                                 # Bottle Count = 2

    print ("2 bottles of beer on the wall, 2 bottles of beer.")
    b = random.randint (1,2)

    if (b == 1):
        print ("Take one down and pass it around, 1 bottle of beer on the wall.\n")
    
    else:
        print ("If one of those bottles should happen to fall, 1 bottle of beer on the wall.\n")

def one ():                                 # Bottle Count = 1
    
    print ("1 bottle of beer on the wall, 1 bottle of beer.")
    print ("If that one bottle should happen to fall, what a waste of alcohol!\n")

def ending ():                              # Bottle Count = 0 [THE END]

    print ("No more bottles of beer on the wall, no more bottles of beer.")
    c = random.randint (1,3)
    
    if (c == 1):
        print ("We've taken them down and passed them around, now we're drunk and passed out!")
    
    elif(c == 2):
        print ("There's nothing else to fall, because there's no more bottles of beer on the wall.")
    
    else:
        print ("Go to the store and buy some more, 99 bottles of beer on the wall...")

def main ():
    
    for i in range (99,-1,-1):              # Bottle count goes from 99 to 0
        
        if (i == 2):                        # Bottle Count = 2
            two ()
        
        elif (i == 1):                      # Bottle Count = 1
            one () 
        
        elif (i == 0):                      # Bottle Count = 0
            ending ()
        
        else:                               # Bottle Count is >=3 and <=99
            nonzero (i)

main ()
print ("\n\n\n")                            # Separating Questions



# c) Solve Fizz Buzz using while loop.
"""
This is a very common and easy problem asked in job interviews.
The problem is as follows:
    Print integers 1 to N, but print “Fizz” if an integer is divisible by 3, “Buzz” if an integer is divisible by 5, and “FizzBuzz” if an integer is divisible by both 3 and 5.

    input: 15
    output: 
            1
            2
            Fizz
            4
            Buzz
            Fizz
            7
            8
            Fizz
            Buzz
            11
            Fizz
            13
            14 
            FizzBuzz

Use while loop to loop through number 1 to N, (take N as input from the user)
Use if, elif and else to check for given conditions.
"""
# Write your code here

p = int (input ("Enter N : ") )             # Taking N as input from user

for i in range (1,p+1):

    if (i%3 == 0 and i%5 == 0):             # If number is divisible by both 3 and 5
        print ("FizzBuzz")
    
    elif (i%3 == 0):                        # If number is divisible by 3
        print ("Fizz")
    
    elif (i%5 == 0):                        # If number is divisible by 5
        print ("Buzz")
    
    else:                                   # If number is neither divisible by 3 nor 5
        print (i)

print ("\n")

# NOTE: Make sure to print few empty lines after each task