#Calculator
import os
from logo import logo1


def add(n1,n2):
    return n1+n2
def subtract(n1,n2):
    return n1-n2
def multiply(n1,n2):
    return n1*n2
def divide(n1,n2):
    return n1/n2
def exponent(n1,n2):
    return n1**n2
operations={
    '+':add,
    '-':subtract,
    '*':multiply,
    '/':divide,
    '**':exponent
    }  

def calculator():
    print(logo1) 
    num1=float(input("What's the first number ? \n"))
    for i in operations:
        print(i)
    flag=True
    while flag:
        op=input("Pick an operation: \n")
        num2=float(input("What's the next number ? \n"))
        # ans=0
        # if op=='+':
        #     ans=add(f_no,n_no)
        # elif op=='-':
        #     ans=subtract(f_no,n_no)
        # elif op=='*':
        #     ans=multiply(f_no,n_no)
        # elif op=='/':
        #     ans=divide(f_no,n_no)
        # else:
        #     print("Invalid Input")
        calculation_func=operations[op]
        ans=calculation_func(num1,num2)
        print(f"{num1} {op} {num2} = {ans}")
        if input(f"Type 'y' to continue calculating with {ans} and 'n' to stop here : ").lower() =="y":
            num1=ans
        else:
            flag=False
            os.system('CLS')
            calculator()
calculator()