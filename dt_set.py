l1 = [1,23,4]
t1 = tuple(l1)
print(l1)
print(*l1)
print(t1)

for items in l1:
    print(items)
l2 = [98,101]
l1.append(l2)
print(l1)


set1 = {2,4,6,1,9,1,2,4,6,1,9,1}
set2 = {1,3,5,7,9,2,4}
set3 = {4,5,6,7}

allgames = set3.intersection(set2).intersection(set1)
print(allgames)


allgames = set2.intersection(set3)
print(allgames)

tennisonly = set2 - set1 - set3
print(tennisonly)


onlytennis_onlyvoll = set1 ^ set2
print(onlytennis_onlyvoll)




set4 = {"a2","a19","a12"}
set4.remove("a19")
print(set4)
# set4.remove("a19")
print(set4)

set4 = {"a2","a19","a12"}
print(set4)
set4.discard("a19")
print(set4)
set4.discard("a19")
print(set4)