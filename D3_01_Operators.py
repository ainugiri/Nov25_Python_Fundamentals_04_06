# Aritmentic 
x = 1000
y =  10

print(f"Addition {x + y}")
print(f"Subtraction {x - y}")
print(f"Multiplication {x * y}")
print(f"Division {x / y}")
x = 1028
print(f"Floor Division {x // y}")
print(f"Modulus  {x % y}")
x =100
print(f"Exponent (power) {x ** 2}")


# relational (llt <, le <=, gt >, ge >=, eq ==, ne !=)
inp = int(input("User :"))
x = inp % 7

# conditional state : simple if else
if x == 0:
    print(f"The modulus value 0, and the given input is divisible by 7")
elif x < 5:
    print(f"The modulus value is less than 5 and the value is :{x}")
elif x >= 5:
    print(f"The modulus value is greater than 5 and the value is :{x}")



# fenner india pvt
# motor belt
# speed and distance motor and pulling point : decide 
#  speed : 100 rpm
#  dist : 30 cm
#  type1

speed = int(input("Enter the motor speed :"))
dist = int(input("Enter the distance : "))
if speed >= 100 and dist == 30:
        print("AND: type1d30 model")

if speed >= 100 or dist == 30:
        print(speed >= 100, dist == 30, speed >= 100 or dist == 30  )
        print("OR: type1d30 model")

# truth table   con1    con2        
#               inp1    inp2        AND      OR      Not(ip1)
#               True    True        True    True    False
#               True    False       Fail    True    False
#               False   True        Fail    True    True
#               False   False       Fail    False   True

# assignment 
x  = 1001
x += 1      # 1002
x = x + 1   # 1003
x -= 1
print("x -= 1", x)
x *= 2
print("x *= 2", x)
x /= 3
print("x /= 3", x)


l1 = ['MacBook', 'Dell Tab', 'Hp NOteBook', 'iPhone', 'Abc','Xyz']
userinp = input("Check list with requirement : ")
x = userinp in l1
if x is True:
      print(f"The item, {userinp} is availble in the list")
else: 
      print("The item, {userinp} is not availble in the list")