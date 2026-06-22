# Tuple : orderd, immutable , allows dupliate elements
mytuple = ("banana", 2, "max")
#or
mytuple = "banana", 2, "max"
mytuple = tuple(["banana", 2, "max"]) #("banana", 2, "max")

# acecssging tuple elements is similar to list
mytuple[1] # 2

mytuple[1] = 4 # ERROR --does not suport item asignment
# Note: tuple with single element will not be recognised as tuple 
mytuple = ("max")
type(mytuple) # string 
# to fix this
mytuple = ("max",)
type(mytuple) # tuple 

mytuple = ("a","p","p","l","e")
mytuple.count("a") #1
mytuple.index("l") #3
mylist = list(mytuple) # covert tuple to list
