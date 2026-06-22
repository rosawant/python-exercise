# Sets : unordered, mutable, no duplicates 
myset = {1, 2, 3}
myset = {1, 2, 3, 1, 2} #{1, 2, 3}
myset = set([1,2,3]) ##{1, 2, 3}

myset = set("Hello") #{'e', 'o', 'H', 'l'}

# Create empty set
myset = {} # this will create dict type
myset = set() # this will create correct empty set
myset.add(1)
myset.add(2)
myset.add(2)

print(myset) # {1, 2, 3}
myset.remove(3) #{1, 2} # it will remove element and gives error if element not present
myset.discard(3) # if removed the elements and doesnt give error if out of set element add to remove
myset.clear()
myset.pop()

# union
odds  = {1, 3, 5, 7}
even = {2, 4, 6, 8}
prime = {2, 3, 5, 7}
new = odds.union(even) #{1, 2, 3, 4, 5, 6, 7, 8}
common_val = odds.intersection(prime) #{3, 5, 7}
diff = even.difference(prime) #{8, 4, 6}

# Subset
setA = {1, 2, 3, 4, 5, 6}
setB = {1, 2, 3}
print(setA.issubset(setB)) # False
print(setB.issubset(setA)) # True
print(setA.issuperset(setB)) # True

