
list1 = ['pen','paper','book','pen','iPhone', 231, 20.10, True]
        #  0,     1,      2,    3,    4,        5,  6,     7

print(list1)
# access with index (ordered)
print(f'first value in the list is {list1[0]}')
print(f'second value in the list is {list1[1]}')
print(f'third value in the list is {list1[2]}')
print(f'fourth value in the list is {list1[3]}')
print(f'fifth value in the list is {list1[4]}')
print(f'sixth value in the list is {list1[5]}')
print(f'seventh value in the list is {list1[6]}')


print(list1)
list1[3] = 'Hero Pen'
print(list1)

# to add at the end position
list1.append('Ford')
print(list1)

list1.insert(5,'iPad')
print(list1)
list1.insert(5,'pen')
print(list1)
print(list1.pop())
print(list1)

list1.remove("pen")
print(list1)

list1.pop(2)
print(list1)

# del list1
print(list1)

list1.remove
