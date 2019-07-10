
#"is Vs. '==' operator

#example when 'is' operator is equal '==' operator
a=1
print(a==1)
print(a is 1)

if a is 1:
    print("Example when 'is' operator is equal '==' operator\n")

#example when 'is' operator it's different
x = [1, 2, 3]
y = [1, 2, 3]
z = y

if x == y:
    print("x list is equal y list but,")
else:
    print("x list isn't equal y list and,")

#x and y variables is different because the list is object
#the objects is not be equal
if x is y:
    print("x list is y list.")
else:
    print("x list isn't y list.")

#'is' is only truthy if the variables reference the same item in memory.
if y is z:
    print("y is z because this is a copy of the list.")


