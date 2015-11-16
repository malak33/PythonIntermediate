from itertools import accumulate, chain, islice, permutations, count

items = [1, 2, 3, 4, 5, 4, 4, 3, 4, 5, 2, 0, 7, 4, 5, 6]
accumulator = accumulate(items)
print(list(accumulator))                   # [1, 3, 6, 10, 15, 19, 23, 26, 30, 35, 37, 37, 44, 48, 53, 59]


list1 = [1, 2, 3]
list2 = [4, 5, 6]
list3 = [7, 8, 9]
chained_list = chain(list1, list2, list3)       # chained list is an iterator, not a new list
print(list(chained_list))                       # [1, 2, 3, 4, 5, 6, 7, 8, 9]


statement = 'she sells seashells by the seashore'
print(''.join(islice(statement, 10, 19)))               # seashells


statement = 'python'
depth = 2
print([''.join(combo) for combo in permutations(statement,depth)])


for c1, c2 in zip(range(0, 10), count(0, 0.25)):
    print(c1, c2)