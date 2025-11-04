t1 = ('Giri','Prasanth','Mohammed','Rose','Giri')
print(t1[2])
# enrolled[2] = 'Afzal'
print(t1)

temp_list = list(t1)
temp_list[2] = 'Afzal'
t1 = tuple(temp_list)

print(t1)

t2 = ('A','B', 'C')

t3 = t2 * 2

print(t3)