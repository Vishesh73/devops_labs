# print("hello world")
# print (2+2)

# name = "Vishesh"
# age = 33
# city = "Lalitpur"
# price = 886.12

# print(name, age, city)
# print(type(name))
# print(type(age))
# print(type(city))
# print(type(price))

# #sum
# a = 2
# b = 4
# # sum = a+b
# # print (sum)
# print(a+b)
# print(a-b)
# print(a*b)
# print(a/b)
# print(a%b) #remainder
# print(a**b) #a^b

#relation operators
# a= 50
# b= 20
# print(a == b) #False (equal)
# print(a != b) #True (not equal)
# print(a >= b) #True
# print(a > b) #True
# print(a <=b) #False
# print(a < b) #False

#assignment operators
# num = 10
# num += 10 (#10+10 = 20)
# print(num)

# #Expression Execution String and Numeric *
# A,B = 2, 3
# Txt = "@"
# print (2*Txt*3)

# #Expression Execution String and String + 

# A,B = "Hello", 3
# Txt = "@"
# print ((A+Txt)*B)

# #Expression Execution Numeric values can operate with all arithmetic operators
# A= 2
# B= 3
# C= 4
# print ((A+B)*C)

# #Arithmetic expression with Integer and float will result in float
# A, B = 10, 5.0
# C = A*B
# print (C)

# #Result of division operator with two integers will be float
# A,B = 4,2
# C = A/B
# print (C)

# #Integer division with float and int will give int displayed as float (in this int value will be converted into float and always rounded off with small value for ex 0.5 will be 0.0
# A, B = 1.5, 3
# C = A//B
# print (C)

# """floor gives closest integer, which is less than or equal to the float value
# #Result of (A // B) is same as floor (A/B)"""

# A, B = 12,5
# C= A/B
# print(C)

# A, B = 12,5
# C= A//B
# print(C)

# A, B = -12,5
# C= A//B
# print(C)

# #Remainder (%) is negative whne denominator is negative
# A, B = 5,-2
# C= A%B
# print(C)

# Taking input from user & printing it

# name= input("name - ")
# #print(name)

# age = int(input("age -"))
# price = float(input("price - "))

# print("My name is", name, "and I am", age, "years old")

#Conditional Statements traffic lights code

# light = input ("light : ")
# if(light== "red"):
#     print("stop")
# elif(light=="yellow"):
#     print("look")
# elif(light=="green"):
#     print("go")
# else:
#     print("light is not working")

#Grades fo student
# marks = int(input("marks : "))
# if(marks >= 90):
#     print("A")
# elif(marks>=80 and marks <90):
#     print("B")
# elif(marks >=70 and marks <80):
#     print("C")
# else:
#     print("D")

# #Print output for 

# A=5 
# G = "M"
# A= 2
# G = "F"

# A= int(input("A : "))
# G = input("M/F : ")

# if ((A ==1 or A ==2)and G=="M"):
#     print("fee is 100")
# elif(A==3 or A==4 or G =="F"):
#     print("fee is 200")
# elif(A==5 and G=="M"):
#     print("fee is 300")
# else:
#     print("no fee")

# #Single Line If/Ternary Operator
# #<var>=<val1>if<condition>else<val2>

# food = input("food: ")
# eat = "Yes" if food == "cake" else "no"
# print(eat)

# #Clever If

# salary = float(input("salary: "))
# tax = salary*(0.1, 0.2) [salary<=50000]
# print(tax)



# Program to calculate the year a person was born

# Function to calculate the birth year
# def calculate_birth_year(age, current_year):
#     return current_year - age

# # Get the current year
# import datetime
# current_year = datetime.datetime.now().year

# # Ask the user for their name and age
# name = input("What is your name? ")
# age = int(input(f"Hello (name), how old are you? "))

# # Calculate the birth year
# birth_year = calculate_birth_year(age, current_year)

