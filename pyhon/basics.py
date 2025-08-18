#print("hiii");print("helo")
#sum of two number using initiallisation.
# a=45;b=78
#print(`sum of ${a} and ${b} = ${a+b}`)#cann't we use like this because in python bactics are not support to use string and expression simultaneously.
# print(f"The sum of {a} and {b} = {a+b}")
#sum of two numbers using users input.
# num1=int(input("Enter ist number="))#we need to give the data type of user input because python automatically takes user input as string even you give any number.
# num2=int(input("Enter 2nd number="))
# print(f"The sum of {num1} and {num2} = {num1+num2}")
# num=input("Enter ist number=")#we need to give the data type of user input because python automatically takes user input as string even you give any number.
# num1=input("Enter 2nd number=")
# print(f"The sum of {num} and {num1} = {num+num1}")
# a=45
# b=4.567
# c="vashi"
# d=False
# print(a,type(a))
# print(b,type(b))
# print(c,type(c))
# print(d,type(d))
###use explicit data type.
# a=23
# decimal=float(a)
# print(decimal,type(decimal))
# string=str(a)
# print(string,type(string))
# b=3.456
# decimal1=int(b)
# print(int(decimal1),type(decimal1))
# c="4"
# string1=int(c)
# print(int(string1),type(string1))
############list ( List is used to store the data of multiple data type . It is a mutable and we use [])
#####list method()(1.slice,count,unpacking,repeat list,sum,indexing,length)
# a=["vashi",23,True,4.9876]
# print(a,type(a))
# print(a[1])
# a[2]="asd"
# print(a)
# list=[2,"vashi",2,3.3345,True,2]
# print(list)
# list[1]="asd"
# print(list)
# print(list[1:3])
# print(list*2)#repeat list
# print(list.count(2))#count the elements in the list
# print(list.index(2))#it will give the index of starting first value idex no matter if you are using multiple times
# a,b,c,d,e,f=list#unpacking the elements
# print(a,b,c,d,e,f)
# print(len(list))
# str="yeevashi"
# print(str,type(str))
# print(str.find(" "))#find is used to detect the space no matter it is aingle,double,etc space if you write find(" ") it will detect single space and find("  ")it will detect double space.
# print(str.find("  "))

# str="yeevashi \nKumari"
# print(str)
#tuple.
# data1=(5,)
# print(data1,type(data1))
# data=("vashi",23,True,4.9876)
# print(data,type(data))
# print(data[2])
# print(data[1])
# data[0]="riya"
#tuple method
# tuple=(1,2,3,"vashi",23,2,4,3,23)
# print(tuple.count(2))#count method
# data=tuple.count("vashi")
# print(data)
# tuple.count(23)
# print(tuple)#it will print original value of tuple because tuple is immutable
# print(tuple.index("vashi"))#we used index to find the index of particular value.
# print(tuple.index(2))#here 2 is present at 2 times in a tuple but tuple find the index of starting 2 no matter if you are using 1 times or multiple times
# tuple1=("riya",34,True,3.234)
# tuple2=("asd",35,False,4.5678)
# result=tuple1+tuple2#concatenat the tuple
# print(result)
# print(tuple1*3)#print tuples in multiple times
# print(result*4)
# tuple3=(2,"rahul",4.56,True)
# print(len(tuple3))#length of tuple
# print(tuple3[1:3])#slice method
# a,b,c,d=tuple3# unpacking method
# print(a,b,c,d)
#List(is mutable )
#practice set
# fruits=[]
# fruit1=input("enter 1st fruit name")
# fruits.append(fruit1)
# fruit2=input("enter 2nd fruit name")
# fruits.append(fruit2)
# fruit3=input("enter 3rd fruit name")
# fruits.append(fruit3)
# fruit4=input("enter 4th fruit name")
# fruits.append(fruit4)
# print(fruits)
# fruit5=input("enter 5th fruit name")
# fruits.append(fruit5)
# fruit6=input("enter 6th fruit name")
# fruits.append(fruit6)
# fruit7=input("enter 7th fruit name")
# fruits.append(fruit7)
# print(fruits)
# marks=[]
# mark1=int(input("enter m1"))
# marks.append(mark1)
# mark2=int(input("enter m2"))
# marks.append(mark2)
# mark3=int(input("enter m3"))
# marks.append(mark3)
# mark4=int(input("enter m4"))
# marks.append(mark4)
# mark5=int(input("enter m5"))
# marks.append(mark5)
# mark6=int(input("enter m6"))
# marks.append(mark6)
# print(marks.sort())#for sorting to do like this is supporting  it's will be none.So don't do like this
# marks.sort()
# print(marks)
#problem 4
# tuple=(1,"asd",True)
# tuple[2]="vashi"
# print(tuple)
#problem 5(to sum the list)
# list=[23,34,21,56]
# print(sum(list))
# #or
# a,b,c,d=list
# print(a,b,c,d)
# sum=a+b+c+d
# print(sum)
#problem 6
# tuple=(2,3,0,4,0,5,6,0,3,0,0)
# print(tuple.count(0))
###Dictionary it is a mutable
# name={
#     "Harry":34,
#     "Vashi":90,
#     "Ram":49,
#     "rahul":[23,35,75]

