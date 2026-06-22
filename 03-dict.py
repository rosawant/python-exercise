# Dictionary: Key-value pairs, unorderd, Mutable
mydict = {"name":"roshan", "age":20, "city":"pune"}
mydict = dict(name="roshan", age=20, city="pune") #{"name":"roshan", "age":20, "city":"pune"}

value = mydict["age"] #20
mydict["email"] = "roshan@example.com" #{"name":"roshan", "age":20, "city":"pune", "email":"roshan@example.com"}
mydict["email"] = "sawant@example.com" #{"name":"roshan", "age":20, "city":"pune", "email":"sawant@example.com"}

# delete
del mydict["name"] #{"age":20, "city":"pune", "email":"sawant@example.com"}
mydict.pop("name")
mydict.popitem() # removes last entry

# loops
for key in mydict:
    print(key) # returns keys
#or
for key in mydict.keys():
    print(key) # returns keys
# name
# age
# city
for value in mydict.values():
    print(value) # returns value

for key, value in mydict.items():
    print(key, value) # returns both

# copy dict
new_dict = mydict  # both original and new dict gets updated
new_dict["email"] = "roshan@example.com" 

print(mydict) 
print(new_dict)
new_dict = mydict.copy() # this will create new and not modify the original
new_dict = dict(mydict)


mydict = {"name":"roshan", "age":20, "city":"pune"}
mydict_1 = dict(name="roshan", age=28, city="pune", email="roshan@example.com")

mydict.update(mydict_1) # {'name': 'roshan', 'age': 28, 'city': 'pune', 'email': 'roshan@example.com'}
# this will overwite the exsiitng elemets and adds the new one