# # Print a personalized message # Using f-string to embed variables directly into the string
# print(f"Hello, {name}!")
# print(f"Based on your age of {age}, you were born in {birth_year}.")
# print("Hope you're having a great day!")

#Sting indexing
# str = "hello_world"
# print(str[5])

# #Slicing Accessing parts of a string

# #str[ starting_idx : ending_idx] # ending idx (index) in not included
# str = "hello world"
# print(str[1:4])
# print(str[0:len(str)])
# print(str[0:])
# print(str[:5])

# #Negative Index
# str = "hello"
# print(str[-5:-3])

# #Functions
# str= "hello world"
# print(str.endswith("ld")) #True

# str= "hello world"
# print(str.capitalize()) 

# #Replace Function str.replace(old, new)

# str= "hello world"
# print(str.replace("e", "i")) #e replace with i

# #returns 1st index of 1st occurrer str.find(word)
# str = "hello world"
# print(str.find("o")) # index 4
# print(str.find("i")) # i is not available in this string so it will show -1 (invalid index)

# #count function
# str = "hello world"
# print(str.count("l")) # the answer will be 3

# #Write a program user's first name & print it's length
# name = input("name : ")
# print(len(name))
# print(name)

# Print the even/odd number

# num= int(input("enter number: "))
# rem = num%2
# if(rem == 0):
#     print("Even")
# else:
#     print("Odd")


#List and tupple
# import random
# q = [5, 4, 6, 8, 1]
# # Print a random element from the list
# print(random.choice(q))
# # Shuffle the list randomly
# random.shuffle(q)
# print(q)

# q = [2,2,4,1,3,5,1]
# print(q[1:6])
# print(q[0:1])
# print(q[4:6])
# print(q[2:3])
# print(q[5:3]) # This slice is invalid because it goes backward, it will give an empty list
# print([q[6], q[0], q[4], q[2], q[5]])

#List of elements
# lst = [2, 2, 4, 1, 3, 5, 1]

# # Loop through the list to count occurrences
# for num in set(lst):  # Using set to get unique elements
#     count = lst.count(num)  # Count occurrences of each number
#     print(f"{num}:{count}")

# The f before the string indicates that it's an f-string. It allows you to directly insert variables or expressions inside the string by using curly braces {}.
# F-strings were introduced in Python 3.6 and are considered one of the most readable and efficient ways to format strings.

#In list we can assign the value but in string it's not possible
# student = ["ramu", 45, 17.4, "Delhi"]
# print(student[0])
# student[0] = "Ram"
# print(student)

# List menthod append
# list = [2,1,3]
# list.append(5)
# print(list)
# # List menthod sort ascending order
# list = [2,1,3]
# list.sort()
# print(list)

# # List menthod sort descending order
# list = [2,1,3]
# list.sort(reverse=True)
# print(list)

# # List menthod reverse
# list = [2,1,3]
# list.reverse()
# print(list)

# #List method insert
# list = [2,1,3]
# list.insert(1,5) # here 1 in index and 5 is new element
# print(list)

# List menthod remove
# list = [2,1,3,1]
# list.remove(1) # this will remove 1 (first occurrence of element)
# print(list)

# #list method pop
# list = [2,1,3,1]
# list.pop(2) # here 2 is index number so it will remove 3 from the list
# print(list)

# tuple
# tuple = (1,2,5,6)
# print(tuple[0])
# print(tuple[2])
# tuple[0]= 8 # It will show an error tuple and string not support"'tuple' object does not support item assignment"

#tuple index
# tup = (1,3,1,5)
# print(tup.index(3)) # here 3 is element and it will index of 3 is 1
# print(tup.count(1))

#WAP to ask user to enter 3 movies name and store them in a list
# movie1 = input("First movie name is: ")
# movie2 = input("Second movie name is: ")
# movie3 = input("Third movie name is: ")
# list =[movie1, movie2, movie3]
# print(list)

#WAP to check if a list contains a palindrome of elements [1,2,3,2,1]
# list = [1,2,1]

