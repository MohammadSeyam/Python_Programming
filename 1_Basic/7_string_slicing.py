s = "practice makes a man perfect"

# string[start : stop : step ]  default step is 1;

# case:1
print(s[5:10])  # char of index 10 will not be printed

# case: 2
print(s[ :10])  # first to index 9

# case: 3
print(s[10: ])  # index 10 to last

# case: 4
print(s[2: : 3])  # every third char from index 2 to last


# string can be access with negative index 