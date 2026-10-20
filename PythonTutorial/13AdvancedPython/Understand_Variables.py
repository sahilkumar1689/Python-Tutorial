class temp:
    # every varaible that are created using without self keyword are created at the class level it means that variable is shared with all the instances.And that variable stored in the class __dict__.Not stored in their instances __dict__.
    class_var_shared = 10
    # This is also sotred in the class __dict__ but the "_" at the start simple tell the devloper this varaible is for the internal use only, it is by convention internal not by memory but if you want you can use it like a simple shared varaiable also. 
    _internal_var = 16
    # This is called the mangling variable it means it is also shared but in order to provide extra protection or in order to acheive the protected variable functionlaity it store using this patter in the __dict__ "_className__varName" so that no one case directly access outside the class, if you wanna to use outside the class you need to follow that mangling name patter.
    __mangling_var = 18

    # Note = Python does not offer any kind of variable protection at the end all the variables can easily be access outside the class.But these "_" or "__" are just used to provide the special meaning to the variables.
    def __init__(self,a,b):
        # All the variable created using the self in created at instance level, it means every instance have their own variable in their __dict__.
        self.a = a 
        self.b = b
    

obj1 = temp(1,2);
obj2 = temp(2,3);
print(obj1.a," ",obj1.b)
print(obj2.a," ",obj2.b)


# Case 1 = here we you clearly see that the class_var_shared variable stored in the class __dict__ not in their instances __dict__.

# temp.class_var_shared = 17
# print(temp.class_var_shared)
# print(temp.__dict__)

# print(obj1.class_var_shared)
# print(obj1.__dict__)

# print(obj2.class_var_shared)
# print(obj2.__dict__)

# Case 2 = But there is a catch in this second case here you clearly see that the temp get 17,obj1 = 16,obj2 = 17.The reason is when we try to do this obj2.class_var_shared = 16 it will create a new attribute at the run time in the obj2 instance __dict__ and they get value from there.
# Typically order = obj.__dict__ -> class.__dict__ -> parent.__dict__ -> Attribute error.

# temp.class_var_shared = 17
# print(temp.class_var_shared)
# print(temp.__dict__)

# obj1.class_var_shared = 16
# print(obj1.class_var_shared)
# print(obj1.__dict__)

# print(obj2.class_var_shared)
# print(obj2.__dict__)

# Note = 1. In python , class variable are shared by loopkup not by storage.So if any instance create their own attribute python firstly lookup in their attribute dictionary.
# 2. These above cases valid for all rest of the variable also "_" or "__".
# 3. Never follow this below pattern:
# class temp:
#     _class_var = 10
#     def __init__(self):
#           self._class_var = 15  # never do this.It will create a _class_var at the instace level and also at the class level also.which is bad.If you want to use the class variable inside the class you directly doing like that temp._class_var.
# 

