# Pyhton Sets 

# defining a set 
# set is a collection of unique values 
# we can use it when we know all the values will be uniqie and order of the data is not metters

s = set()
# adding item to set
s.add(1)
s.add(2)
s.add(3)
s.add(4)
# trying to add duplicate 
s.add(3)


# removing item from set 

s.remove(2)

print(s)


# print the length of set

# f"" is formated string
print(f" set has {len(s)} elements")