# }
# print(name,type(name))
# print(name.keys())# to find the keys from dictionaries
# print(name.values())# to find the value from dictionaries
# print(name["Vashi"])# to access the value of vashi
# name["Ram"]="asd"# to chane the value of Ram
# print(name["rahul"])
# name["rahul"]="riya"
# print(name)
# name["Ram"]=50
# name["reena"]=60 #add new value on existing dictionaries
# print(name)
# name.update({"rahul":70 , "yeevashi":40})#update method 
# print(name)
# print(name.get("yeevashi"))# get() is used to get the value of key within dictionary
# print(name["yeevashi"]) # this is also used to get the value of key within dictionary
# ## to understand the difference between line number 156 and 157 then write like this...
# print(name.get("yeevashi1"))# output will be none
# print(name["yeevashi1"])## output will be key error.
# employee={
#     "name":"vashi",
#     "age":43,
#     "role":"Frontend",
#     "company":"google"
# }
# # print(employee,type(employee))
# # print(employee.keys())
# # print(employee.values())
# # print(employee["name"])
# # employee["name"]="yeevashi"
# # print(employee)
# # employee.update({"company":"google","Location":"Mysore"})
# # print(employee)
# employee["role"]="backend"
# print(employee)
# employee["company"]="Amazon"
# print(employee)
# employee.update({"salary":80000})
# print(employee)
# print(employee.get("company"))
# print(employee["company"])
# print(employee.get("company1"))
# print(employee["company1"])
###set (It is an unordered,cann,t access element by index,set cann't contain duplicate value)
# s={}#it's type is dictionary
# print(s,type(s))
# b=set()#it's type is set
# print(b,type(b))
# print(s,type(s))
# a={"vashi",23,34,3,23,34,True,2.234}
# print(a,type(a))
# a.add("riya")
# print(a)
# a.remove(True)
# # a.clear()
# # print(a)
# print(len(a))
# s1={23,89,"rahul","riya",True,4.345}
# s2={"priya",2,False,1.2900,89,"rahul"}
# print(s1.union(s2))
# print(s1.intersection(s2))
# print(s1-s2)
# print(s1.subset(s2))
###########list practice (mutable,You can manipulate with existing item but you cann't add extra item in existing list)
#####(1.slice,count,unpacking,repeat list,sum,indexing,length)
# list=[24,"riya",5.3456,True,2,3,2,3,2,3,24,5.3456]
# print(tuple,type(list))
# list[0]=456; list[3]=False
# print(list)
# list1=[23,354,876,3,23,65,92]
# print(f"the sum of all item in list1 = {sum(list1)}")
# print(list.count(3))
# print(list[3:11])
# a,b,c,d,e,f,g,h,i,j,k,l=list
# print(a,b,c,d,e,f,g,h,i,j,k,l)
# print(list*2)#repeat list 
# print(len(list))
# print(list.index(3))
# list3=[]
# f1=input("enter fruit f1")
# list3.append(f1)
# f2=input("enter fruit f2")
# list3.append(f2)
# f3=input("enter fruit f3")
# list3.append(f3)
# f4=input("enter fruit f4")
# list3.append(f4)
# list3.sort()
# print(list3)
###########tuple(It is immutable)
# tuple=(1,2,5,"puja",3.190,2,4)

