# Magic Methods = Magic methods are special methods surrounded by double underscores "__method__" that let you define or customize the behavior of Python objects.

# Some of the most important methods are:
# 1. __new__(cls,*args,**kwargs) and __init__(self,*args,**kwargs) = The __new__ is used to create a new instance of a class, while the __init__ is used to initialize the instance.In simple terms __new__ is used to create a new object and __init__ is used to initialize the object.And __new__ is called before __init__ and it must return an instance of the class, if it does not return any then then object is not created and __init__ is not called.
# Uses Cases = Generally used to control the object creation process like in order to achieve the singleton pattern etc.

# e.g.:

class A:
    def __new__(cls,val):
        print("__new__ called")
        return super().__new__(cls);
    
    def __init__(self,val):
        print("__init__ called")
        self.val = val  

# a = A(10)
# print(a.val)

# Singleton Pattern generally used for the database connections:

class singleton:
    _instance = None
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        print("Database Connection")

# a = singleton()
# b = singleton()
# print(a is b)

# 2. __str__(self) and __repr__(self) = __str__ is used to return a string representation of an object, while __repr__ is used to return an official string representation of an object.In short __str__ is used for end user and __repr__ is used for developer.__str__ automatially calls when we try to print any instance. 

# e.g.:

class A:
    def __init__(self,val):
        self.val = val
    
    def __str__(self):
        return f"Value: {self.val}"
    
    def __repr__(self):
        return f"A({self.val})"
    
# a = A(10)
# print(a.__str__()) 
# print(a)    # similar to a.__str__()
# print(repr(a))
# print(a.__repr__())  # similar to a.__repr__()


# 3. __len__,__getitem__,__setitem__,__delitem__,__iter__,__next__,__contains__,reversed__ = These methods help us to make our class iterable or behave like a collection.Because when you call len() internally call __len__ method, when you call for loop then it calls __iter__ method and so on.
# If any object has __iter__ method then it is iterable and we can use it in for loop.And for loop calls __next__ method to get the next value until it raises StopIteration exception.

# e.g.:

class A:
    def __init__(self):
        self.data = [1,2,3,4,5]
    
    def __len__(self):
        return len(self.data)
    
    def __getitem__(self,index):
        return self.data[index]
    
    def __setitem__(self,index,value):
        self.data[index] = value
    
    def __delitem__(self,index):
        del self.data[index]
    
    def __iter__(self):
        return iter(self.data)
    
    def __next__(self):
        return next(self.data)
    
    def __contains__(self,item):
        return item in self.data
    
    def __reversed__(self):
        return list(reversed(self.data))
    
    def __str__(self):
        return str(self.data)
    
    def __repr__(self):
        return f"A({self.data})"
    
# a = A()
# print(len(a))
# print(a[0])
# a[0] = 10
# print(a[0])
# del a[0]
# print(a)
# print(a.__str__())
# print(a.__repr__())
# print(10 in a)
# print(reversed(a))

# 4. __getattribute__,__getattr____setattr__,__delattr__,__dir__ = These methods help us to control the attribute access of an object.

# e.g.:

class A:
    def __init__(self):
        self.data = [1,2,3,4,5]
    
    # It run always when you access any attribute of an object.
    def __getattribute__(self,attr):
        print(f"Accessing {attr}")
        return super().__getattribute__(attr)
    
    # It run when you access any attribute of an object that is not found.
    def __getattr__(self,attr):
        print(f"Attribute {attr} not found")
    
    # It run always when you set any attribute of an object.
    def __setattr__(self,attr,value):
        print(f"Setting {attr} to {value}")
        super().__setattr__(attr,value)
    
    # It run always when you delete any attribute of an object.
    def __delattr__(self,attr):
        print(f"Deleting {attr}")
        super().__delattr__(attr)
    
    # It run always when you call dir() on an object.
    # def __dir__(self):
    #     return dir(self)
    
# a = A()
# a.data
# a.x
# a.data = 10
# a.x = 10
# del a.data
# del a.x
# print(dir(a))

