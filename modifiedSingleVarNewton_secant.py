from sympy import *

def print_box(content):
    content_str = f"║ {content} ║"
    width = len(content_str)
    print("▀" * 50) 
    print("╔" + "═" * (width - 2) + "╗")
    print(content_str)
    print("╚" + "═" * (width - 2) + "╝")

def f():
    X = symbols("X")
    F = X**2*(X-5)
    return (X,F)

def fsub(sub):
    X,F = f()
    return F.subs(X,sub)

def fPrime():
    X,F = f()
    return (X,diff(F,X))

def fPrimeSub(sub):
    X,F = fPrime()
    return F.subs(X,sub)

def SM(initialGuess1=0,initialGuess0=0,iteration=0, previousX = float('inf'),prePreviousX=float('inf'), ebsilon = 0.00001):
    print_box(f"iteration: {iteration}")
    iteration +=1

    newX = float('inf')
    if iteration == 1:
        newX = initialGuess1 - (initialGuess1-initialGuess0)*fPrimeSub(initialGuess1)/(fPrimeSub(initialGuess1)- fPrimeSub(initialGuess0))
        print(f"X{iteration-2} = {initialGuess1}\nX{iteration-1} = {initialGuess0}\nX{iteration} = {newX}")
        previousX, prePreviousX = newX, initialGuess1
    else:
        newX = previousX - (previousX-prePreviousX)*fPrimeSub(previousX)/(fPrimeSub(previousX)- fPrimeSub(prePreviousX))
        print(f"X{iteration} = {newX}")
        previousX, prePreviousX = newX, previousX


    if abs(prePreviousX - previousX) > ebsilon:
        return SM(iteration=iteration,previousX=previousX,prePreviousX=prePreviousX,ebsilon=ebsilon)
    else:
        return previousX

print(f"min: {SM(initialGuess0=2.5,initialGuess1=2.6)}")