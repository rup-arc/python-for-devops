#count = 0
#while count < 5:
 #   print(count)
  #  count += 1    

   # numbers = [1, 2, 3, 4, 5]
#for number in numbers:
 #   if number == 3:
  #      break
   # print(number)

    #numbers = [1, 2, 3, 4, 5]
#for number in numbers:
 #   if number == 3:
  #      continue
   # print(number)



#automation of a simple log file
log_file = [
    "error:file not found ",
    "file1:secrets",
    "file2:logging to a file",
    "error:not found"
]

for line in log_file:
    if "error" in line:
        print(line)
