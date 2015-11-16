from collections import defaultdict

d1 = defaultdict(str)
d1['greet1'] = 'hello'
print(d1['greet1'])     # works as expected
print(d1['greet2'])     # not valid, invokes the str() constructor as a result


string_val = 'she sells seashells by the seashore'
d2 = defaultdict(int)

for ch in string_val:
    d2[ch] += 1              # initially d[ch] will be an error, default value from int() which is zero will be used

for k,v in d2.items():
    print('{k}:{v}'.format(k=k, v=v))
