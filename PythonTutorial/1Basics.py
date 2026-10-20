# 1. Python = Python is a high level, interpreted , dynamically typed programming language.It supports multiple programming paradigms, including procedural, object-oriented, and functional programming. 
# It is well known for its clear and readable syntax.It is popular becuase of its cross-platform compatibility, open source, extensive standard library, and large community support.

# Python is a multi-threading programming language but it allow only one thread to execute at a time because of GIL(Global Interpreter Lock).Even though it support multi-threading but it is not suitable for CPU intensive tasks because of GIL.But it is suitable for I/O intensive tasks like web scraping,networking etc.
# For example if we have a program which is downloading multiple files from the internet then it is suitable to use multi-threading because while one thread is waiting for the response from the server, other threads can continue downloading other files.
# But if you want to do the cpu heavy task then you can use multi-processing module which create multiple processes and each process have its own python interpreter and memory space.So it can bypass the GIL limitation and utilize the multiple cores of the CPU.

# Internal working of Python:
# 1. Firstly the we write the python code in a file with .py extension.
# 2. Then the python interpreter reads the code and compiles it into bytecode.Now this bytecode is also called a magic code.Because it is low level representation of the source code that is platform-independent.One thing we need to remember is that the bytecode is not machine code, it is an intermediate representation of the source code.And because it is platform-independent, it can run on any machine that has a Python interpreter installed.The bytecode is stored in .pyc files, which are created in the __pycache__ directory.
# 3. The bytecode is then executed by the Python Virtual Machine (PVM).
# 4. The PVM executes the bytecode line by line, converting it into machine code that the computer can understand.
# 5. The PVM also manages memory allocation and garbage collection, which means it automatically frees up memory that is no longer needed by the program.




# 2. Rest of the basic thing like the variables,keywords , type casting and type coversion are same as in other programming languages.

# Identifieres = These are nothing but the names given to the varaibles are called identifiers.

# Keywords = These are the reserved words in Python that have a special meaning and cannot be used as identifiers. For example, if, else, while, for, def, class, etc.

# Variables = These are the names given to the data that we want to store in the memory. In Python, we do not need to declare the data type of the variable explicitly. The data type is inferred from the value assigned to the variable.
# special and uniques examples to delare a varaibles in python:
# a = b = c = 10  # Multiple variables can be assigned the same value in a single line.
# x, y, z = 1, 2, 3  # Multiple variables can be assigned different values in a single line.
# _private_var = "This is a private variable"  # Variables starting with an underscore are considered private by convention.
# global_var = "This is a global variable"  # Variables declared outside of any function are considered global.
# constant_var = 3.14  # Constants are typically written in uppercase letters by convention.

# Literals = These are the fixed values that we assign to the variables. For example, 10, 20.5, "Hello", True, etc.In this we have a very special literal called None, which is used to represent the absence of a value or a null value.

# 3.Operators = These are the symbols that are used to perform operations on the variables and literals. Python supports various types of operators, including arithmetic, relational, logical, bitwise, assignment like in other programming languages.But it contains two special operators that are not present in other programming languages:
# 1. Identity operator = This operator is used to check whether two variables reference to the same object in memory or not. It is represented by the keywords 'is' and 'is not'.
# 2. Membership operator = This operator is used to check whether a particular value is present in a sequence (like a list, tuple, or string) or not. It is represented by the keywords 'in' and 'not in'.

# 4. Data Types = Python has several built-in data types that are used to store different types of data. The most commonly used data types are:
# 1.Numeric data types = int , float, complex
# 2.Sequence data types = str,list, tuple, range
# 3.Mapping data type = dict
# 4.Set data types = set, frozenset
# 5.Boolean data type = bool
# 6.Binary data types = bytes, bytearray, memoryview
# 7.NoneType = None

# Note = 1. In python every data type is an object including variables also.So it just means that when we create any variable, it is actually creating an object in memory and assigning a reference to that object to the variable.So there is no any concept like stack and heap memory in python.Everything is stored in heap memory and the variables are just references to those objects.
# 2. Because there is no concept like stack and heap memory in python, we do not need to worry about memory management and garbage collection. Python automatically manages memory allocation and deallocation for us. It uses a technique called reference counting to keep track of the number of references to an object in memory. When the reference count drops to zero, the object is automatically deleted from memory.
# 3. Also the data types are categoriesed into two types: mutable and immutable.
# Mutable data types = These are the data types whose value can be changed after they are created. For example, list, set, and dict,bytearray,class.
# Immutable data types = These are the data typeswhose value cannot be changed after they are created.They just references to new object. For example, int, float,complex, str, tuple (but note: if it contains a mutable object inside, that mutable part can still change), and frozenset,bytes.

