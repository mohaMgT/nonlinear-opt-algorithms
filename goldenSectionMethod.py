from sympy import *

def print_box(content):
    content_str = f"║ {content} ║"
    width = len(content_str)
    print("▀" * 50) 
    print("╔" + "═" * (width - 2) + "╗")
    print(content_str)
    print("╚" + "═" * (width - 2) + "╝")

def function():
    X = symbols('x')
    F = X**2 + 2*X
    return (X,F)

def function_sub(sub):
    X,F = function()
    return F.subs(X,sub)

def checkABOrder(a,b):
    if a > b:
        temp = b
        b = a
        a = temp
    return a,b

def GSM(a,b,alpha,ebsilon,iteration):
    print_box(f"iteration = {iteration}")
    iteration += 1

    a,b = checkABOrder(a,b)
    if (b-a) > ebsilon:
        

        lamda = a + (1-alpha)*(b-a)
        mu = a + alpha*(b-a)
        print(f"a = {a}\nb = {b}\nlambda = {lamda}\nmu = {mu}\n")

        if function_sub(lamda) > function_sub(mu):
            print("****************")
            print(f"f(lamda) = {function_sub(lamda)}\nf(mu)    = {function_sub(mu)}")
            print(f"f(lamda) > f(mu)\n a = {lamda}\nb = {b}")
            print("****************")

            a = lamda
            b = b
            return GSM(a,b,alpha,ebsilon,iteration)
        else:
            print("****************")
            print(f"f(lamda) = {function_sub(lamda)}\nf(mu)    = {function_sub(mu)}")
            print(f"* f(lamda) <= f(mu)\na = {a}\nb = {mu}")
            print("****************")
            a = a
            b = mu
            return GSM(a,b,alpha,ebsilon,iteration)

    else:
        return (a+b)/2

print(f"result: {GSM(a=-3,b=5,alpha=0.618,ebsilon=0.2,iteration=0)}")
print(function())