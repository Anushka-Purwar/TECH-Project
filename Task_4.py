#First Questio( Task 4)
#Function for finding roots of a quadratic equation
#Write a python function that takes a, b, c as arguments, where a, b, c are
#constants (ax^2 + bx + c = 0) and returns a 2-tuple


import math        #Importing neccesary directories
import typing  
def  quadratic_solve( p: float, q : float, r : float):         #Function define
  
    dis = q * q - 4 * p * r                                    #i have taken coefficent of x^2 as p, x as q and the constant as r  (For ease)
    vale = math.sqrt(abs(dis)) 

    print("\n\n")
    print(" The Given Quadratic Equation is " + str(p) + "x^2 " + " + " + str(q) + "x " + " + " + str(r) + " = 0") 
    
    
    if dis > 0:                                         #if - else/ if-elif ladder
        print(" Real and different roots ")               #in case of real and different roots, roots will be found in this manner
        root1 =  (-q + vale) / (2 * p) 
        root2 = (-q - vale) / (2 * p)
        
        return root1 , root2
  
    elif dis == 0:  
        print(" real and same roots")               #in case of real and same, roots will be found in this manner
        root1 = root2 = -q / (2 * p)
        return root1  , root2                        #root1 = root2 because both roots are equal and real
        
        
  
    else :  
        print("Complex Roots")                  #in case of complex roots, roots will be found in this manner
        root1 = - q / (2 * p)
        root2 = - q / (2 * p)
        return str(root1) + " +i" + str(vale)  , str(root2) + " -i" + str(vale)
  
  
p = float(input('Enter a:'))  
q = float(input('Enter b:'))  
r = float(input('Enter c:'))  
  
# If p is 0, then incorrect equation  
if p == 0:  
    print("Enter correct quadratic equation")  
  
else:  
    print(quadratic_solve(p, q, r))                            #Function call





print("\n\n\n\n")


#Second part of Task 4
#Binary Search is a fundamental searching algorithm that is used almost
#everywhere. It is used to check if an items is present
#in a list/sequence of items.
#Note: For binary search to work, the list/sequence must be sorted.
#Search a python list
#(The list may contain any data type, but all types must be the same)
#binary search


def search(seq, k):
    start = 0
    end = len(seq) - 1

    while  start <= end : 
        mid = start + (end - start) // 2
        midpoint_value = seq[mid]
        if midpoint_value == k:
            return mid

        elif k < midpoint_value :
            end = mid - 1

        else:
            start = mid + 1

    return None

list = []    
size = int(input("Enter the size of the array: "))    
       
for i in range(size):    
     x = int(input("Enter the element at {} position in the array: ".format(i+1)))    
     list.append(x)    
      
list.sort()    
print("Entered array elements are: ")    
for lists in list:    
    print(lists,end="\t")    
     
z = int(input("\nEnter the array element to be searched: "))    
print(search(list, z)) 

print("\n\n\n\n\n\n")

#Third part of task 4
#Write a function that takes in a list of 4-tuple which represents student
#information, and returns a subset of the list of students filtered
#according to the given criteria.
#student -> (roll, name, branch, sgpa)
#Output the students matching the follwing criteria:
#1) Admitted in session 2020-21 (roll starts with 20)
#2) Have a sgpa of 8 or above

from typing import List, Tuple, Dict

student_astuple = Tuple[str, str, str, int]

def great_performers(all_students:List[student_astuple]) -> List[Dict]:

     
    filtered: List[student_astuple] = []

    def condition(student):
        if student[0][:2]=='20' and student[3]>=8:
            return student
        else:
            return None

    filtered=list(filter(condition,all_students))

    # Return the result as a list of dicts

    result: List[Dict] = []
    
    
    for i in filtered:
        result.append(dict(roll = i[0], name = i[1], branch = i[2], cgpa = i[3]))

    return result

L = [
       ('1900200300205','Ed sheeran','IT',8.8),
       ('2000400300204','sue','IT',9.0),
       ('1900400300235','jane','IT',6.2),
       ('2000300500374','mic','IT',8.2)]
result_a=great_performers(L)
print(result_a)

print("\n\n\n\n\n\n")
