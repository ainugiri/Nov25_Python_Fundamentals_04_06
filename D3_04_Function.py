# access_modifier return_type functionname (argu){
# -------------
# ---------
# ---------
# }

# functionname(arguments)


def functionname():
    print("You called the function, following inst")
    print("stmt1")
    print("stmt2")
    print("stmt3")
    print("stmt4")
    print("stmt5")
functionname();



def welcome(username="Guest"):
    print(f"Hi {username}, Welcome to the training program")

welcome("Giri");
welcome("Steve");
welcome();

def addition(a,b=1):
    return a/b

print(addition(100))

s_area = lambda a : a * a
c_area = lambda x : 3.14 *x * x

print(c_area(7))
print(s_area(10))