# print(tuple,type(tuple))
# print(tuple[0])
# print(tuple[3:5])#slice method.
# a,b,c,d,e,f,g=tuple####unpacking
# print(f"a={a}, b={b}, c={c}, d={d},e={e},f={f}, g={g}")
# print(len(tuple))
# print(tuple.index("puja"))
# print(tuple.count(2))
######dictionary
# dict={
#     "name":"yeevashi",
#     "course":"computer",
#     "role":"Data scientist"
# }
# print(dict.keys())
# print(dict.values())
# print(dict,type(dict))
# print(dict["role"])
# dict["course"]="BCA"
# dict.update({"Location":"Pune","salary":50000})
# print(dict)
#####set
# set=set()#empty set
# print(set,type(set))
# s={"yeevashi",34,True,False,34,"yeevashi",23.4556,34,True,False}
# s1={"riya",34,23,True}
# print(s)
# print(s.union(s1))
# print(s.intersection(s1))
# print(s-s1)
# If,elif.else statement
# num=int(input("enter any number"))
# if(num>18):
#     print("adult")
# elif(num>30):
#     print("young")
# elif(num>60):
#     print("old")
# else:
#     print("child")
#  loop(for loop,while loop)for loop
# for i in range(0,100):
#     print(i)
#     for num in range(0,100,4):
#         if num==50:
#             break
#         print(num)
# list=["vashi",23,3.12333,23,"vashi",23]
# print(list.count(23))
# print(list.index("vashi"))
# print(list[1:4])
# list[0]="yeevashi"
# print(list)
# list1=[23,1,2,3,4]
# print(sum(list1))
# list.append("asd")
# print(list)
# a,b,c,d,e,f=list
# print(f"a={a}, b={b}, c={c}, d={d}, e={e}, f={f}")
# print(len(list))
# print(list*4)
# list2=[]
# num1=int(input("Enter your n1"))
# list2.append(num1)
# num2=int(input("enter n2="))
# list2.append(num2)
# num3=int(input("enter n3="))
# list2.append(num3)
# num4=int(input("enter n4="))
# list2.append(num4)
# list2.sort()
# print(list2)
# tuple=("vashi",23,3.123,True,23)
# print(tuple,type(tuple))
# print(tuple[0])
# print(tuple*2)
# print(tuple.count("vashi"))
# print(tuple.index(23))
# print(len(tuple))
# print(tuple[1:3])
# dictionary={
#         "name":"vashi",
#         "age":23,
#         "course":"bca"
# }
# print(dictionary,type(dictionary))
# print(dictionary.values())
# print()
# print(dictionary["course"])
# dictionary["name"]="rahul"
# dictionary.update({"location":"pune"})
# print(dictionary)
# a=()
# print(a,type(a))
# s=set()
# print(s,type(s))
# s1={"vashi",23,34,True,3.1234,23,True}
# s2={"asd",23,True,32}
# print(s1)
# print(s1-s2)
# print(s1.union(s2))
# print(s1.intersection(s2))
#########control structure(flow,control,looping,jumping statement)
# flow control(if,if else,if elif)
# num=int(input("enter any number="))
# if(num<=30):
#     print("D grade")
# elif(num<=50):
#     print("C Grade")
# elif(num<=70):
#     print("B Greade")
# elif(num<=80):
#     print("A Grade")
# elif(num<=90):
#     print("O Grade")
# else:
#     print("Fail")
#####looping(while,for)
# print 1-100
# num=int(input("enter any number="))
# while(num<=100):
#     print(num)
#     # num++ (python doesn't support prefix and postfix(increment,decrement))
#     num=num+1
####print 1-100 with skip 2-number like 1,3,5,7,9,11...etc
# num=int(input("enter any number="))
# while(num<=100):
#     print(num)
#     num=num+2
####print(table of any number)
# num=int(input("enter any number="))
# while(num<=100):
#     if(num%5==0):
#         print(num)
#     num=num+1
#####for loop(print1-100) syntax(for variable in range(starting_number,ending_number,step_number))step_number can be optional
# for i in range(1,100):###here stoping_number is not includable because it half-open like this([))
#     print(i)
# for num in range(1,100,3):
#     print(num)
###we can use else in looping(while,for) .So why we can use else in loop because when only our while,for condition will be executed without any break 
# num=int(input("enter any number="))
# while(num<=50):
#     print(num)
#     num=num+1
# else:
#     print("All number is executed successfully")
# for i in range(1,50,2):
#     print(i)
# else:
#     print("for loop executed sucessfully")

