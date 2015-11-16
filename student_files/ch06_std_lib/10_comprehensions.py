# dictionary comprehension
data = {'January': 31, 'February': 28, 'March': 31, 'April': 30, 'May': 31, 'June': 30,
        'July': 31, 'August': 31, 'September': 30, 'October': 31, 'November': 30, 'December': 31 }

day31_months = { k:data[k] for k in data if data[k] > 30 }
print(day31_months)



# set comprehension
days_set = {days for days in data.values()}

print(days_set)



# generator expression
g = (k for k in range(400) if k % 9 == 0)
for val in g:
    print(val)