# 5.Control Flow = Python provides several control flow statements that are used to control the flow of execution of the program. The most commonly used control flow statements are:
# 1. Conditional statements = if, elif, else.Exactly similar to the other programming languages. But the only differenc lies in the syntax. In Python, we use indentation to define the blocks of code instead of curly braces or keywords like begin and end.
# 2. Looping statements = for, while.Here the difference lies in the syntax and the indentation.
# 3. Loop control statements = break, continue, pass
# 4. Exception handling statements = try, except, finally, raise

# Examples:

# 1. Write a program to check whether a number is even or odd using if-else statement.
# num = int(input("Enter a number: ")); # input() method is used to take input from the user.

# if (num % 2 == 0):
#     print(f"{num} is an even number."); # here we are using f-string/string literals to format the string and print the value of num variable.
# elif (num %2 != 0):
#     print(f"{num} is an odd number.");
# else:
#     print(f"{num} is not a valid number.");
    
# 2. Write a program to print the first 10 natural numbers using for loop but updation by 2.

# print("Using for loop:");
# for i in range(1,11,2): 
#     print(i,end=" "); # here we are using end=" " parameter to print the numbers in the same line with space in between.
# else:
#     print("End of else loop.");    
    
# Note = 1. range(start,stop/Exclusive,step/updation) function is used to generate a sequence of numbers. It takes three arguments: start, stop, and step/updation.
# 2. You can also add else block which for or while loop. Which run when the last iteration failed.

# print("\nUsing while loop:");
# j = 1;

# while j<=10:
#     print(j,end=" ");
#     j += 2;

# 3. break, continue , pass = These are nothing but the keywords break break the current iteration, continue skip the current iteration, pass is nothing but a placeholder.

# Example of continue and pass:

# for i in range(1,11):
#     if(i == 2):
#         continue;  #Continue break the flow from here and skip that iteration.
#     if(i %2 == 0):
#         print(i);
#         print(f"{i} is an even number.");

# for i in range(1,11):
#     if(i == 2):
#         pass;  #pass does not break the flow from here.
#     if(i %2 == 0):
#         print(i);
#         print(f"{i} is an even number.");

# 6. Function = It is nothing but a reusable block of code.Created using "def"  keyword in python.

# Syntax:
# def functionName(parameter1,parameter2,...):

# def greet(name):
#     print(f"Hello {name}");

# greet("Akshay");

# Note:
# 1. Default parameter = we can also set te default parameter to the function.
# 2. Keyword arguments = we can also pass arguments value in a random fashion.
# e.g. = functionName(age="...",name="...");
# 3. Arbitary Arguments = It is used when you need to create a function which can receive unlimited arguments.
# Types = *args used for positional arguments and **kwargs used for keyword arguments.
# e.g.:

# def sum(*args):
#     total = 0;
#     for i in args:
#         total += i;
#     return total;

# print("Sum is:",sum(1,2,3,4,5));


# def details(**args):
    
#     for key,value in args.items():
#         print(f"{key}:{value}");

# details(name="Akshay",age=23);

# 4. In python there is no any cocept like the call by value and reference because we know that in python very thin is object and passed using the reference so according to the data type whether it is mutable or immutable the values changes in the funciton.

# 5. Lambda function = These function are nothing but the shortand property to create a function which can takes multiple parameters and return one output.It is created by using the "lambda" keyword.
# e.g.:

# sum = lambda x,y:x+y;

# print(sum(5,5));

# 6. Type hints = Also called type annotation.It is used to give a hint that what type of data a varaible can store or a function can return.One more important thing is , type hints are only for developers not for python compiler.It means if you store the wrong value in the type hints variable then python don't show you the runtime error,python ignore the type hints.
# e.g.:
# name:str = input("Enter Your name:");

# def func1(a:int,b:float)->int:
#     return a+b;

# 7. Some of the built in funciton of python:

# 1. Type & Introspection:
# x = 10;
# print(type(x))                
# print(id(x))                   # Unique memory ID (e.g., 140493123123456)
# print(isinstance(x, list))     # False
# print(dir(x)) 

# 2. Input/Output:
# input(),print();


# 3. Data Conversion:

# print(int("42"))           # 42
# print(float("3.14"))       # 3.14
# print(str(100))            # '100'
# print(list("abc"))         # ['a', 'b', 'c']
# print(tuple([1, 2]))       # (1, 2)
# print(set([1, 2, 2]))      # {1, 2}
# print(dict(a=1, b=2))      # {'a': 1, 'b': 2}
# print(bool(0))             # False



# 4. Iteration & Sequence Operations:

# arr = [1,2,3,4,5];
# # len() – get length
# print(len(arr));

# # range() – generate a sequence of numbers.Return Lazy iterator.

# print(list(range(5)));

# # enumerate() – loop with index + value.Return Lazy iterator.

# print(list(enumerate(arr))); # you can integrate with loop as well:

