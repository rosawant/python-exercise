# Lists: Ordered, mutable and allows duplicate values
mylist  = ["banana", "cherry", "apple"]
print(mylist) 
print(mylist[0]) # banana
print(mylist[-1]) # apple
mylist.append("lemon") #["banana", "cherry", "apple", "lemon"]
mylist.insert(1, "orange") #["banana", "orange", "apple", "lemon"]
mylist.pop() # remove last element
mylist.remove("cherry")
mylist.clear() # [] --> remove all elements
mylist.reverse()
mylist.sort() # This will sort the original list
newlist = sorted(mylist) # This will create a new sorted list

# create empty list , so later you can append items
mylist2 = list()
print(mylist2) # []

# list allows all data types items and also allow duplicates
mylist3 = [2, True, "apple", "apple"]

mylist4 = [0] * 4 # [0, 0, 0, 0]
mylist5 = mylist3 + mylist4 # join two list

# list copy
list_org = ["banana", "cherry", "apple"]
list_cpy = list_org # with this both list refer to same list of memory
list_cpy.append("lemon")
print(list_org) #["banana", "cherry", "apple", "lemon"]
print(list_cpy) #["banana", "cherry", "apple", "lemon"] # changed orignal list as well

# to avoid update the orignal list
#option1
list_cpy = list_org.copy() # with this it will not update original list
#option2
list_cpy = list(list_org)
# option3
list_cpy = list_org[:]