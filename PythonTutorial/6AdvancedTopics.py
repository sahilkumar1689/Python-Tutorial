# 1. List comprehension = It is a concide and effective way to create a list.The main advantage of using list comprehension is that it provide a lot of filteration and conditions in order to create a list.

# 1. Using for loop with list comprehension:

# obj = {
#     "name":"akshay",
#     "Age":24,
#     "roll":1
# }

# keys = [i for i in obj.keys()];

# print(keys);

# # 2. Using loops and if statements:

# list1 = [1,2,3,4,5,6,7,8,9,10];

# oddList = [i for i in list1 if i%2!=0]
# print(oddList);


# 2. We also have fractions and decimal libraries read about that.
# 3. We can also have oct(),hex(),bin() for converting numbers into any other format.
# 4. empty {} = treated as empty dictionary and set() = is used to create the empty set.

# 5. Yield Keyword = Yield is similar to the return keyword it is also used to return some value but there is a catch return only return single value and end the function competely but yield is used to create a generated function.Now generater functions are those function who remember their state between different functions call and always starts where they left from.
# So in simple words return keyword simple return one value and exit function but yield also return one value but pasuse the function and save it state in the memory so that when we call that function again it starts where it left off.

#  e.g.:

# def generatorEven(limit):
    
#     for i in range(2,limit+1,2):
#         yield i;

# for i in generatorEven(10):
#     print(i);

# 5. Decorators = Decorators are special functions that take another functions as their parameter add extra functionality to it and return that function.

# Some built in decorators:

# 1. @staticmethod = The method doesn’t not need self,cls object.This method is belong to the class itself,it simply means that we can directly call using class name.Althought we can also call it via object but internally python calls via class name.Because it does not accept the cls,self object so it cannot access the instance or class level data.It is only used to provide some utility functionlaity inside the class.But we can use the class data indirectly using the class name inside the static method.
# e.g.:

# class staticMethodExample:
#     @staticmethod
#     def greet(name):
#         print(f"Hello {name}");

# staticMethodExample.greet("Akshay");  # calling via class name.
# obj = staticMethodExample();
# obj.greet("Rahul");                    # calling via object.
# print(staticMethodExample().__dir__()) # it will also added in the dir of the class.



# 2. @classmethod → It is a method that works with cls object instead of self.Often used as alternative constructors.
# e.g.:
# class User:
#     count = 0

#     @classmethod
#     def create(cls):
#         cls.count += 1
#         return cls()

# inst = User()
# inst.create()        # we can also call using instance but internally it called via class name.
# user1 = User.create()
# user2 = User.create()
# print(User.count)  # Output: 3


# 3. @property and @<property_name>.setter = Method behaves like an attribute.Generally used for data encapsulation and validation.
# e.g.:

# class User:
#     def __init__(self, age):
#         self._age = age

#     @property
#     def age(self):
#         return self._age

#     @age.setter
#     def age(self, value):
#         if value < 0:
#             raise ValueError("Age cannot be negative")
#         self._age = value

# user = User(25)
# print(user.age)  # Accessing age like an attribute
# user.age = 30    # Setting age like an attribute
# print(user.age)

# 4. @lru_cache → Used to cache the results of function calls to optimize performance for expensive or frequently called functions.
# e.g.:

# from functools import lru_cache
# @lru_cache(maxsize=32)
# def fibonacci(n):
#     if n < 2:
#         return n
#     return fibonacci(n-1) + fibonacci(n-2)
# print(fibonacci(10))  # Output: 55

# 5. @dataclass → Automatically generates special methods like __init__(), __repr__(), and __eq__() for classes.It is  primarily used to store data in a class.
# e.g.:
# from dataclasses import dataclass

# @dataclass
# class User:
#     name: str
#     age: int

# u = User("Sahil", 22)
# print(u)


# 1. User defined decorators:


# def parentFunction(func):
#     def childFunction(name):
#         print("Welcome in decorator.");
#         func(name);
#         print("Thanks to visit decorator.");
#     return childFunction;
    

