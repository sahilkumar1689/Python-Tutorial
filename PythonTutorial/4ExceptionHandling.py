# We can easily handle the exception using the try-except block in python.

try:
    a = input("Enter number:");
    b = input("Enter another number");
    
    if(a == 0):
        raise Exception("Please enter non zero Number."); # we can also raise custom errors.
    
    if(b == 0):
        raise ZeroDivisionError; 
    
    print(a/b);
    
except Exception as e:
    print("Error is:",e);
else:
    print("After Try");
finally:
    print("Always Run on no matter what.");