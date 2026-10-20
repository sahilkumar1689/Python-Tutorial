# Modules = Specifically in python modules are nothing but a python script that created with the help of .py extension , which contain some classes,functions,variables ,etc. And we can easy use those functions and classses in other file by just import them.

# Types:
# 1. Used defined Modules = These modules are those modules which created by the programmers for their ease.

# Example 1:
# import Calculator; # Here we can import all the functions writen in calulator folder using the fileName.Now we can use all the function by using the fileName.Methods() Name.

# print(Calculator.add(1,2,3,4,5));
# print(Calculator.sub(1,2));

# Example 2:
# from Calculator import * # By using that import statement we can import all the methods of the calculator file now we can directly use them without require the fileName.

# print(add(1,2,3,4,5));
# print(mul(1,2,3,4,5));

# Example 3:

# from Calculator import rem,div;     # We can directly import the specific methods also.

# print(rem(4,3));
# print(div(4,3));



# 2. Built in module = These are those module which already present in the python we just need to import them to use.

# 1. Math module = Provide complex mathematical functions.

# importing the math module  
# import math  
  
# # using the variables and functions from the imported module  
# print("Pi =", math.pi)  # returns value of Pi  
# print("Square root of 16 =", math.sqrt(16))  # returns square root of 16  
# print("Floor value of 19.5 =", math.floor(19.5)) # returns floor value of 19.5  
# print("Ceiling value of 24.7 =", math.ceil(24.7))  # returns ceiling value of 24.7  
# print("Factorial of 6 =", math.factorial(6)) # returns factorial of 6  


# 2. Random module = Use to generate random number.

# import random;

# 1. random.randint(start,end) = It generate random value between start and end both are inclusive.

# print(random.randint(5,10));

# 2. random.random() = It generate random value between 0,1.
# print(random.random());

# 3. random.choice(list) = Use to select random value from the list of elements.

# list1 = ["akshay",23,6.5,1];

# print(random.choice(list1));


# 3. os module = It is very powerfull module which help us to provide a connection between the user and the operating system.And allow us to perform system specific task.

# 1. os.name() = It will return the current operation system name.
# 2. os.mkdir() = used to create new directory.
# 3. os.getcwd() = used to get current working directory.
# 4. os.rename() = rename the directory name.
# 5. os.environ[NameofSecrete] = It is used to access the secrete varaible in the python code.But firstly we need to use the load environemnt variable in the os. For this we install the dotenv package.

# e.g.:

#from dotenv import load_dotenv, find_dotenv

# dotenv_path = find_dotenv()  # Finds the .env file
# load_dotenv(dotenv_path)     # Loads it
# os.environ["secreteName"];

# 4. sys module








