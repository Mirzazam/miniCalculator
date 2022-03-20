# this function is to add

def add():
    return num1+num2

# this function is for substraction

def sub():
    return num1-num2

#to multiply the numbers:
def mul():
    return num1*num2

#to divide the numbers:
def div():
    return num1/num2

#to divide the numbers:
def per():
    return num1/num2*100

#to divide the numbers:
def inc():
    return num1*2.54
    

print("Type in the option and press ENTER:\n")
print("Select 1 for Addition")
print("select 2 for Sub")
print("select 3 for Multiply")
print("select 4 for Division")
print("select 5 for Percentage")
print("select 6 for 'Inch to CM conversion'")
while True: 
    a = int(input("\nEnter your choice: "))
    if a == str or a > 6:
        a = print("Enter a valid choice (re-run the program to start) ")
        break
    
    if a == 1:
        num1 = float(input("Enter the number: "))
        num2 = float(input("Enter the value: "))
        print("The sum of the given numbers is: ", add())
    elif a == 2:
        num1 = float(input("Enter the number: "))
        num2 = float(input("Enter the value: "))
        print("The sub of the given numbers is: ", sub())

    elif a == 3:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        print("The product of the given numbers is: ", mul())

    elif a == 4:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        print("The quotient of the given numbers is: ", div())

    elif a == 5:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        print("The percentage of the given numbers is: ", per())

    elif a == 6:
        num1 = float(input("Enter the number: "))
        print("The values of the given numbers is: ", inc(),"Cm")

    next = input("\nDo you want to perform next calculation? 'yes' or 'no': ")
    if next == 'no':
        print("\nThank you for using the Mini cal, hope you liked it!")
        break