# @parentFunction
# def greet(name):
#     print(f"Hello {name}");
    
# # Basically the above code internally works like this:
# # greet = parentFunction(greet); 
    
# greet("Akshay");


# 2. Addition decorator with cache storage:

# import time;


# def cacheDecorator(func):
#     cache_Storage = {};
#     def wrapper(*args):
#         # Checking in the cache:
#         if args in cache_Storage:
#             return cache_Storage[args];
        
#         # Calling the actual functions:
#         result = func(*args);

#         # Store result in the cache:
#         cache_Storage[args] = result;
        
#         # return that result;
#         return result;
    
#     return wrapper;


# @cacheDecorator
# def add(*args):
#     time.sleep(5);
#     return sum(args);

# print(add(2,3));
# print(add(2,3,3));


# 6. Walrus operator = It allow us to assign value to the variable as a part of an expresssion.Simple means we can store the result of any expression in a variable at the time we use that expression.

# e.g.:

# if (n := len([1,2,3,4,5])) > 3:
#     print(f"List contains {n} elements");

# 7. Advanced Type hints = we simply need to import the typing module.
# from typing import List,Tuple,Dict,Union;

# var1:List[int] = [1,2,3,4,5];


# 8. Match Case statements = It is similar to the switch statements in other languages.

# Syntax:

# match variableName:
#     case value1:
#         return "someting";
#     case value2:
#         return "someting";
#     case _:
#         return "someting";

# 9. We can open more than one file at a time using "with" keyword.

# 10. Meaning of "If __name__ == "__main__" " = Some basically the __name__ is a default attribute in python which tell us about the module in python from where the program is run.If the program is directly run using the command line then its equal to the __main__ , else not. So it is genrally used to check the behaviour that whether our code run directly or imported from the other file.


# 11. Iterator = It is an object that allow us to travers any iterable object like list,tuple,string,etc.
# It internally implements two methods:
# 1. __iter__() = It will return the iterator object iteself.
# 2. __next__() = Return the next item or raise StopIterator exception.

# There are two methods we used in order to convert any iterable object to iterator:
# 1. iter(iterable_object) = Used to create iterator.
# 2. next(iterator) = Used to return the next value.


# 1. Iterator with iterable:

# li = [5,4,3,2,1];   # it is iterable

# it = iter(li);      # it will call the __iter__() method of the list and create an iterator of that and return that iterator.

# print(next(it));    # next will call the __next__() method of iterator.
# print(next(it));
# print(next(it));
# print(next(it));
# print(next(it));
# print(next(it));    # it will raise an Stop iterator error.

#  2. Internal working of loop:

#### Original Loop :
# for i in li:
#     print(i);


#### Internal Working of loop:
# it1 = iter(li);

# while True:
#     try:
#         i = next(it1);
#         print(i);
#     except StopIteration:
#         break;


# 3. Custom iterator:

# class customIterator:
#     def __init__(self,data):
#         self.__num=0;
#         self.data = data;
    
#     def __iter__(self):
#         return self;
    
#     def __next__(self):
#         if self.__num < self.data:
#             val = self.__num;
#             self.__num += 1;
#             return val;
#         else: raise StopIteration;
    
# Now you know what happen beind the scene, refer example 2:
# for i in customIterator(5):
#     print(i);

# Note = 1. Bascially the iter() called the __iter__() methods which return the iterator itself.
# 2. The next() call the __next__() methods which return the next value or raise exception.
# 3. Main difference between the iterable and the iterator is, all the iterable has __iter__() method by default but on the other hand all the iterator have __iter__() and the __next__() methods. So it is compulsary to convert the iterable to iterator in order to successfully iterate over them. Python exactly does the same thing behind the scene,refer example 2.

