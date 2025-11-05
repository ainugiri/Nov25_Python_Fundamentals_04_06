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