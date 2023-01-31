# 1.1 Evaluate expressions to identify the data types Python assings to Variables
x=True
print(type(x)) #boot

#1.2 Perfomr and analyze data and data type operations
x=2
y="4"
print (x+int(y))

#1.3 Determine the sequence of execution based on a operator precedence

print(3+ 4 * 2)

#2.1 Construct and analyze code segments that use branching statements
letter = "A"
 
if letter == "B":
  print("letter is B")
   
else:
     
  if letter == "C":
    print("letter is C")

#2.2 Construct and analyze code segments that perform iteration
for i in range(10):
    pass

#3.1 Construct and analyze code segments that perform file input and output operations 

open("names.txt") # The relative path is "names.txt"
names_file = open("data/names.txt", "r")

#3.2 Construct and analyze code segments that perform console input and output operations
int ("main() { /* ... */ }")

#5 Analyze, detect, and fix code segments that have errors
#  fro i in range(10):
#  File "<stdin>", line 1
#    fro i in range(10):
# 5.2 Analyze and construct code segments that handle exceptions
def divide(x, y):
    try:
        # Floor Division : Gives only Fractional
        # Part as Answer
        result = x // y
    except ZeroDivisionError:
        print("Sorry ! You are dividing by zero ")
    else:
        print("Yeah ! Your answer is :", result)
    finally: 
        # this block is always executed  
        # regardless of exception generation. 
        print('This is always executed')  
 
# Look at parameters and note the working of Program
divide(3, 2)
divide(3, 0)

#6
# 6.1 Perform basic file system and command-line operations by using built-in modules
import os
print(os.path.join('/test/', '/myfile'))
('myfile')

#4 
#4.2 • Call signatures, default values, return, def, pass
n = 10

if n > 10:
    # write code later

print('Hello')