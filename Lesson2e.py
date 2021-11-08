
# dictionaries
# dictionaries store key - value

mydictionary = {
    'make':'Toyota',
    'model':'Vitz',
    'reg': 'KCD445D',
    'cost': 5000000
}

print(mydictionary)
print(mydictionary['model'])

# update
mydictionary['cost'] = 600000
print(mydictionary)

# adding
mydictionary['color'] = 'silver'
print(mydictionary)

# delete
del mydictionary['reg']
print(mydictionary)

del mydictionary
print(mydictionary)