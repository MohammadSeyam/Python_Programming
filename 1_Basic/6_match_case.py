a = int(input("enter a number: "))

match(a):
    case 1:
        print("You select 1")
    case 2:
        print("You select 2")
    case 3:
        print("You select 3")
    case 4:
        print("You select 4")
    case 5:
        print("You select 5")
    case _:
        print("You selected less than 1 or greater than 5")