# if we are use break in while else,for else loop then else statement will not be executed because of break keyword, it will termnate our current code
# num=int(input("enter any number="))
# while(num<=50):
#     if(num==4):
#         break
#     print(num)
#     num=num+1
# else:
#     print("All number is executed successfully")
# for i in range(1,50,2):
#     if(i==5):
#         break
#     print(i)
# else:
#     print("for loop executed sucessfully")
# foods_item=["banana","mango","litchi","kela","potato","tomato"]
# for food in foods_item:
#     print(food)
# data=["ramban","fruits","vegetable",23,14,True,3.123]
# print(data,type(data))
# for packet in data:
#     print(packet)
# data1=("fastfood",["fruits","kela"],"vegetable",67,14,False,3.123)
# print(data1,type(data1))
# for info in data1:
#     print(info)
# data3={
#     "name":"vashi",
#     "roll":34,
#     "course":"bfs"
# }
# print(data3,type(data3))
# for info1 in data3:
#     print(info1 )
# print(data3.values())
###check tthe vowel and consonent on given string also count the vowel
# str="yeevashikumarisharma"
# count=0
# for char in str:
#     if(char=="a"or char=="e" or char=="i"or char=="o" or char=="u"):
#         count=count+1
#         print(f"character={char}")
    
# print(f"vowel is present in string={count}")
###reverse the string
# str="yeevashi"
# print("reverse yeevashi",str[::-1])###reverse by character
# str1="niharika sharma"
# print("niharika sharma",''.join(str1.split()[::-1]))
# print()
#########list(,insert,append,extend,pop,remove,slice,count,sum,index,reverse,clear,sort)
# list=["banana","mango","strawberry","orange","kiwi","avacado"]
# list.insert(2,"jaamun")
# print(list)
# list.sort()
# print(list)
# list.pop()
# print(list)
# list.append(["kela,sev,santra"])
# print(list)
# list.extend(["panner","pakoda","palak","kimchi"])
# print(list)
# # list.remove("strawberry")
# if "strawberry" in list:
#     list.remove("strawberry")
# else:
#     print("strawberry not found on list")
# print(list)
# print(list[2:5])
# list.reverse()
# print(list)
# list.clear()
# print(list)

