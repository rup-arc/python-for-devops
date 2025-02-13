#arn = "arn:aws:iam:123456:user/johndoe"
#print(arn.split("/"))

#name= "Rupam"
#print(name.upper())

#str1="hello"
#str2="too"
#result= str1+" "+str2
#print(result)

#text="i am rupam das "
#length= len(text)
#print(length)

#text = "Python is awesome"
#new_text = text.replace("awesome", "great")
#print("Modified text:", new_text)

#text = "Python is awesome"
#words = text.split()
#print("Words:", words)

#text = "   Some spaces around   "
#stripped_text = text.strip()
#print("Stripped text:", stripped_text)

#text = "Python is awesome"
#substring = "is"
#if substring in text:
    #print(substring, "found in the text")

#result= round(3.14159265359, 2)  
#print("Rounded:", result)


#result = abs(-7)
#print("Absolute Value:", result)


#import re
#text = "The quick brown fox"
#pattern = "brown"
#search = re.search(pattern, text)
#if search:
 #   print("Pattern found:", search.group())
#else:
 #   print("Pattern not found")
    
import re
text = "The quick brown fox jumps over the lazy brown dog"
pattern = "brown"
replacement = "red"
new_text = re.sub(pattern, replacement, text)
print("Modified text:", new_text)    

import re
text = "apple,banana,orange,grape"
pattern = ","
split_result = re.split(pattern, text)
print("Split result:", split_result)
    


