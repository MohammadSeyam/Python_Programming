list1 = [1,5,6,4,2,3,2]

# 1: reverse()
list1.reverse()
print(list1)

# 2: sort()  , ascending
list1.sort()
print(list1)

# 3: sort(reverse=True)  , descending
list1.sort(reverse=True)
print(list1)

# 4: append   ,insert at last
list1.append(10)
print(list1)

# 5: pop()     ,remove last element
list1.pop()
print(list1)

# 6: access with negative index
print(list1[-1])    # last element

# 7: count()     ,count element
print(list1.count(2))

# 8: insert(index, value)    , insert at specific index
list1.insert(1,100)
print(list1)

# 9: remove()   ,remove the first occurrence 
list1.append(100)
list1.remove(100)
print(list1)

# 10: pop(idx)   ,remove element from a specific index
list1.pop(4)
print(list1)

# 11: count()    , count the occurrence of element
print(list1.count(4))

# 12: copy
list2 = list1.copy()
print(list2)

# 13: slicing   ,same as string.slice()
print(list1[1:4])