# for data in list:
#     print(data)
####tuple
# tuple=(34,45,5,6,76,54)
# print(tuple[1:5])
# print(tuple.count(34))
#####Function
# def greet():
#     return("Good morning!!")
# data=greet()
# print(data)
# ####write a programme to add two  umbers.
# num1=int(input("enter num1="))
# num2=int(input("enter num2="))
# def sum():
#     return num1+num2, num1-num2, num1*num2
# add=sum()
# print(f" {num1} + {num2} = {num1+num2} , {num1}-{num2}={num1-num2}, {num1}*{num2}= {num1*num2}")
# def plus(a,b):
#     return(f"The ssum of {a} and {b}= {a+b}")
# info=plus(5,8)
# print(info)
##fibonacci series
# a=0
# b=1
# print(f"{a}\n{b}")
# for i in range(8):
#     temp=a+b
#     print(temp)
#     a=b
#     b=temp
# count=0
# for i in range(11):
#     count=count+i
# print(f"The sum of {i} = {count}")
##########function
# def greet(hello="name"):
#     print(hello)
# greet()
# greet("vashi")
# def info(name,age):
#     print(f"name={name}, age={age}")
# data=info(age=34,name="vashi")
######for print multiple number,string at a time within function.
# def count(*numbers):
#     for number in numbers:
#         print(number)
# count(3,2,1,2,3,4,4,5,6,6,89)
# print(count,type(count))
####lambda function.(Syntax:-var_name=lambda argument:operation)Lambda function is a function who don't have function name and make sure that operation contain only and only one argument.You don't need to use lambda function everywhere just use this where you have to write only one line of code.and one more thing it is mainly used in map(),filter(),reduce()
###greet message.
# greet=lambda:print("hiii")
# greet()
###add two number.
# sum=lambda a,b : a+b,a-b##and make sure that operation contain only and only one argument if you give more than one it will give an error
# print(sum(5,6))
# sub=lambda c,d : c-d
# print(sub(9,2))
# mul=lambda m,n:m*n
# print(mul(3,4))
# cube=lambda a: a*a*a
# print(cube(5))
# avg=lambda a,b,c:(a+b+c)/3
# print(avg(3,4,5))
#####operators.
# a=10
# b=3
##Arithmetic operator
# print(f"{a} + {b} = {a+b}")
# print(f"{a} - {b} = {a-b}")
# print(f"{a} * {b} = {a*b}")
# print(f"{a} / {b} = {a/b}")#3
# print(f"{a} % {b} = {a%b}")#1
# print(f"{a} // {b} = {a//b}")#3 Floor division
###Relational operator.
# print(a>b)#true
# print(a>=b)#True
# print(a<b)#false
# print(a<=b)#false
# c=10;d=10
# print(c==d)#true
# e="hii";f="hiii"
# print(e==f)#false
# x="23";y=23
# print(x==y)##false
# print(x!=y)#true
# print(a==b and a>b)#false
# print("str"=="str" and a>b)#true
# print("vashi"=="vashi" and "vashi"=="vashi")##true
# print(a<b or a>b)#true
# print("vashi"=="vashi" or a<b)#true
# print(not 1)#false
# a=10
# b="10"
# print(a==b)#false
# print(type(a)==type(b))#false
###Membership operator.This operator is used in string,tuple,list,set and dictionary
##in, not in are a membership operator
# str="yeevashi"
# print("ee" in str)
# str1={
#     "name":"vashi",
#     "age":10
# }
# print("age" in str1)
# list=["name","age","anana",34,56]
# list.remove("name")
# print(list)
# list.pop()
# print(list)
# list.insert(2,"greets")
# list.append("wow")
# print(list)
# print("name" in list)##false
# if("name" in list):
#     print("name")
# elif("name" not in list):
#     list.insert(1,"name")
#     print(list)
# else:
#     print("leave it")
# list1=[23,1,2,345,67,45]
# print(sum(list1))
###identity operator(is,is not)This operator is used to identify the value and their memmory location
# a=5
# b=5
# print(a is b)##true
# x=10
# y="10"
# print(x is y)#false
# print(x is not y)##true
# p=2
# q=2.0
# print(p is q)##false
###type casting
##explicit type casting
# a=10
# print(float(a))
# print(bin(a))
# print(hex(a))
# b="A"
# print(ord(b))#65
# list=[]
# list.append(["hii","heelo","wow","nice"])
# print(list)
# list.extend(["vashi","riya","sheela"])
# print(list)
# def greet():

#     print("hello")

# greet()
###sir python
# print("hello world!!")
#8. a=123.123
# print("The result is {:.2f}".format(a))
# print("The result is {:.3f}".format(a))
# print("The resu;t is {:.0f}".format(a))
# a=123.123
# b=343.343
# print("The result is a={:.2f},b={:.2f}".format(a,b))
# c=234.456
# d=404.405
# print("c={:.2f} d={:.2f}".format(c,d))
##2. wap to programm to read two number and print the sum.
# num1=int(input("enter 1st number="))
# num2=int(input("enter 2nd number="))
# print("sum of {num1} and {num2} =", num1+num2)
##3.wap to print your name,roll and semester
# name=input("enter your name=")
# roll=int(input("enter your roll="))
# semester=input("enter your semester=")
# print(f"Your name={name} , roll={roll} and semester={semester}")
##4. wap to add 1-10.
# sum=0
# for num in range(1,11):
#     sum=sum+num
# print(f"The sum of 1-10 ={sum}")
##5. wap to read 3 numbers and print their sum in decimal format
# num1=int(input("enter 1st number="))
# num2=int(input("enter 2nd number="))
# num3=int(input("enter 3rd number="))
# print(f"The sum of {num1} , {num2}, {num3} ={float(num1+num2+num3)}")
##6. wap to read 3 value, 1st one should be date, 2nd one should be month and 3rd one should be year like date-month-year
# date=int(input("enter date="))
# month=int(input("enter month="))
# year=int(input("enter Year="))
# print("Date,month and Year =" ,date,month,year,sep="-")
##7. wap to print your name and age usinf f-string.
# name="vashi";age=23
# print(f"name={name} and age={age}")
##9. wap to print the largest number among three.
a=10;b=20;c=40
if(a>b and a>c):
    print("a is greatest")
elif(b>c and b>a):
    print("b is largest")
else:
    print("c is largest")
