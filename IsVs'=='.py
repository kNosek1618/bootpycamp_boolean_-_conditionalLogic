
#"is Vs. '==' operator

#example when 'is' operator is equal '==' operator
a=1
print(a==1)
print(a is 1)

if a is 1:
    print("Example when 'is' operator is equal '==' operator\n")


x = [1, 2, 3]
y = [1, 2, 3]

if x == y:
    print("x list is equal y list but,")
else:
    print("x list isn't equal y list but,")

if x is y:
    print("x list is y list.")
else:
    print("x list isn't y list.")
