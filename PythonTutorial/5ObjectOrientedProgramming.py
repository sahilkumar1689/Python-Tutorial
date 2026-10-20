# 1. Class Syntax= Always use pascacal case for class name and snake case for method and variable name.

# class className:

class base:
    # Constructore = In python we can create contructor using the __init__(self) method. Which by default contain one self object which refer to the current instance of the class.In pyton we cannot overload the contstructor.There are only two types of constructor in python default and parameterised.
    count = 0  # All the variable creating outside the constructor are treated as the class varaible which related to class.These varaible are similar to the static variable in other languages.
    def __init__(self,name):
        self.name = name;  # Here we can create instance variable like this.Which related to the instance.
        print(f"Hello,{name}");
        base.count += 1;
        
        # Access Specifiers = In python we have three access specifiers public,protected,private.
        self.public = 1; # public varaible.
        self._protected = 1; # protected varaible.
        self.__private = 1; # private varaible.
        
    def details(self):
        # If any other method in class want to work with the instance variable then by default they need to take a self object as a first parameter.
        print(f"{self.public},{self.__private},{self._protected}");

# Relationships = In python we generally we have two types of relationships aggregation and inheritance.

# 1. Aggregation = It is also called has-a relationship where flow goes top down.
# e.g.:

class customer:
    def __init__(self,name,gender,address):
        self.name = name
        self.gender = gender
        self.address = address
    
    def change_details(self,new_name,new_gender,new_city,new_state,new_country):
        self.name = new_name
        self.gender = new_gender
        self.address.change_address(new_city,new_state,new_country)
    
    def print_details():
        print("Name: ",self.name)
        print("Gender: ",self.gender)
        print(self.address)

class address:
    def __init__(self,city,state,country):
        self.city = city
        self.state = state
        self.country = country
    
    def change_address(self,new_city,new_state,new_country):
        self.city = new_city
        self.state = new_state
        self.country = new_country
    
    def __str__(self):
        print("City: ",self.city)
        print("State: ",self.state)
        print("Country: ",self.country)


c1_add = address("Jalandhar","Punjab","India")
c1_customer = customer("Akshay","Male",c1_add)

c1_customer.print_details();

c1_customer.change_details("Sahil","Male","Ludhiana","Punjab","India")
c1_customer.print_details();


# 2. Inheritance = It is also called is-a relationship where flow goes bottom up. In python we can have all five types of inheritance.single,multilevel,multiple,hierarchy,hybrid.

class details:
    def __init__(self,name,age):
        self.name = name;
        self.age = age;

class stdmarks:
    def __init__(self,marks):
        self.marks = marks;
    
class stdDetails(details,stdmarks):
    def __init__(self, name, age,marks):
        # super().__init__(name, age);   # It is only used to call the details constructor because python follow the MRO , method resolution order from left to right.
        
        # But you can directly pass the data using their class name:
        details.__init__(self,name,age);
        stdmarks.__init__(self,marks);
    
    def studentDetails(self):
        # print(f"Name is:{self.name}, age is:{self.age}");
        
        totalMarks = 0  # it will treated as the local varaible finisher ones methods ends.
        
        for i in self.marks:
            totalMarks += i;
        
        print(f"Name is:{self.name}, age is:{self.age}, total marks:{totalMarks}");
    
    def __repr__(self):
        return f"Automatically called when instance is directly printed.";

std1 = stdDetails("Akshay",23,[1,2,3,4,5]);

# std1.studentDetails();

# Polymorphism = In python we does not have any compile time polymorhism because the python is a dynamically typed language.
# 1. So if we try to make more than one function with same name python always pick the lastly created function.
# 2. Python also does not support operator overloading but it provide some magic method like __add__ , __mul__,etc.
# e.g.:
class complex:
    def __init__(self,a,b):
        self.a = a;
        self.b = b;
    
    def printComplex(self):
        print(f"{self.a}+i{self.b}");
    
    def __add__(self,other):
        return complex(self.a+other.a,self.b+other.b);

# obj1 = complex(2,3);
# obj1.printComplex();

# obj2 = complex(3,2);
# obj2.printComplex();

# obj3 = obj1 + obj2;

# obj3.printComplex();

# 3. But python support the method overriding:

class p1:
    def greet(self):
        print("Greetings from p1");

class p2(p1):
    def greet(self):
        print("Greetings from p2");
        

# obj = p2();

# obj.greet();
    

# 4. Abstract Methods = Pyhton also follow the abstract methods and classes.You know abstract classes are those classes which atleast contain one abstract method in it and we cannot create any instance of that class.Abstract class may contains the simple/concrete methods and the abstract methods as well.
# After that the abstract methods are those methods which does not have any defination , they only have declaration.And their defination are provided by the subclasses who inherit the abstract class.

# You need to import these things in order to implement the abstarct methods.
from abc import ABC,abstractmethod

# In order to create abstract class you need to inherit the ABC class:
class animal(ABC):
    
    # Here we create abstract method like this:
    @abstractmethod
    def eat(self):
        pass;

    def speak(self):
        pass;

class dog(animal):
    def eat(self):
        print("Eat meat.");
    
    def speak(self):
        print("Bark");
        
class cat(animal):
    def eat(self):
        print("Drink Milk.");
    
    def speak(self):
        print("Meauth");

# animal1 = dog();
# animal1.eat();
# animal1.speak();

# animal2 = cat();
# animal2.eat();
# animal2.speak();


# Some built-in methods in classes:

print(getattr(std1,"name"));    # used to get any attribute from the object.
setattr(std1,"age",24);         # set the value of any attribute.
print(getattr(std1,"age"));

print(hasattr(std1,"roll"));    # check they have that attribtue.
delattr(std1,"age");            # delete any attribute.

# Some built-in attrubutes:

print(std1.__dict__);       # it provide the dictonary which contains the information about the class:
print(std1.__doc__);        # it contains string which have class documentation.
print(__name__);            # used to access the class module name
print(std1.__module__);     # used to access the module name
# print(std1.__bases__);  #It include tuple of all base classes.
print(std1);

