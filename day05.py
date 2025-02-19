#import os 
  
#print(os.getenv("password"))    # in terimal u have to use this export password="Rupam"

#my_list = [1, 2, 3, 4, 5]

# Identity operators
#a = my_list
#b = [1, 2, 3, 4, 5]

#is_same_object = a is my_list
#is_not_same_object = b is not my_list

# Membership operators
#element_in_list = 3 in my_list
#element_not_in_list = 6 not in my_list

#print("a is my_list:", is_same_object)
#print("b is not my_list:", is_not_same_object)
#print("3 in my_list:", element_in_list)
#print("6 not in my_list:", element_not_in_list)




import sys 

# Get the type from command line argument
instance_type = sys.argv[1]
# Compare the input string to 't2.micro'
if instance_type == "t2.micro":
    print("Creating EC2 for you")
elif instance_type == "t2.large":
     print("iyt will charge u 4 dollar/month")  
elif instance_type == "t2.medium":
     print("iyt will charge u 3 dollar/month")         
else:
    print("Your input is incorrect, please give t2.micro, t2.medium,t2.large")


coordinates = (3, 4)
x, y = coordinates  # Unpack the tuple into x and y (x=3, y=4)