import random
# random number
a = random.random() #0.719208072450777 random float
b = random.uniform(1,10) #9.918495407789427 between range 1 to 9
c = random.randint(1,10) 
d = random.randrange(1,10) # this will never include 10, it will print number from 1 to 9

# random from list
mylist = list("ABCDEF")
a = random.choice(mylist) # print random character from given list
b = random.sample(mylist, 3) #['E', 'B', 'A']  print random 3 char from list
c = random.choices(mylist, 3) # it will print single elemets multiple time
d = random.shuffle(mylist)

#######


