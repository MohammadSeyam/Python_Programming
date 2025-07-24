s = input("Enter a string: ")                   # s is string type

a = int(input("Enter a integer: "))             # a is integer type

f = float(input("Enter a float value: "))       # f is float type

print("line separated input sucessfully done\n")



# input multiple variable in single line
n,st,fl = input("Enter 'int string float' in a single line with space separate: ").split()
n = int(n)
st = str(st)
fl = float(fl)


# check type
print(type(n))
print(type(st))
print(type(fl))

print("finished")