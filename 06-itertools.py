# itertools : product, permutations, combinations, accumulate, groupby and infinite iterators
## Product
from itertools import product
a = [1, 2]
b = [3]

prod = product(a,b) #[(1, 3), (2, 3)]
prod = product(a,b, repeat=2) #[(1, 3, 1, 3), (1, 3, 2, 3), (2, 3, 1, 3), (2, 3, 2, 3)]

## Permutations
from itertools import permutations
a = [1, 2, 3]
perm = list(permutations(a)) #[(1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 1, 2), (3, 2, 1)]

## combinations
from itertools import combinations
a = [1, 2, 3, 4]
comb = combinations(a,2)
print(list(comb)) #[(1, 2), (1, 3), (1, 4), (2, 3), (2, 4), (3, 4)]

## accumulate
from itertools import accumulate
a = [1, 2, 3, 4]
acc = accumulate(a)
print(list(acc)) #[1, 3, 6, 10]

#option2
from itertools import accumulate
import operator
a = [1, 2, 3, 4]
acc = accumulate(a, func=operator.mul)
print(list(acc)) #[1, 2, 6, 24]

# option 3 
from itertools import accumulate
import operator
a = [1, 2, 5, 3, 4]
acc = accumulate(a, func=max)
print(list(acc)) #[1, 2, 5, 5, 5]  --> 5 is max from 3, 4

## Groupby
from itertools import groupby
def smaller_than_3(x):
    return(x < 3)

a = [1, 2, 3, 4]
group_obj = groupby(a, key=smaller_than_3)
for key, value in group_obj:
    print(key,list(value))
# True [1, 2]
# False [3, 4]
# option 2
from itertools import groupby

a = [1, 2, 3, 4]
group_obj = groupby(a, key=lambda x: x<3)
for key, value in group_obj:
    print(key,list(value))
# True [1, 2]
# False [3, 4]

## count, cycle , repeat
# count
from itertools import count, cycle, repeat
for i in count(10):
    print(i) # this will count infinately
    if i == 15:
        break # the count will stop at 15
# cycle
from itertools import count, cycle, repeat
a = [1, 2, 3]
for i in cycle(a):
    print(i)  # it will lopp infinately through the list 

# repeat
from itertools import count, cycle, repeat
for i in repeat(1):
    print(i)  # it will print 1 infinitely

from itertools import count, cycle, repeat
for i in repeat(1,4):
    print(i)  # it will print '1' 4 times