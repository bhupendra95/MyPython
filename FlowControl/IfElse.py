
# WAP accept a intger number and check the given number is +ve or -ve no.

n = input("Enter a number : ")

if n > 0:
    print(n, " is a +ve number")
else:
    print(n, " is -ve number")

####################################################################
# write a script accept a number and check the given number is an Even
# or Odd number
n = input("Enter a number : ")
if n % 2 == 0:
    print(n, " is an Even number")
else:
    print(n, " is an Odd number")

###########################################################
# write a script accept a number and check the given number is 3 digit
# or not
n = input("Enter a number : ")
if n >= 100 and n <= 999:
    print(n, " is a 3 digit number")
else:
    print(n, " is not a 3 digit number")

#############################################################
# Login program

uname = input("Enter username : ")
pwd = input("Enter password : ")

if uname == "admin" and pwd == "python":
    print("Welcome to Python Class")
else:
    print("Invalid username or password")

#########################################################
# Guess number program

n = input("Enter guess number [1-10] :")

if n == 3:
    print("Wow. your guess is correct. you done great job")
else:
    print("Sorry. your is guess wron.better luck next time")

##########################################################
# Guess number program
import random

n = input("Enter guess number [1-10] : ")
x = random.randint(1, 10)

if n == x:
    print("Wow. ypur guess is correct. you done great job")
else:
    print("Sorry. your is guess wrong.better luck next time")

##############################################################

# write a script accept 2 number's and find greast number
a = input("Enter a number 1 : ")
b = input("Enter a number 2 : ")
if a != b:
    if a > b:
        print(a, " is big")
    else:
        print(b, " is big")
else:
    print("given 2 numbers are equal")


# Write a scrpt accept empno,ename,job and salary and calculate bonus
# based on the following condtions
# job       bonus
# manager    20% on ann_sal
# analyst    18% on ann_sal
# programmer 15% on ann_sal
# salesman   12% on ann_sal
# others     10% on ann_sal

empno = input("Enter a  empno : ")
ename = input("Enter a ename : ")
job = input("Enter a job : ")
sal = input("Enter a salary : ")
ann_sal = sal * 12

if job == "manager":
    bonus = int(ann_sal) * 20 / 100
elif job == "analyst":
    bonus = int(ann_sal) * 18 / 100
elif job == "programmer":
    bonus = int(ann_sal) * 15 / 100
elif job == "salesman":
    bonus = int(ann_sal) * 12 / 100
else:
    bonus = int(ann_sal) * 10 / 100

print("#" * 33)
print("###   Employee Bonus Report  ####")
print("-" * 30)
print("###   Employee Number  : ", empno, " ###")
print("###   Employee Name    : ", ename, " ###")
print("###   Employee Job     : ", job, " ###")
print("###   Employee Salary  : ", sal, " ###")
print("###   Employee AnnSal  : ", ann_sal, " ###")
print("###   Employee Bonus   : ", bonus, " ###")
print("-" * 33)
print("#" * 33)