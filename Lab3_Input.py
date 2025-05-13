# ENSF 692 Spring 2025
# May 13 Lab 3
# Exercise 3 - Solutions

# Add comments to explain the functionality of this program

# Input Method 1
# Method 1 requests user input of type string using the input command and prints out the string entered by the user 
print('\n')
print("***METHOD 1***")
input1 = input("Please enter your name: ")
print("This is the first input:", input1)
print(f'input1\'s type: {type(input1)}') 


# Input Method 2 
# Method 2 begins an infinite loop requesting input from a user using the input command. Then the output is compared for equality against 
# the letter 'x'. If the input is equal to 'x' then a break command is used to break out of the infinite loop, if they are not equal 
# then the loop goes back to the start and repeats indefinitely until 'x' is input. 
print('\n' * 2)
print("***METHOD 2***")
while True:
    input2 = input("I am looking for specific input. You must type x: ")
    if input2 == "x":
        break
print("This is the second input: " + input2)


# Rewrite Input Method 2 so that no break statement is necessary 
print('\n' * 2) 
print('***Method 2 - Revised***') 
notX = True 
while notX:
    input2 = input("I am looking for a specific input. You must type x:")
    # Check to see if input2 is equal to x
    # If it is equal to 'x': notX changes to false, the loop resets and the while condition evaluates to false and will continue to line 39  
    # If it is not equal to 'x': notX stays true, the loop resets and the while condition evaluates to true and will repeat the loop 
    notX = (input2 is not 'x') 
print("This is the second input: " + input2)

# Key analysis questions 
# How is Method 3 different from the first two input methods? 
#   Method 3 differs from method 1 because it is within a loop to repeat whereas method 1 only executes once 
#   Method 3 differs from method 2 because it does not utilize the break statement to change control flow, it uses the normal loop structure 
# How are the control flow statements used in each example? 
#   No special control flow in method 1, flow executes line by line in order. 
#   Method 2 utilizes while to change control flow to loop through lines 22-25, and uses a break statement to break out of that flow to continue with normal exeecution 
#   Method 3 utilizes while to change contorl flow to loop through lines 33-38, once the condition is met normal flow is continued on line 48 
# What kinds of situations would need you to prompt a user for input and what possible ways can you process that input? 
#   You could prompt a user for input anytime you need data from a user that you can't obtain through other means or needs to be known during runtime 
#   Asking for a password, entering shipping information, prompting for an API key to access data in some way, etc. 
