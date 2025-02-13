# Variable Scope and Lifetime
##Local Scope: 
#def my_function():
 #   x = 10  # Local variable
  #  print(x)
#my_function()

#Global Scope 
#y = 20  
#def another_function():
 #   print(y)  
#another_function()
#print(y)  

#Using Variables to Store and Manipulate Configuration Data in a DevOps Context 
# Define configuration variables for a web server
server_name = "my_server"
port = 80
is_https_enabled = True
max_connections = 1000

print(f"Server Name: {server_name}")
print(f"Port: {port}")
print(f"HTTPS Enabled: {is_https_enabled}")
print(f"Max Connections: {max_connections}")

port = 443
is_https_enabled = False

print(f"Updated Port: {port}")
print(f"Updated HTTPS Enabled: {is_https_enabled}")