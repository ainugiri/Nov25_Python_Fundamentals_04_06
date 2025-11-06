# l1 = ['Java','Python', 'JS','CSS','React','SQL','1',2,3,4,5,6,7]
# for x in l1:
#     print("Welcome")

# for x in l1:
#     print(x)


# for i in range(10):
for i in range(1,11):
    print(i)

i = 0
noofoccurance = int(input("User : "))
while i <= noofoccurance:
    i += 1
    if i == 3:
        continue
    else:
        print(f"{i} Welcome")
    

print("EOF")