# # zip() – combine multiple iterables element-wise.Return Lazy iterator.

# letters = ['a', 'b']
# numbers = [1, 2]
# print(list(zip(letters, numbers)))  # [('a', 1), ('b', 2)]

# nums = [5,4,3,2,1]; 

# # sorted() – return sorted list
# print(sorted(nums));  # It by default return in ascending order.You can also pass the reverse=True parameter to sort in descending order.
# print(sorted(nums,reverse=True));

# obj = {"apple":3,"banana":1,"cherry":2};
# print(sorted(obj)); # it will sort the keys of the dictionary.
# print(sorted(obj.items(),key=lambda x:x[1])); # it will sort the dictionary based on the values.

# arr_obj = [{"name":"akshay","age":24},{"name":"rahul","age":22},{"name":"rohit","age":23}];
# print(sorted(arr_obj,key=lambda x:x["age"])); # it will sort the list of dictionary based on the age key.
# print(sorted(arr_obj,key=lambda x:x["name"])); # it will sort the list of dictionary based on the name key.
# print(sorted(arr_obj,key=lambda x:x["name"],reverse=True)); # it will sort the list of dictionary based on the name key in descending order.




# # reversed() – reverse iterator.You need to type cast the result after that.It will only reverse the iterator/pointer in the memory.It will return a lazy iterator so you need to type case in a list which force python to run for all elements.
# print(list(reversed(nums)));


# # sum() – sum of iterable
# print(sum(nums));        
 

# # min() / max() – smallest / largest item
# print(min(nums));          
# print(max(nums));



# 5. Functional Programming Functions:

# nums = [1, 2, 3, 4]

# # map() – apply a function to all items in an iterable.Return reverse iterator.
# print(list(map(lambda x: x*2, nums)))      # [2, 4, 6, 8]

# # filter() – filter items based on a condition.Return reverse iterator.
# print(list(filter(lambda x: x%2 == 0, nums))) # [2, 4]

# # any() – returns True if any element is truthy
# print(any([0, False, 5]))                  # True

# # all() – returns True if all elements are truthy
# print(all([1, True, 3]))                   # True



# 6.  Object Creation / Utilities

# abs() – absolute value
# print(abs(-7))           # 7


# round(float,precisionAfterDecimal) – round to nearest integer or decimal places
# print(round(3.14159, 2)) # 3.14

# pow(n,m) – power (also ** operator)
# print(pow(2, 3))         # 8


# hash() – hash value of object
# print(hash("python"))    # Unique hash value


# slice() – create slice objects for indexing.Basically we can do slicing manually like [start:stop:step] but in order to reuse that logic we can create it using the slice(start,end,step) method and reuse that logic in multiple lists.
# s = slice(1, 4)
# temp = [10,20,30,40];
# print(temp[s])  # [20, 30, 40]

# Note = 1. Negative slicing = negative slicing means -1 for last element , -2 for second last,and so on.
# but you can simple use that formula like len(num)-NegativeSliceNumber = actual start:
#  e.g. :
# temp[-4:-1] # temp[0,3];
# 2. We apply slicing on tuples , list,string.But not on set,dict,frozenset.


# 7. Other methods:

# # open()
# with open("test.txt", "w") as f:
#     f.write("Hello World")

# # eval() — use carefully!
# x = 10
# print(eval("x + 5"))  # 15

# # exec() — executes Python code dynamically
# exec("y = 7")
# print(y)              # 7

# print(globals().keys())  # All global variables
# print(locals())          # Local variables
# class MyClass:
#     def __init__(self):
#         self.a = 10
# obj = MyClass()
# print(vars(obj))         # {'a': 10}

print("Hello World!");

# Dynamic string in python :

# print("Hello {}".format("Sahil"))
# print("Hello {name}".format(name="Sahil"))
# print("Hello {name} {sirname}".format(name="Sahil", sirname="Kumar"))
# print("""Hello {name} {sirname}""".format(name="Sahil", sirname="Kumar"))

# print(""" Hello %(name)s %(sirname)s """ % {"name": "Sahil", "sirname": "Kumar"}) # Old way
 
# name = "sahil"
# print(f"hello {name}")

# Immutable and mutable data types in python:
# Immutable data types = int, float, complex, str, tuple, frozenset, bytes.It simply means that once we create an object of these data types then we cannot change their value.But we can reassign the variable to a new object.
# For example:
# a = 10
# b = a
# b = 5
# print(a) # Output: 10
# print(b) # Output: 5
#   
# Mutable data types = list, set, dict, bytearray, class. It simply means that once we create an object of these data types then we can change their value without creating a new object.
# For example:

# a = [1, 2, 3]
# b = a
# b.append(4)
# print(a) # Output: [1, 2, 3, 4]
# print(b) # Output: [1, 2, 3, 4]
