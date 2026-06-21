# number = 100
# while number > 0:
#     print(number)
#     number //= 2 # this is euivalent number // 2 
# # note: number /2 will retuen true values with floating number while number //2 gives roundup value
# # 100
# # 50
# # 25
# # 12
# # 6
# # 3
# # 1

# ## Example 2
# command = ""

# while command.lower() != "quit":
#     command = input(":>")
#     print("Echo", command)

## Infinite loop
while True:
    command = input(":>")
    print("Echo", command)
    if command.lower() == "quit":
        break
