x = int(input("User : "))
# if x > 9:
#     print(True)
# else:
#     print(False)

if x > 95:
    print("Grade: A+")
elif x >= 90:
    print("Grade: A")
elif x >= 80:
    print("Grade: B")
elif x >= 70:
    print("Grade: C")
elif x >= 60:
    print("Grade: D")
elif x >= 50:
    print("Grade: E")
else:
    print("Grade: Fail")


if x >= 50:
    y = int(input("Attendance Percentage"))
    if y > 75:
        print("Cleared")
    else:
        print("Not Cleared")




# Match - Case ==== Switch Case

day = int(input("Kindly select the day for booking, 0 - Sunday, 1 -Monday,...."))
match day:
    case 1:
        print("Thank you for your booking on Monday ")
        op1 = int(input("Kindly select 0 - Breakfast, 1 -Lunch, 2- Dinner...."))
        match op1:
            case 0:
                print("Thank you for your booking on Monday for breakfast")
            case 1:    
                print("Thank you for your booking on Monday for lunch")
            case 2:    
                print("Thank you for your booking on Monday for Dinner")
            case _:
                print("Thank YOU, Kindly try again")

    case 2:
        print("Thank you for your booking on Tuesday ")
    case 3:
        print("Thank you for your booking on Wednesday ")
    case 4:
        print("Thank you for your booking on Thursday ")
    case 5:
        print("Thank you for your booking on Friday ")
    case 6:
        print("Thank you for your booking on Saturday ")
    case 0 :
        print("Thank you for your booking on Sunday ")


# for loop and while loop
#  for (i = 0; i<=10; i++){
#   printf(i)
# }
print("FOR LOOP")
for i in range(10): # 0 1 2 3 4 5 6 7 8 9
    print(i)
