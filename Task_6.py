#Task6
#Define a class based on the following statement:
#Your friend Yashi, is looking for a way to store her cooking recipes.
#Now she asked you to make a program where she can input the dish name,
#dish ingredients and their quantity, and the procedure for making the
#dish. Your task is to create a Python class

print("\n\n")
class Recipes:

    recipe_count = 0

    def __init__(self, dish_name, recipe_author) -> None:
        self.dish_name = dish_name
        self.recipe_author = recipe_author

    def input_recipe(self, ingredients, instructions):
        self.ingredients = ingredients
        self.instructions = instructions
        Recipes.recipe_count += 1
    
    def show_recipe(self):
        print(f"\n{self.dish_name}\nMade by ---> {self.recipe_author}\n")
        
        print("Ingredients Required --->")
        for k in self.ingredients:
            print(f"{self.ingredients[k]} of {k}")
        
        print("\nInstructions for preparing the dish --->")
        for k in range(len(self.instructions)):
            print(f"Step {k+1}: {self.instructions[k]}")

    def get_all_recipes():
        print (Recipes.recipe_count)

A = input("Please enter the name of the Recipe : ")
B = input("Please enter the Author of the Recipe : ")
C = input("Please enter all names of ingredients seperated by a ',' : ").split(",")
D = input("Please enter all qunatities of the ingredients according to the above names, seperated by a ',' : ").split(",")   
E = dict(zip(C,D))
F = input("Please enter all the steps and kindly seperate them by a fullstop(.) : ").split(". ")

d1 = Recipes(A,B)
d1.input_recipe(E,F)
d1.show_recipe()

print("\nTotal Recipes saved --->")
Recipes.get_all_recipes()
print("\n\n\n\n\n\n")


#You need to write a python script to manage your contacts. Derive class
#Contact from the base classes Person and Address and use their methods
#to print out the contact information. for eg. class Contact(Person,
#Address): You will need to use multiple inheritance to inherit both
#classes.
class Person:
    def __init__(self, name, email):
        self.name = name
        self.email = email


class Address:
    def __init__(self, street, city):
        self.street = street
        self.city = city


class Contact(Person, Address):
    def __init__(self, name, email, street, city):
        Person.__init__(self, name, email)
        Address.__init__(self, street, city)
        

    def __str__(self):
        return "Name: " + self.name + "\nEmail: " + self.email + "\nStreet: " + self.street + "\nCity: " + self.city + "\n"


class Phonebook:
    def __init__(self):
        self.contactlist = []

    def add(self, contact: Contact):
       
        self.contactlist.append(contact)

  
    def show(self):
        for i in self.contactlist:
            print(i)

   
    def sortByStreet(self):
        self.contactlist.sort(key=lambda x: x.street)

   
    def sortByCity(self):
        self.contactlist.sort(key=lambda x: x.city)

   
    def searchByStreet(self, street):
        for i in self.contactlist:
            if i.street.lower() == street.lower():
                print(i)

    
    def searchByCity(self, city):
        for i in self.contactlist:
            if i.city.lower() == city.lower():
                print(i)


if __name__ == "__main__":
    phone = Phonebook()
    c1 = Contact("Anushka", "Ap@gmail.com", "civil lines", "Banda")
    c2 = Contact("Pratiksha", "princy@gmail.com", "kalikua", "Banda")
    c3 = Contact("Nandini", "Nandini@gmail.com", "Lalbangla", "kanpur")
    c4 = Contact("Jimin", "jimin@gmail.com", "Seoul", "Korea")
    c5 = Contact("V", "v@yahoo.com", "Daegu", "Itaweon")
    c6 = Contact("Jin", "seok@yahoo.com", "busan", "Korea")
    c7 = Contact("Mansi", "Mansi@yahoo.com", "Unnao", "Kanpur")
    c8 = Contact("RM", "destryctor@yahoo.com", "Ilsan", "Korea")
    c9 = Contact("Suga", "meow@gmail.com", "Daegu", "Korea")
    c10 = Contact("Jhope", "hoseok@gamil.com", "Busan", "Korea")
    c11=Contact("jungkook","kookie@gmail.com","Busan","Korea")
    phone.add(c1)
    phone.add(c2)
    phone.add(c3)
    phone.add(c4)
    phone.add(c5)
    phone.add(c6)
    phone.add(c7)
    phone.add(c8)
    phone.add(c9)
    phone.add(c10)
    phone.add(c11)
    phone.sortByCity()
    phone.show()