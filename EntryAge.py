
age = input("How old are you:")

if age == type(str):
    if age:
        age = int(age)
        if age >= 18 and age < 21:
            print("You can enter, but need a wristband!")
        elif age >= 21:
            print("You are good to enter and can drink")
        else:
            print("You can't come in, little one! :(")
    else:
        print("please, enter the age.")
else:
    print("Please, enter the number.")