
#Definition for Conditional Statements
# 'if'   some codition is True
#        do something
# 'elif' some other condition is True:
#        do something
# 'else':
#        do something



#Example of conditional statements
name = input("Write the name:")

if name == "Konrad":
    print("you are the best")
elif name == "Marek":
    print("You aren't Konrad")
else:
    print("Carry on")

#'is' operator is equal '==' operator
print("\n")
a=1
print(a==1)
print(a is 1)

if a is 1:
    print("'is' operator is equal '==' operator")