# copy_list = list.copy()
# copy_list.reverse()
# if(copy_list == list):
#     print("Palindrome")
# else:
#     print("Not palindrome")

#Dictionary in python is mutuable(changeable)

# dict = {
#     "name" : "ABC",
#     "learning": ["python","shell"],
#     "age" : 33,
# }
# dict["name"] = "Ram" #overwrite the value
# print(dict["name"])
# print(dict)

#Nested in dictionary

# Student = {
#     "name" : "Deepak",
#     "age" : 22,
#     "subjects" : {
#         "phy" : 88,
#         "chem" : 84,
#         "math" : 82
#     }
# }
# Student.update({"city" : "Delhi"})
# print(Student)
# print(Student["subjects"])
# print(len(Student))
# print(list(Student["subjects"]))
# print(Student.items())

#Set (mutable) in python sets are mutable but element in the sets are immutable
# we can add or remove elements in the set but we can not change the existing element(value) in the set
# num = {1,2,3,3,3, "hello"}
# print(type(num))
# print(num)

#Union & Intersection in set
# set1 = {1,2,3}
# set2 = {2,3,4,5}

# print(set1.union(set2)) # unique value
# print(set1.intersection(set2)) # common value

#Loops in python

# count = 1
# while count <= 100: #stopping condition
#     print(count)
#     count+=1

# count = 5
# while count >= 1:
#     print(count)
#     count -= 1

#print the multiplication table of a number n
# num = int(input("enter number : "))
# count = 1
# while count <= 10:
#     print((num)*(count))
#     count += 1

# print the element of the following list using a loop
# nums = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# index = 0
# while index < len(nums):
#     print(nums[index]) #use square brackets [] for indexing in Python
#     index+=1

#search for a number x in this tuple
# nums = (1, 4, 9, 16, 25, 36, 49, 64)
# x = int(input("enter number: "))
# i = 0
# found = False  # Flag to check if the number is found
# while i < len(nums):
#     if (nums[i] == x):
#         print("found at index", i)
#         found = True  # Set the flag to True when found
#         break  # Exit the loop since the number is found
#     i += 1

# if not found:
#     print("not found")

# continue
# i= 0
# while i <= 5:
#     if(i == 3): #if(1%2 == 0) to print even number and if(1%2 != 0) to print odd number
#         i += 1
#         continue
#     print(i)
#     i += 1
    
#for loop in python

# nums = [1,2,3,45,6]
# for val in nums:
#     print(val)
        
# print the element of the following list using a for loop
# nums = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# for el in nums:
#     print(el)
    
#search for a number x in this tuple
# nums = (1, 4, 9, 16, 25, 36, 49, 64)
# x = int(input("enter number: "))
# i = 0
# for el in nums:
#     if(el==x):
#         print("number found at index", i)
#         i += 1
#         break
#     # else:
#     #     print("not found")

#range
# seq = range(6)
# for i in seq:
#     print(i)

# for i in range (2, 10, 2):  # range(start, stop, step)
#     print(i)

# for i in range (1, 101):  # range(start, stop)
#     print(i)

# for i in range (100, 0, -1):  # range(start, stop)
#     print(i)

#WAP to find the factorial of first n numbers using for and while

# n= 5
# fact = 1
# i = 1
# while i <=n:
#     fact *= i
#     i += 1
#     print ("factorial =", fact)

# n = 5
# fact = 1
# for i in range(1,6):
#     fact *= i
#     print("factorial =", fact)

# functions

# def calcu_sum(a,b):
#     sum = a+b
#     print(sum)
#     return sum
# calcu_sum(5,10)
# calcu_sum(4,8)

# def calcu_avg(a,b,c):
#     sum = a+b+c
#     avg = sum/3
#     print(avg)
#     return avg

# calcu_avg(2,3,2)

# items = ["hi", "hello", "bye"]
# def print_list(items):
#     for i in items:
#         print(i, end = " ")

# print_list(items)

# def convert(usd_val):
#     inr_val = usd_val*83

