#(C) 2017 Eugene Vereshchagin.
#Simple Calculator on Python.
#Written on Python 3.6.1
num1 = 0
num2 = 0
def diginput(a):
    while  (a == 0):
       try:
         a = int(input())
         return a
         continue
       except ValueError:
        print ()
        print("Incorrect Value, try again...")

def zerocheck(a):
    while  (a == 0):
       try:
         a = int(input())
         return a
         continue
       except ZeroDivisionError:
        print ()
        print("Divider can't be equal to zero, try again...") 

def calc(operator, num1, num2):

    if operator == '1':
        print(num1)
        print(num1,"+", num2, " = ", num1+num2)
    elif operator == '2':
        print(num1,"-", num2, " = ", num1-num2)
    elif operator == '3':
        print(num1,"*", num2, " = ", num1*num2)
    elif operator == '4':
        print(num1,"/", num2, " = ", num1/num2


print("Enter the first operand:")
num1 = diginput(num1)
print("Choose an operation for calculation")
print ("Print the number and press Enter")
print ()
print ("1 - to add (+)")
print ("2 - to subtract (-)")
print ("3 - to multiply (x)")
print ("4 - to divide (/)")
operator = input()
while (operator != '1' and operator != '2' and operator != '3' and operator != '4'):
      print("Incorrect operator, try again...")
      operator = input()
else:
      print()
print("Enter the second operand:")      
num2 = diginput(num2)

