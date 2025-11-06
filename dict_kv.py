# data -> em : dasid, name, doj, loc, 
# e1 _> dasid: a825662, name: Giri, doj: 2021, loc: CH, IN

e1 = {
    "DasID":"A825662",
    "Name" : "Giri Prasad ",
    "DOJ" : "2021",
    "Technologies" : ["Java","MySQL","React","Python","DevOps","Cloud"]
}

print(e1)
print(e1.keys())
print(e1.values())
e1["DOJ"] = "2019"
print(e1.items())
print(e1["Name"])

if "DOJ" in e1:
    print("Yes, It is available as a key in the e1")
else:
    print("No is not available as a key in the e1")

e1["mobile"] = 918231
print(e1)

# e1.pop("mobile")
# print(e1)


# e1.popitem()
# print(e1)

# del e1["mobile"]
# print(e1)

# del e1
# print(e1)
for item in e1:
    print(e1[item])

for item in e1.values():
    print(item)


for k,v in e1.items():
    print(k,v)

e1.clear()
print(e1)


dic1 = dict()
print(type(dic1))

dic1 = {
    "key1": "value1",
    "key2": "value2",
    "key3": "value3",
    "key4": "value4",
    "key5": "value5",
}

print(dic1["key1"], dic1["key5"])


dic1 = {
    "key1": "value1001",
    "key1": "value1002",
    "key1": "value1005",
    "key1": "value1004",
    "key1": "value1003",
}



print(dic1["key1"])


dic2 = {
    "a":1,
    "b":2,
    "c":3,

}

print(dic2)

# remove -> empty
dic2 = {}
print(dic2)

dic3 = dict(x = 10, y = 25, z = 30, p=202, q = 2032)
print(dic3)
print("dic3['x']", dic3['x'])
print(dic3.get('y',"Not Found"))
print(dic3.get('a',"Not Found"))

dic3['y'] = 205
print(dic3.get('y',"Not Found"))
del dic3["q"]
print(dic3)

print(dic3.pop("p"))
print(dic3)

dic4 = dict()
dic4.update(dic3)
print(dic4)


dic5 = dict(name = 'Giri', Loc = 'Chennai', WF='Home', Mob=982)
print(dic5)



dic6 = dict(Dept = 'Tesing', Head = 'XYZ', ProCode='Pid:10201')
print(dic6)

dic5.update(dic6)
print(dic5)