##10. wap to print character of name
# name="Yeevashi"
# for char in name:
#     print(char)
##11. wap to print your name by alphabetical wise except a.
# name="vashi"
# sorted_name=sorted(name)
# for char in sorted_name:
#     if char=="a":
#         continue
#     print(char)
####function.
##example of pass.
def data():
    pass
##wap to check whether the given number is even or odd.
# num=int(input("enter any number="))
# def check(num):
#     if(num%2==0):
#         print("even number")
#     else:
#         print("odd number")
# check(num)
###wap to print 1-10 except 5 using function.
# def num():
#     for a in range(1,11):
#         if(a==5):
#             continue
#         print(a)
# num()
##wap to find the square root of quadratic equation.
# import cmath 
# a=int(input("enter a="))
# b=int(input("enter b="))
# c=int(input("enter c="))
# D=(b**2)-(4*a*c)
# if(D>0):
#     Root1=(-b + cmath.sqrt(D))/(2*a)
#     Root2=(-b - cmath.sqrt(D))/(2*a)
#     print("Two real and distinct roots:")
#     print(f"root1={Root1} and root2={Root2}")
# elif(D==0):
#     Root= -b/(2*a)
#     print("One real and equal root:")
#     print("Root=",Root)

# else:
#     real_part=-b/(2*a)
#     imag_part=cmath.sqrt(-D)/(2*a)
#     print("Complex roots:")
#     print("Root1=",complex(real_part,imag_part))
#     print("Root2=",complex(real_part,-imag_part))
######Recurssion function 
# def greet():
#     print("hello")
#     greet()
# greet()
##print 10,9,8,7,6,5,4,3,2,1 by enter the number as 10 by user
# def natural(n):
#     print(n)
#     if(n==0):
#         return
#     natural(n-1)
# natural(10)

####factorial of number
# def factorial(n):
#     if(n==0 or n==1):
#         return(1)
#     elif(n<0):
#         return("Invalid number")
#     else:
#         fact=n * factorial(n-1)
#         return(fact)
#     # natural()
# print(factorial(5))
# def greet(name,ending):
#     print(f"hiii {name}")
#     print(ending)
# greet("vashi","thanku")

# def factorial(n):
#     if(n==0 or n==1):
#         return 1
#     return n* factorial(n-1)
# fact=factorial(5)
# print(f"The factorial of 5 = {fact}")
###fibonacci series
# def fibonacci(n):
#     if(n<0):
#         return 
#     return fibonacci(n-1)+ fibonacci(n-2)
# fib=fibonacci(5)
# print(f"The factorial of 5 = {fib}")
####practice set 
# programm to print greatest  umber among three
# def greatest(a,b,c):
#     if(a>b and a>c):
#         return(a)
#     elif(b>c and b>a):
#         return(b)
#     else:
#         return c
# add=greatest(3,4,5)
# print(add)
###programm to convert celcius into farenheit
# celcius=23
# farenheit=32+(9/5*celcius)
# print(farenheit)
# def celcius(f):
#    c=5*(f-32)/9
#    return c
# data=celcius(290)
# print(data)
###average of three numbers
# def average(a,b,c):
#    print((a+b+c)/3)
# average(5,23,4)
# average(5,23,40)
# average(5,23,1)
# def gooday(name,ending):
#    print("good day ,"+ name)
#    print(ending)
# gooday("vashi","Thanku")
# gooday("Yeevashi","Thanks")
# gooday("shrivashi","Thanks")
# def fact(n):
#    if(n==0 or n==1):
#       return 1
#    return n*fact(n-1)
   
