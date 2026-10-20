def add(*args):
    return sum(args)

def sub(*args):
    if len(args) == 0:
        return 0
    elif len(args) == 1:
        return args[0]
    else:
        result = args[0]
        for num in args[1:]:
            result -= num
        return result
    
def mul(*args):
    result = 1
    for num in args:
        result *= num
    return result

def div(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b