# Colletions: counter, namedtuple, OrderedDict, defaultdict, deque
# from collections import Counter
# a = "aaaabbbcc"

# my_counter = Counter(a)
# print(my_counter) #Counter({'a': 4, 'b': 3, 'c': 2})
# print(my_counter.keys()) #dict_keys(['a', 'b', 'c'])
# print(my_counter.values()) #dict_values([4, 3, 2])
# print(my_counter.most_common(1)) #{'a': 4}
# print(my_counter.most_common(2)) #{'a': 4, 'b': 3} #gives list of most common key-value
# print(my_counter.most_common(1)[0]) #('a', 4)
# print(my_counter.most_common(1)[0][0]) #a
# print(list(my_counter.elements())) #['a', 'a', 'a', 'a', 'b', 'b', 'b', 'c', 'c']


# ### NamedTuple
# from collections import namedtuple

# Point = namedtuple('Point','x,y')
# pt = Point(1,4)
# print(pt) #Point(x=1, y=4)
# print(pt.x) #1

### OrderedDict
from collections import defaultdict

d = defaultdict()
d['a'] = 1
d['b'] = 2
print(d['a']) #1
print(d['c']) #0 --> 'c' is not present to it returns default 0
# with normal dict, list it would have given error
# d = defaultdict() --> returns 0
# d = defaultdict(float) --> returns 0.0
# d = defaultdict(list) --> returns []

#deque --> double ended queue, it will remove elements from both side
from collections import deque
d = deque()

d.append(1)
d.append(2)
print(d) #deque([1, 2])
d.appendleft(3) #deque([3, 1, 2])
d.pop() #deque([3, 1])
d.popleft() ##deque([1, 2])
d.extend([4,5,6]) #deque([3, 1, 2, 4, 5, 6])
d.extendleft([4,5,6]) #deque([6, 5, 4, 3, 1, 2, 4, 5, 6])
d.clear() # clear all dict
