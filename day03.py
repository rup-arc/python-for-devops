#function,modules and packages   python workspaces or virtual environment 

def adition(num1,num2):
    a=num1+num2
    return a 

def substraction(num1,num2):
    s=num1-num2
    return s 

def multui(num1,num2):
    m=num1*num2
    return m 

num1 = float(input("Enter the first number: "))  
num2 = float(input("Enter the second number: "))


print(f"Addition of {num1} and {num2} is: {adition(num1, num2)}")    
print(f"Subtraction of {num1} and {num2} is: {substraction(num1, num2)}")    
print(f"Multiplication of {num1} and {num2} is: {multui(num1, num2)}")
