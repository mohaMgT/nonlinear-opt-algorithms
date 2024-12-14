from sympy import *

def print_box(content):
    content_str = f"║ {content} ║"
    width = len(content_str)
    print("╔" + "═" * (width - 2) + "╗")
    print(content_str)
    print("╚" + "═" * (width - 2) + "╝")

def print_brace(title, a, b):
    width = max(len(str(a)), len(str(b))) + 4
    print(f" {title.center(width)}")
    print(" " + " " * (width // 2) + "⎧")
    print(f" a = {a}".ljust(width + 2))
    print(" " + " " * (width // 2) + "⎪")
    print(f" b = {b}".ljust(width + 2))
    print(" " + " " * (width // 2) + "⎩")


def function():
    X = symbols('X')
    F = X**2
    return (X,F)

def function_sub(sub):
    X,F = function()
    return F.subs(X,sub)

def functionPrime():
    X,F = function()
    return (X,diff(F,X))

def functionPrimeSub(sub):
    X,F = functionPrime()
    return F.subs(X,sub)

def bisection(a,b,ebsilon,iteration):
    print("▀" * 50)    
    print_box(f"iteration = {iteration}")
    iteration += 1

    if abs(a-b)> ebsilon:    
        x = (a+b)/2
        print(f"a == {a}\nb == {b}\nx == {x}")
        
        fPrimeOfX = functionPrimeSub(x)

        if fPrimeOfX < 0:
            print(f"**********************\nf'(x) < 0\n**********************\na = {x}\nb = {b}")
            a = x
            b = b
            return bisection(a,b,ebsilon,iteration)
        elif fPrimeOfX > 0:
            print(f"**********************\nf'(x)> 0\n**********************\na = {a}\nb = {x}")
            a = a
            b = x
            return bisection(a,b,ebsilon,iteration)
        else:
            print("**********************\nf'(x) = 0\n**********************")
            return x
    else:

        return (a+b)/2


print(f"result: {bisection(a=-11,b=8,ebsilon=0.0000001,iteration=0)}")
print(f"f  : {function()}")
print(f"f' : {functionPrime()} ")