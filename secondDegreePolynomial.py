from sympy import *
import random

def print_box(content):
    content_str = f"║ {content} ║"
    width = len(content_str)
    print("▀" * 50) 
    print("╔" + "═" * (width - 2) + "╗")
    print(content_str)
    print("╚" + "═" * (width - 2) + "╝")

def targetFunction():
    X = symbols('X')
    F = X**2 * (X-5)
    return (X,F)

def targetFunctionSub(sub):
    X,F = targetFunction()
    return F.subs(X,sub)

def function():
    a,b,c,X = symbols('a b c X')
    f = a * X**2 + b * X + c
    return (a,b,c,X,f)

def functionSubX(sub):
    a,b,c,X,f = function()
    return f.subs(X,sub)

def functionSubABC(subA,subB,subC):
    a,b,c,X,f = function()
    return f.subs({a : subA, b : subB, c : subC})

def makeEquasion(x):
    return Eq(functionSubX(x),targetFunctionSub(x))

def twoSmallest(x1,x2,x3):
    smallest = min(x1,min(x2,x3))
    secondSmallest = float('inf')
    if smallest == x1:
        secondSmallest = min(x2,x3)
    elif smallest == x2:
        secondSmallest = min(x1,x3)
    elif smallest == x3:
        secondSmallest = min(x1,x2)
    return (smallest,secondSmallest)

def SDPM(beginning=0, ending=0, iteration=1, x1=-1, x2=-1, x3=-1, preXBar=float('inf'), ebsilon=0.000001):


    print_box(f"iteration: {iteration}")
    iteration += 1

    if x1 == -1 and x2 == -1 and x3 == -1:
        x1 = random.uniform(beginning, ending)
        x2 = random.uniform(beginning, ending)
        x3 = random.uniform(beginning, ending)

    eq1 = makeEquasion(x1)
    eq2 = makeEquasion(x2)
    eq3 = makeEquasion(x3)
    print(f"x1: {x1}\nx2:{x2}\nx3: {x3}\neq1: {eq1}\neq2: {eq2}\neq3: {eq3}")
    
    a,b,c,X,f = function()
    solution = linsolve([eq1,eq2,eq3],(a,b,c))

    xBar = -list(solution)[0][1]/(2*list(solution)[0][0])

    smallest,secondsmallest = twoSmallest(x1,x2,x3)

    print("."*30)
    print(f"xbar = {xBar}")
    print("."*30)

    if abs(preXBar-xBar) > ebsilon:
        return SDPM(iteration=iteration,x1=xBar, x2=smallest, x3=secondsmallest,preXBar=xBar)
    else:
        return xBar


print(f"min: {SDPM(beginning=1,ending=7)}")