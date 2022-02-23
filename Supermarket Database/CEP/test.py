
# Q#1

def add(x,y):
    a = x/y
    print(a)

add(3,3)

print("\n")
      
# Q#2

def check(func):
    
    def wrapper(x,y):
        if y==0:
            print("Divisor is zero")
        else:
            func(x,y)
    return wrapper

@check
def add(x,y):
    a = x/y
    print(a)


add(3,0)

























##def print_X(func):
##    def wrapper():
##        print("XXXXX")
##        func()
##        print("XXXXX")
##    return wrapper
##
##def print_Y(func):
##    def wrapper():
##        print("YYYYY")
##        func()
##        print("YYYYY")
##    return wrapper
##
##@print_X
##@print_Y
##def func():
##    print("Hello")
##    
##func()
