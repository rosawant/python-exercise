# # ## Example 1
# # def greet(first_name):
# #     return f"{first_name}"


# # name = greet("roshan")
# # print(name)

# # file = open("content.txt", "w") # open file for writing
# # file.write(name) # write to file

# ## example 2
# def increment(increment, by):
#     return increment + by
# print(increment(1,2)) # ans: 3 #without return statement the fuction will return 'None'
# print(increment(1,by=2)) # keyword argument

# # Optional paramater
# def increment(increment, by=1): # <-- setting default value for by paramater
#     return increment + by
# # note1: while calling we dont need to pass value , if it passed from the fucntion call the default valut gets overwirrte
# # note2: optional paramter can only be passed after the requireed parameter like  def increment(increment,number, by=1) not possible like  def increment(increment, by=1, number)

# xargs --> can pass n number of arguments

def multiply(*numbers):
    print(numbers)

multiply(2,3,4,5)