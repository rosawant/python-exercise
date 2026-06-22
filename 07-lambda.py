# lambda arguments: expressions

add_10 = lambda x: x + 10
print(add_10(5)) # 15

# example 2 - multiple arg
mul = lambda x,y: x*y
print(mul(2,3)) #6

# example 3
points2D = [(1, 2), (15, 1), (5, -1), (10, 4)]
sorted_2D = sorted(points2D) #[(1, 2), (5, -1), (10, 4), (15, 1)] # this by default sort with the x element from (x,y)
print(sorted_2D)

sorted_2D_with_y = sorted_2D = sorted(points2D, key=lambda x: x[1])
print(sorted_2D_with_y) # [(5, -1), (15, 1), (1, 2), (10, 4)]

##map(lambda argument: expression, iterable)

a = [1, 2, 3, 4, 5]
b = map(lambda x: x*2, a)
print(list(b)) #[2, 4, 6, 8, 10]
# OR
b = [ x*2 for x in a ] ##[2, 4, 6, 8, 10] #better apprach easy to understand

## filter(func, seq)
a = [1, 2, 3, 4, 5, 6]
even_num = filter(lambda x: x%2 == 0, a)
print(list(even_num)) #[2, 4, 6]

## reduce(func, seq)
from functools import reduce
a = [1, 2, 3, 4]
product_a = reduce(lambda x,y: x*y, a)
print(product_a) #24 --> 1*2--> 2*3--> 6*4-->24
