"""
this is also a comment
"""
# this is a comment
name: str = input("what's your name? ") # variable 
#print("hello, " + name) # prints a string concatenation
#print("hello,", name) # prints the variable as an argument
name = name.title().strip() # capitalize string and strip whitespaces
print(f"hello, {name}") # string interpolation