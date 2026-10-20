def add(*num):
    sum = 0;
    
    for i in num:
        sum += i;
    return sum;

def sub(a,b):
    return (a-b);

def div(a,b):
    return (a/b);

def rem(a,b):
    return (a%b);

def mul(*num):
    ans = 1;
    
    for i in num:
        ans *= i;
    return ans;