# 12. Scoping principle in python = It is basically the rule that tell us in which order the variable will be searched in the different scopes.Basically in python we have four types of scopes:
# 1. Local scope = It is the scope that is created inside the function.
# 2. Enclosing scope = It is the scope of the enclosing function in case of nested function.
# 3. Global scope = It is the scope that is created when we define any variable outside the function.
# 4. Built-in scope = It is the scope that is created when we import any module in our program.
# The order of searching the variable in the different scopes is:
# Local → Enclosing → Global → Built-in
# It is also known as the LEGB rule.
# e.g.:
# x = "global x";
# def outer():
#     x = "enclosing x";
#     def inner():
#         x = "local x";
#         print(x);
#     inner();
#     print(x);
# outer();
# print(x);

# Note = 1. In the above example we can see that the variable is searched in the local scope first then in the enclosing scope then in the global scope.
# 2. If we don't find the variable in any of the scopes then it will raise

# 13. Scoping mechanism in python = Pyhton does not follow the block scope like other languages, it only follows the function scope. For example if we define any variable inside the if block or for loop or while loop then that variable will be accessible outside that block.But if we define any variable inside the function then that variable will not be accessible outside that function.If we wanna to access the different scope variable then we can use the global and nonlocal keywords.
# 1. Global keyword = It is used to access the global variable inside the function.
# 2. Nonlocal keyword = It is used to access the enclosing variable inside the nested function.

# But if we use the variable outside the function then, every variable treated as the global variable.

# e.g.:

# a = 10;
# b = 15;

# if a <=10:
#     c = a;
# elif b >=10:
#     c = b
# else:
#     c = None

# print("a: ",a);
# print("b: ",b);
# print("c: ",c);

# Note = 1. In python does not follow the block scope like other languages, it only follows the function scope.
# 2. If we define any variable inside the if block or for loop or while loop then that variable will be accessible outside that block.
# 3. If we define any variable inside the function then that variable will not be accessible outside that function.
# 4. If we wanna to access the different scope variable then we can use the global and nonlocal keywords.

# 14. We can also megre two or more dictionaries using the ** operator.
# e.g.:
# dict1 = {"name":"akshay","age":24};
# dict2 = {"roll":1,"college":"ABC"};
# dict3 = {**dict1,**dict2};
# print(dict3);
# We can also use the update() method to merge two dictionaries.
# dict1.update(dict2);
# print(dict1);

# We can also use the | operator to merge two dictionaries.
# dict3 = dict1 | dict2;
# print(dict3);

# We can also use the | = operator to merge two dictionaries and update the first dictionary.
# dict1 |= dict2;
# print(dict1);

# We can also use the copy() method to create a shallow copy of the dictionary.
# dict4 = dict1.copy();
# print(dict4);
# dict4["name"] = "rahul";
# print(dict1);
# print(dict4);
# Note = 1. The ** operator is used to unpack the dictionary and merge them.
# 2. The update() method is used to merge two dictionaries and update the first dictionary.
# 3. The | operator is used to merge two dictionaries and return a new dictionary.
# 4. The | = operator is used to merge two dictionaries and update the first dictionary.
# 5. The copy() method is used to create a shallow copy of the dictionary.The shallow copy means that if we change the value of the copied dictionary then it will not affect the original dictionary.
# 6. The deep copy means that if we change the value of the copied dictionary then it will affect the original dictionary. We can create a deep copy of the dictionary using the copy module.
# import copy;
# dict5 = copy.deepcopy(dict1);
# print(dict5);
# dict5["name"] = "rohit";
# print(dict1);
# print(dict5);

# 15. We can also merge two arrays using the * operator.
# e.g.:
# arr1 = [1,2,3];
# arr2 = [4,5,6];
# arr3 = [*arr1,*arr2];
# print(arr3);
# We can also use the + operator to merge two arrays.
# arr3 = arr1 + arr2;
# print(arr3);
# Note = 1. The * operator is used to unpack the array and merge them.
# 2. The + operator is used to merge two arrays and return a new array.
# 3. The extend() method is used to merge two arrays and update the first array.
# arr1.extend(arr2);
# print(arr1);
# 4. The copy() method is used to create a shallow copy of the array.
# arr4 = arr1.copy();
# print(arr4);
# arr4[0] = 10;
# print(arr1);
# print(arr4);

            