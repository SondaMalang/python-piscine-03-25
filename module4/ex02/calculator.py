
#!/usr/bin/python3

num1 = int(input("Give me the first number: "))
num2 = int(input("Give me the second number: "))


added = num1+num2
difference = num1-num2
quotient=int(num1/num2)
product= num1*num2

if type(num1) == int and type(num2) == int:
 print("Thank you!","\n",
       num1,"+",num2,"=",added,"\n",
       num1,"-",num2,"=",difference,"\n",
       num1,"/",num2,"=",quotient,"\n",
       num1,"*",num2,"=",product,"\n")

else:
 print("Please enter a number")