# 5. Operators overloading = We acheive operator overloading using magic methods in python.

# e.g.:

class complex:
    def __init__(self,a,b):
        self.a = a
        self.b = b

    def __str__(self):
        return f"{self.a}+{self.b}i"
    
    def __add__(self,other):
        if isinstance(other,complex):
            return complex(self.a + other.a,self.b + other.b)
        else:
            raise TypeError("Unsupported operand type(s) for +: 'complex' and 'int'")

    def __sub__(self,other):
        if isinstance(other,complex):
            return complex(self.a - other.a,self.b - other.b)
        else:
            raise TypeError("Unsupported operand type(s) for -: 'complex' and 'int'")
    
    def __mul__(self,other):
        if isinstance(other,complex):
            return complex(self.a * other.a,self.b * other.b)
        else:
            raise TypeError("Unsupported operand type(s) for *: 'complex' and 'int'")
    
    def __truediv__(self,other):
        if isinstance(other,complex):
            return complex(self.a / other.a,self.b / other.b)
        else:
            raise TypeError("Unsupported operand type(s) for /: 'complex' and 'int'")
    
    def __eq__(self,other):
        if isinstance(other,complex):
            return self.a == other.a and self.b == other.b
        else:
            raise TypeError("Unsupported operand type(s) for ==: 'complex' and 'int'")
    
    def __ne__(self,other):
        if isinstance(other,complex):
            return self.a != other.a or self.b != other.b
        else:
            raise TypeError("Unsupported operand type(s) for !=: 'complex' and 'int'")
    
    def __lt__(self,other):
        if isinstance(other,complex):
            return self.a < other.a and self.b < other.b
        else:
            raise TypeError("Unsupported operand type(s) for <: 'complex' and 'int'")
    
    def __le__(self,other):
        if isinstance(other,complex):
            return self.a <= other.a and self.b <= other.b
        else:
            raise TypeError("Unsupported operand type(s) for <=: 'complex' and 'int'")
    
    def __gt__(self,other):
        if isinstance(other,complex):
            return self.a > other.a and self.b > other.b
        else:
            raise TypeError("Unsupported operand type(s) for >: 'complex' and 'int'")
    
    def __ge__(self,other):
        if isinstance(other,complex):
            return self.a >= other.a and self.b >= other.b
        else:
            raise TypeError("Unsupported operand type(s) for >=: 'complex' and 'int'")

obj1 = complex(1,2)
print(obj1)
obj2 = complex(3,4)
print(obj2)
obj3 = obj1 + obj2
print(obj3)


# 6.  __call__() = It is used to make an object callable i.e we can call the object as a function.

# e.g.:

class call_example:
    def __init__(self):
        self.data = [1,2,3,4,5]
    
    def __call__(self):
        return self.data

obj = call_example()
print(obj())


# 7. __enter__() and __exit__() = It is used to implement the context manager.

# e.g.:

class FileLogger:
    def __enter__(self):
        print("Resource acquired")
        return self

    def __exit__(self, exc_type, exc, tb):
        print("Resource released") 
        # it also return true for supress the exception and false for raise the exception.

with FileLogger():
    print("Inside block")

# 8. __slots__ = It is used to limit the attributes of an object.

# e.g.:


class A:
    __slots__ = ["data"] # we can only use those attributes that are defined in __slots__
    def __init__(self):
        self.data = [1,2,3,4,5]

obj = A()
obj.data = 10
# obj.x = 10 # it will raise an error

# 9. __name__ = It is used to get the name of the module.It is used to check if the module is being run as a script or imported as a module.If the module is being run as a script then __name__ is set to "__main__" otherwise it is set to the name of the module.

# e.g.:

print(__name__)


# Note = 1. Magic methods are nothing but the special mehtods of the class that called automatically while performaing some operations like we can also say that every operation in python are attached with some magic methods e.g len() == __len__, str() == __str__,+ == __add__ etc.
# 2. Magic methods are contract between the your object and python.We don't call them explicitly python call them for us when we perform some operations.  