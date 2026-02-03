# print("heejdfeihfuehfefhihfillp")
# str"jayansh\tgupta"
# print(str[-5 : -2])

# strinput("enter second name: ")
# print(str)
# print(len(str))

# str"i ave $ the $ the power $"
# print(str.count("$"))

# marksint(input("Enter your marks: "))
# if(marks > 90):
#    grade"A"
# elif(marks <90 and marks>80):
#     grade"B"
# elif(marks < 80 and marks > 70):
#     grade"C"
# else:
#     grade"D"

# print("the grade od student is ",grade)    

# if(num %20):
#     print("its even")
# else:
#     print(":its odd")

# aint(input("enter second number:  "))
# bint(input("enter second number:  "))
# cint(input("enter third number:  "))
# if(a>b and a>c):
#     print(a,"a is greatest")
# elif(b>c):
#     print(b,"b is greatest")
# else:
#     print(c,"c is greatest")


# list=[]
# list.append(input("Enter first fav movie: "))
# list.append(input("Enter second fav movie: "))
# list.append(input("Enter third fav movie: "))
# print(list)


# list=["m","a","a","m"]
# copy_list=list.copy()
# copy_list.reverse()
# if(list==copy_list):
#     print("Palindrome")
# else:
#     print("Not palindrome")


# grade=("A","B","C","D","A","D","C","B","A","D","CB","D","A","A")
# print(grade.count("A"))


# dict = {
#     "name": "jayansh Gupta",
#     "age": 22,
#     "subject": ["java","python","html","css"],
#     "topics": ("dictionary","set"),
#     "cgpa": 6.5,
#     33 : False,
# }
# print(dict["cgpa"])
# print(dict["subject"])
# dict["name"]="jayansh" #its is immutable 
# print(dict)

# null_dict={}  #this is empty dictionary

# dict1={
#     "table":["a piece of furniture","lists of facts and figiures"],
#     "cat": "a small animal"
# }
# print(dict1)

# set={"python","c++","java","python","c++"}
# print(len(set))

# physics=int(input("enter marks: "))
# chemistry=int(input("enter marks: "))
# math=int(input("enter marks: "))
# student_marks={}
# student_marks["physics"]=physics
# # or student_marks.update({physics: physics})
# student_marks["chemistry"]=chemistry
# student_marks["math"]=math
# print(student_marks)

# p={
#     ("float",9.0),
#     ("int",9)
# }
# print(type(p))

# a=int(input("enter n "))
# i=1
# while(i<=10):
#     print(i*a)
#     i +=1
# list=[1,4,9,16,25]
# idx=0
# while(idx<len(list)):
#     print(list[idx])
#     idx +=1

# list=(1,4,9,16,25)
# idx=0
# x=16
# while idx<len(list):
#     if(list[idx]==x):
#         print("Found",x,"at index ",idx)
#         break
#     else:
#         print("finding")
#     idx +=1

# list=(1,4,9,16,25)
# for val in list:
#     print(val)

# for el in range(10):
#     print(el)

# for el in range(2,10):
#     print(el)

# for el in range(2,21,2):
#     print(el)

# n=int(input("Enter no. "))
# for i in range(1,11):
#     print(n*i)

# for el in range(10):
#     pass       #make null loop

#sum of n natural numbers
# n=int(input("enter n number: "))
# i=1
# count=0
# while i<=n:
#     count +=i
#     i+=1
# print(count)

# #factorial of n natural numbers
# n=int(input("Enter n number: "))
# i=1
# ans=1
# for i in range(1,n+1):
#     ans *= i
# print(ans)

#function
# cities=["mumbai","kolkata","delhi","gwalior","pune"]
# def city(list):
   
#     for el in list:
#         print(el,end=" ")
# city(cities)

# print(end="\n")

# def odd_even(n):
#     if(n%2==0):
#         print("Even")
#     else:
#         print("Odd")
# odd_even(51)

# def converter(usd_val):
#     Inr=usd_val*83
#     print(usd_val,"usd = ",Inr,"INR")
# converter(10)

#Recursion
# def rec(n):
#     if(n==0):
#         return 0
#     return rec(n-1)+n
# print(rec(5))

# #2
# def print_list(list,idx=0):
#     if(idx==len(list)):
#         return
#     print(list[idx])
#     print_list(list,idx+1)
# list=[2,5,3,7,9,3]
# print_list(list)


