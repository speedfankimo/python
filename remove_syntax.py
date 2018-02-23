#n.pop(index) will remove the item at index from the list and return it to you:
n = [1, 3, 5]
# Remove the first item in the list here
n.pop(0)
print n


#n.remove(item) will remove the actual item if it finds it:

n = [1, 3, 5]
n.remove(5)
print n


#del(n[1]) is like .pop in that it will remove the item at the given index, but it won't return it:
n = [1, 3, 5]
del(n[0])
print n

