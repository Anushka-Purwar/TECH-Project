#a) Read a text file and print all its content
#Just create any text file using notepad and write something in it. Read
#all the lines in the text file using python and print it.


file = open('python.txt', "r")
print(file.read()+ "\n\n")


print("\n\n\n")


#2.b) Divide a number by 0 and catch the exception
#Dividing a number by 0 throws an error.. catch the error and show the
#exception to the user.

p = int(input("PLease enter the  numerator : "))
q  = int(input("Please enter the denominator : "))

try:
  print(p/q)
except:
 print("Can't be divide by zero....")

  
print("\n\n\n")  