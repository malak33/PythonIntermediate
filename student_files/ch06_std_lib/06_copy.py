from copy import deepcopy

lst1 = ['hello','goodbye',['buenos','dias']]

lst2 = deepcopy(lst1)

lst2[2][1] = 'noches'
lst2[0] = 'hola'

print(lst1)
print(lst2)