# n=int(input("enter any number="))
# factorial=fact(n)
# print(f"The factorial of {n} = {factorial}")
####sum of 1st n natural number.
# def natural(n):
#    if(n==1):
#       return 1
#    return natural(n-1)+ n
# data=natural(5)
# print(data)
##print the table of given number
# def table(n):
#    if(n==0):
#       return
#    print ("*" * n)
#    table(n-1)
# data=table(7)
# print(data)
####method of print.
# greet="hii"
# name="vashi"
# print("greet -",greet,"name -",name)##separator
# print(f"greet= {greet} and name={name}")##fstring
# print("name and greet")##string
##Add two numbers
# a=25
# string=str(a)
# print(string)
# float=float(a)
# print(float)
# boolean=bool(a)
# print(boolean)##boolean convert the non-integer value into boolean except 0,"",[],{}
# a=int(input ("enter num1="))
# b=int(input ("enter num2="))
# c=int(input ("enter num3="))
# print(a+b+c)
###use split method is used to take multiple input in single line
# a,b,c=map(int,input("enter numbers").split())
# print(f"a={a},b={b},c={c}")
##lambda function
# sum=lambda a,b:print(a+b)
# sum(2,3)
# def data(*args):
#     print(args)
# data("hii","hello","greet")
# def data(*args):
#     print(args)
# data(["hii","hello","greet"])
# def fact(n):
#     if(n==0 or n==1):
#         return 1
#     return n*fact(n-1)
# data=fact(5)
# print(data)
#### built-in module(It is basically a file which contain python code(function,class,variables,etc).So that we can use this module on other program).We use module for reuasability prevent from duplication of code
###built-in module(math,os,calendar,random,statistics,datetime,time,json,functools,itertools,etc)
# import math############################math module
# # print(math.sqrt(25))
# # print(math.pow(2,3))
# # print(math.pi)
# print(math.sin(30))###here we give sin 30 we know that 30 is in degree but python expect that 30 is in radian so the output is given based radian value not degree.So prevent from this you have to mention radian for converting the radian into degree like this.
# print(math.sin(math.radians(30)))
# print(math.sin(math.radians(90)))
# print(math.tan(math.radians(45)))
# print(math.sin(math.radians(45)))
####random 
# import random
# print(random.randint(1,5))
#### datetime
# import datetime
# print(datetime.datetime.now())
# import time
# print(time.time())
###calendar
# import calendar
# print(calendar.month(2025,7))
# print(calendar.month(2025,8))
# import keyword
# print(keyword.kwlist)
# import math
# print(math.pow(3,4))
# print(math.sqrt(4))
# print(math.sin(math.radians(90)))
# print(math.cos(math.radians(45)))
# print(math.pi)
# from math import pow
# print(pow(2,3))
# from math import* 
# print(pow(2,3))
# print(sin(radians(90)))  
# print(factorial(5))
# print(f"log 10={log(10)}")     
# print(f"log 1={log(1)}")    
# print(f"lcm={lcm(2,4)}") 
# print(f"gcd={gcd(2,8)}") 
# print(f"permutation={perm(2,3)}") 
# print(f"combination={comb(2,9)}") 
# print(trunc(5.49))##truncate is used to remove the number after decimal
# print(floor(5.99))#5
# print(ceil(5.89))#6
# import random
# print(random.randint(2,5))
# import keyword
# print(keyword.kwlist)
###datetime module
# import calendar
# print(calendar.month(2026,8))
# import datetime
# print(datetime.datetime.now())
#####datatypes&collections
###########class
# class student:
#     course="BCACS"###class attribute
#     year=3###class attribute
#     college="JRSU"###class attribute
#     def data(self):
#         print(f"course={self.course},year={self.year},college={self.college}")
# vashi=student()
# vashi.course="BFS"#####object attribute
# vashi.data()####it's output will be like "course=BFS,year=3,college=JRSU"here our class attribute course=BCACS and object attribute is like course=BFS then object attribute will always overwrite the class attribute.
# class student:
#     course="BCACS"###class attribute
#     year=3###class attribute
#     college="JRSU"###class attribute
#     def data(self):
#         print(f"course={self.course},year={self.year},college={self.college}")
# vashi=student()
# vashi.course="BFS"#####object attribute
# vashi.data()
########create a class "pets" from a class"Animal and further creates a class "Dog" from "pets".Add a methd "bark"to class"Dog
# class Animal:
#     pass
# class pets(Animal):
#     pass
# class Dogs(pets):
#     def bark(self): 
#         print("Dog barks")

# german_shephard=Dogs()
# german_shephard.bark()
###constructor,self(it is used to access the instance variable or method of a class refer to the current object)
##constructor syntax:- __init__()
# class A:
#     def __init__(self,name,course):
#         roll=56
#         clg:"JRSU"
#         print(f"name={name}, roll={roll},course={course},clg={clg}")
# class B(A):
#     def __init__(self,roll,clg):
#         super().__init__(name,course)
#         print(f"name={name},course={course}, roll={roll},clg={clg}")

# object=B("vashi","bca",23,"JRU")
