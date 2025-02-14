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


#so i am facing bproblem while installing boto3 so there are some commands to install it 
-----pipx install boto3 --include-deps
#and here are some extra command to how to create  diff virtual environment in a machine
pipx install virtualenv
python3 -m venv project_2   # create project in venv
source project_2/bin/activate  # go to th virtual env to do some work 
pipx install jira # installing some dependencies
deactivate # deactivatting the vnv
