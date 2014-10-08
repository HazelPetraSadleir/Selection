#Hazel Petra Sadleir
#08-10-2014
#Selection Class Exercise

#Revision Exercise n4

number1 = int(input("Please enter number1: "))
number2 = int(input("Please enter number2: "))
if number1>number2 :
    print("Number1 is larger than number2")
elif number2>number1 :
    print("Number2 is larger than number1")
else:
    print("Number1 and number2 are the same")

number3 = int(input("Please enter number3: "))
if number1>number2 and number1>number3 :
    print("Number1 is the largest")
elif number2>number1 and number2>number3:
    print("Number2 is the largest")
else:
    print("Number3 is the largest")
