#For printing clearly.
blank = '    '
# Strings, lists, tuples, and maps.

string = 'This is a string.'
list = ['This', 'is', 'a', 'list.']
tuple = ('This', 'is', 'a', 'tuple.')
map = {'1' : 'This',
'2' : 'is',
'3' : 'a',
'4' : 'map.'}

# The following uses for loops in order to print a the last 3 var types.

for i in range(len(list)):
    print(list[i])

print(blank * 20)

for i in range(len(tuple)):
    print(tuple[i])

print(blank * 20)

for i in range(len(map)):
    print(map[str(i+1)])

# List Arithmetic
l1 = [1, 2, 3, 4]
l2 = ['word1', 'grape']
print(l1 + l2)