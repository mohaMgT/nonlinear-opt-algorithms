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

def fprimePrime():
    X,F = fPrime()
    return (X,diff(F,X))

def fPrimePrimeSub(sub):
    X,F = fprimePrime()
    return F.subs(X,sub)

def SVN(initialGuess=0,iteration=0, previousX = float('inf'), ebsilon = 0.00001):
    print_box(f"iteration: {iteration}")
    iteration +=1

    newX = float('inf')
    if iteration == 1:
        newX = initialGuess - fPrimeSub(initialGuess)/fPrimePrimeSub(initialGuess)
        print(f"X{iteration-1} = {initialGuess}\nX{iteration} = {newX}")
    else:
        newX = previousX - fPrimeSub(previousX)/fPrimePrimeSub(previousX)
        print(f"X{iteration} = {newX}")


    if abs(newX - previousX) > ebsilon:
        return SVN(iteration=iteration,previousX=newX,ebsilon=ebsilon)
    else:
        return previousX

print(f"min: {SVN(initialGuess=2.5)}")