x = 100
y = 101
z = 102

print(x,y,z)

x, y, z = 101, 'Giri', False
print(x,y,z)

tup1 = (101,112,123)
print(f"tup1[0] : {tup1[0]} ")
print(f"tup1[1] : {tup1[1]} ")
print(f"tup1[2] : {tup1[2]} ")

# tup1[0] = 1001


# modify the tuple; convert to list -> changes -> convert into tuple

templist = list(tup1)
templist[2] = 1001
tup1 = tuple(templist)

print(tup1)

templist = list(tup1)

templist.append(2025)
print(templist)

slice1 = templist[0:3]
print(f"Slice1 : {slice1}")
templist = [1,2,3,4,5,6,7,8,9,10,1,2,3,4,5,1,2,3,4,5,6,7,8,9,10]
print(templist)

slice1 = templist[0:3]
print(f"Slice1 : {slice1}")

slice2 = templist[-3:]
print(f"Slice1 : {slice2}")

slice3 = templist[1::2]
print(slice3)

slice4 = templist[::2]
print(slice4)

slice3 = templist[-5::2]
print(slice3)

tup1 = tuple(templist)
print(tup1)

s_t1 = tup1[::3]
print(s_t1)


print(f"The occurance of 1 : {tup1.count(1)}")
print(f"The occurance of 9 : {tup1.count(9)}")

print(f"The index of 9 : {tup1.index(9)}")