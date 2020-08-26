# inheritance allows us to define a class that inherits all the methods and properties from another class.
# there are two types of classes: parent class, child class.

# create a parent class 
class Person:
    def __init__(self, fname, lname):
        self.firstname = "clyne"
        self.lastname = "zino" 

    def printname(self):
        print(self.firstname, self.lastname)

        # use the person class to create an object, and then execute the printname method

x = Person("clyne", "zino")
x.printname()        


# child class
class Person:
    def __init__(self, fname, lname):
       self.firstname = "clyne"
       self.lastname = "zino" 

    def printname(self):
        print(self.firstname, self.lastname)

class Student(Person):
    def __init__(self, fname, lname):
        Person.__init__(self, "clyne", "zino")

x = Student("clyne", "zino")
x.printname()      


#use the super function
class Person:
    def __init__(self, fname, lname):
       self.firstname = "clyne"
       self.lastname = "zino" 

    def printname(self):
        print(self.firstname, self.lastname)


class Student(Person):
    def __init__(self, fname, lname):
        super(). __init__(fname, lname)
        

x =Student("clyne", "zino")
x.printname()

# Add properties
class Person:
    def __init__(self, fname, lname):
       self.firstname = "clyne"
       self.lastname = "zino" 

    def printname(self):
        print(self.firstname, self.lastname)


class Student(Person):
    def __init__(self, fname, lname, year):
       super(). __init__(fname, lname)
       self.graduationyear = year
        

x = Student("clyne","zino", 2016)
print(x.graduationyear)


# Add methods
class Person:
    def __init__(self, fname, lname):
       self.firstname = "clyne"
       self.lastname = "zino" 

    def printname(self):
        print(self.firstname, self.lastname)


class Student(Person):
    def __init__(self, fname, lname, year):
        super(). __init__(fname, lname)
        self.graduationyear = year

    def welcome(self):
        print("welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)

        

x = Student("clyne","zino", 2016)
x.welcome()