#     print(usd_val,"USD =", inr_val, "INR")
# convert(10)

#recursive function
# def show(n):
#     if n == 0:
#         return
#     print(n)
#     show(n-1)
# show(5)

# def factorial(n):
#     if (n == 0 or n == 1):
#         return 1
#     return n*factorial(n-1)
# print(factorial(4))

# class student:   #class
#     def __init__(self, name, age, marks): #constructor
#         self.name = name
#         self.age = age
#         self.marks = marks

#     @staticmethod  #decorator work at class level and don't need to pass self
#     def hello():
#         print("hello")

#     def get_avg(self):  #method
#         sum = 0
#         for mark in self.marks:
#             sum += mark
#         print(self.name, self.age, self.marks, sum/3)
    
# s1 = student("ram", 22, [80,87,90]) #object
# s1.get_avg() #calling the method
# s1.hello() #calling the method 


# class account:
#     def __init__(self, name, balance, account_no):
#         self.name = name
#         self.balance = balance
#         self.account_no = account_no

#     def deposite(self, amount):
#         self.balance += amount
#         print("Rs.", amount, "deposited successfully")
#         print("total available balance is", self.balance)

#     def withdraw(self, amount):
#         if amount > self.balance:
#             print("insufficient balance")
#         else:
#             self.balance -= amount
#             print("Rs.", amount, "withdraw successfully")
#             print("total available balance is", self.balance)

#     def get_balance(self):
#         print("current balance is", self.balance)

# a1 = account("ram", 1000, 1234)
# a2 = account("shyam", 2000, 5678)
# a1.deposite(100)
# a1.withdraw(200)
# a1.get_balance()
# a2.deposite(500)
# a2.withdraw(100)
# a2.get_balance()

#private in python
# class account:
#     def __init__(self, account_no, account_password):
#         self.account_no = account_no
#         self.__account_password = account_password   # we can make the variable private by using double underscore( __ )
#         #that mean we can not access the variable (account_password) outside the class
        

# account1 = account(1234, "dhyuw142$") #object
# print(account1.account_no)
# print(account1.__account_password) #it will show an error because we can not access the private variable outside the class

#inheritance in python multiple inheritance
# class A:
#     def __init__(self, type):
#         self.type  = type
#         print("A")
#     varA = "welcome to class A"

# class B:
#     def __init__(self):
#         print("B")
#     varB = "welcome to class B"

# class C(A,B):
#     def __init__(self, type):
#         super().__init__(type) #super() is used to call the constructor of the parent class
#         print("C")
#     varC = "welcome to class C"

# c1 = C("type")

# print(c1.varA)
# print(c1.varB)
# print(c1.varC)
# print(c1.type)

#property decorator

# class student:
#      def __init__(self, name, phy, chem, math):
#          self.name = name
#          self.phy = phy
#          self.chem = chem
#          self.math = math
#      @property
#      def avg(self):
#         return str((self.phy + self.chem + self.math)/3) + "%"

# student1 = student("ram", 80, 90, 85)
# print(student1.avg)

# student1.phy = 90
# print(student1.avg)

#polymorphism in python (one to may form) called operator overloading
# print(1+2) # 3
# print(type(1+2)) # <class 'int'>

# print("hello" + "world") # helloworld "concatenation"
# print(type("hello" + "world")) # <class 'str'>

# print(1.0 + 2.0) # 3.0
# print(type(1.0 + 2.0)) # <class 'float'>

# print([1,2,3] + [4,5,6]) # [1,2,3,4,5,6] merging two list
# print(type([1,2,3] + [4,5,6])) # <class 'list'>

# print((1,2,3) + (4,5,6)) # (1,2,3,4,5,6) merging two tuple
# print(type((1,2,3) + (4,5,6))) # <class 'tuple'>

# random password

import random
import string

password_len = 12

value = string.ascii_letters + string.digits + string.punctuation

password = " "
for i in range(password_len):
    password += random.choice(value)

print("hello user your password is", password)