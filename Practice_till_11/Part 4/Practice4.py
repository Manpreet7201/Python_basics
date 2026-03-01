# Find the key with maximum value.
myDict = {'Manpreet': 95.0, 'Kiran': 85.0, 'Japneet': 75.56}
max_key = None
max_value = 0
for key in myDict:
    if myDict[key] > max_value:
        max_value = myDict[key]
        max_key = key

print(max_key)
print(max_value)