
# city_population = {"NewYorkCity":8550405,"LosAngeles":3971883,"Toronto":2731571, "Chicago":2720546, 
# "Houston":2296224, "Montreal":1704694,  "Vancouver":631486, "Boston":667137}
# print(city_population["NewYorkCity"])
# print(city_population)
# print(type(city_population))

# Dict = {'ball' : 'green','Ball': 'red'}
# print(Dict['ball'])
# print(Dict['Ball'])

# student=dict(name= "Ravina",age= 20)
# print(student)

# my_dict = {1: 'apple', 2: 'ball'}
# print(my_dict)

# my_dict = {'name': 'John',1: [2, 4, 3]}
# print(my_dict[1])

# Dic= {1:'NAVGURUKUL', 2:'IN', 3:{'A':'WELCOME','B':'To', 'C' : 'DHARAMSALA'}}
# print(Dic)


# person={'name':'jack','age':20,'gender':'male',4:'organisation'}
# result = person['age'] 
# x = person.get("gender")
# print(person[4])
# print(x)
# print(result) 

# person={'name':'jack','age':20,'gender':'male',4:{'organisation':'navgurukul','place':'dharamsala'}}
# print(person['gender'])
# print(person[4])
# result = person[4]['place']
# print(result)

# dic= {'Name': 'RAM', 'Age': 17,}
# dic['ORGANIZATION'] = "NAV GURUKUL"
# dic['place'] = 'dharamsala'
# print(dic)

# dic= {'Name': 'RAM','Age': 17,}
# dic['student']={'id':22, 'place':'dharamsala'}
# print(dic)

# car ={"brand":  "ford","model":  "mustang","year":  1964}
# if "model" in car:
#     print("Yes, 'model' is one of the keys in the car dictionary.")
# else:
#     print("No, 'model' key dictionary mai nahi hai.")

# person= {'1': 'RAM', '2': 17,}
# person[3] = 'male'
# print(person)

# details={'Name': 'RAM','Age': 17, 'student': {'id': 22,'place': 'dharamsala'}} 
# details['student']['id']=35
# print(details)

# classes ={"room1":  "6th","room2":  "7th","room3":  "8th"}
# mydict=classes.copy()
# print(mydict)

# CAR_DETAILS={"brand": "Ford","model": "jason","year": 1964}
# CAR_DETAILS.pop("model")
# print(CAR_DETAILS)

# person={'name':'jack','id':22,'place':'dharamsala'}
# person.popitem()
# print(person) 

# person={'name':'jack','id':22,'place':'dharamsala'}
# del (person('place'))
# print(person)

# states_capitals = {'Gujarat' : 'Gandhinagar','Maharashtra' : 'Mumbai','Rajasthan' : 'Jaipur','Bihar' : 'Patna'}
# for state in states_capitals:
#   print(state)

# states_capitals = {'Gujarat' : 'Gandhinagar','Maharashtra' : 'Mumbai','Rajasthan' : 'Jaipur','Bihar' : 'Patna'}
# for state in states_capitals:
#     print(states_capitals[state])

# details ={"name":  "Bijender","age":  17,"class":  "10th"}
# for x in details.values():
#     print(x)

# movie ={"name":  "Puli","hero":  "Vijay","rating":  7.5}
# for x,y in movie.items():
#     print(x,y)

# meal ={"monday":  "Chole chawal","sunday":  "Fried rice","wednesday":  "dosa"}
# print(len(meal))

                            # Debug

# details={"name":"Shanti","age":12,"email":"shanti@navgurukul.org",}
# print(details["name"])
# # print(details["lastname"])
# print(details["age"])

# dict1={1:2,2:3,3:4,4:5}
# sum=0
# for i in dict1.values():
#     sum+=i
# print(sum)

# dict={}
# for i in range(1,16):
#     dict[i]=i*i
# print(dict)

# s={'umesh':21,'bijender':54,'amar':67,'peter':89,'sonu':56}
# a={'python':20,"gaurav":300,'dev':34,"karan":43}
# c={}
# for i in (s,a):
#     c.update(i)
# print(c) 

# questions  part 2


# a = {(1,2):1,(2,3):2}
# print(a[1,2])

# a = {'a':1,'b':2,'c':3}
# print(a['a','b'])

# fruit = {}
# def addone(index):
#     if index in fruit:
#         fruit[index] += 1
#     else:
#         fruit[index] = 1
# addone('Apple')
# addone('Banana')
# addone('apple')
# addone('Apple')
# print(len(fruit))
# print(fruit)

# Student = {}
# Age = {}
# Details = {}
# Student['name'] = "bikki"
# Age['student_age'] = 14
# Details['Student'] = Student
# Details['Age'] = Age
# print(len(Details["Student"]))

# my_dict = {}
# my_dict[(1,2,4)] = 8
# my_dict[(4,2,1)] = 10
# my_dict[(1,2)] = 12
# sum = 0
# for k in my_dict:
#     sum += my_dict[k]
# print(sum)
# print(my_dict)

# box = {}
# jars = {}
# crates = {}
# box['biscuit'] = 1
# box['cake'] = 3
# jars['jam'] = 4
# crates['box'] = box
# crates['jars'] = jars
# print(len(crates))

# rec = {"Name" : "Python", "Age":"20","Addr" : "NJ", "Country" :"USA"}
# id1 = id(rec)
# del rec
# rec = {"Name" : "Python", "Age":"20", "Addr" : "NJ", "Country" : "USA"}
# id2 = id(rec)
# print(id1 == id2)

# Question part 1:

# 1.
# dic1={1:10, 2:20}
# dic2={3:30,2:40}
# dic3={5:50,6:60}
# d3={}
# for i in dic1:
#     for j in dic2:
#         for k in dic3:
#             if i not in d3:
#                 d3[i]=dic1[i]
#             elif i in dic2  :
#                d3[i]=dic1[i]+dic2[j]
#             elif j not in d3:
#                 d3[j]=dic2[j]
#             else:
#                 d3[k]=dic3[k]
# print(d3)


# Q.2  
# dict1={"name":"Raju", "marks":56}
# n=input("enter n:")
# for i in dict1:
#     if n in dict1:
#         print("exists in dict1")
#     else:
#         print("not exists in dict1")


# Q.3
# my_dict = {'data1':100,'data2': -54,'data3': 247}
# sum=0 
# for i in my_dict.values():
#     sum+=i
# print(sum)


# 4.
# Dic= {1: 'NAVGURUKUL',2: 'IN',  3:{'A' : 'WELCOME','B' : 'To','C' : 'DHARAMSALA'}}
# del Dic[3]["A"]
# print(Dic)



# 5.
# list1=["one","two","three","four","five"]
# list2=[1,2,3,4,5,]
# d={}
# for i in range(0,len(list1)):
#     d[list1[i]]=list2[i]
# print(d)m

# d={}
# for key in list1:
#     for value in list2:
#         d[key]=value
#         list2.remove(value)
#         break
# print(d)


# 6.
# dic={"ball":"red","bat":4,"wickets":8,"ball":"green","bat":3}
# temp = []
# res = dict()
# for key, val in dic.items():
#     if val not in temp:
#         temp.append(val)
#         res[key] = val
# print("The dictionary after values removal : " , str(res)  )

# res = dict()
# for key, value in dic.items():
#     if value not in res.values():
#         res[key] = value
# print(res)


# 7.
# d=[{"first":"1"}, {"second": "2"}, {"third": "1"}, {"four": "5"}, {"five":"5"}, 
# {"six":"9"},{"seven":"7"}]
# l=[]
# b=[]
# for i in d:
#         for j in i.values():
#                 l.append(j)
#                 for k in l:
#                         if k not in b:
#                                 b.append(k)
# print(b)

        
# 8.
# dic={'sonu':85,'Kartik':90,'Deepak':96,'Aman':76,'Somesh':60,'Umesh':85,'Amarpal':70,'Roshan':57,
# 'Riyaz':98,'Shabid':56}
# sum=0
# for i in dic:
#     sum+=dic[i]
# print(sum)


# 9.
# t="MISSISSIPPI" 
# d={}
# for i in t:
#     if i in d:
#         d[i]+=1
#     else:
#         d[i]=1
# print(d)

# for i in t:
#     d[i]=t.count(i)
# print(d)


# 10.
# dict1 =  {'Alex': ['subj1', 'subj2', 'subj3'], 'David': ['subj1', 'subj2']}
# count=0
# for item in dict1.values():
#     for i in item:
#         count+=1
# print(count)


# # 11.
# t = {'a':50, 'b':58, 'c':56,'d':40, 'e':100, 'f':20}
# n=3
# for i in t:
#         s=sorted(t.values())
# print(s[-3:])
        

# 12.
# dict={}
# for i in range (1,16):
#     for j in range(i+1):
#         dict[i]=j**2
# print(dict)


13.
t = {'a':50, 'b':58,'c': 56,'d':40,'e':100, 'f':20}
m=0
l=[]
for i in t:
        if t[i]>m :
                m=t[i]
                key=i
l.append(key)
m1=0
for i in t:
        if t[i]>m1:
                if t[i] !=m:
                        m1=t[i]
                        key=i
l.append(key)
m2=0
for i in t:
        if t[i]>m2:
                if t[i] !=m and t[i] !=m1:
                        m2=t[i]
                        key=i
l.append(key)
print(l)

# 14.
# d={'bijender':45,'deepak':60,'param':20,'anjili':30,'roshini':50}


#                                 MAXIMUM

# dict = {'a':50, 'b':58, 'c':56,'d':40,'e':100, 'f':20}
# m=0
# for i in dict.values():
#     if i >m:
#         m=i
#         res=m
# print(res)

# dict = {'a':50, 'b':58, 'c':56,'d':40,'e':100, 'f':20}
# m=0
# dic=list(dict.values())
# min=dic[0]
# for i in  range (len(dic)):
#         if min>dic[i]:
#                 min=dic[i]
# print(min)

# dict= {'Micheal' : {'i' : 15, 'z' : 14},'George' : {'q' : 2, 'y' : 10, 'w' : 3},'John' : {'n' : 19}}
# b={}
# for k,v in dict.items():
#     count=0
#     for i in v.values():
#         if i>count:
#             count=i
#             res=count
# print(res)

                               



                                #        sort

# a1 = {'a':1, 'b':13, 'd':4, 'c':2, 'e':30}
# s=sorted(a1.keys())
# s=sorted(a1.keys(),reverse=True)
# s=sorted(a1.values())
# s=sorted(a1.values(),reverse=True)
# print(s)
                       
                        # depend on value

# a1 = {'a':1, 'b':13, 'd':4, 'c':2, 'e':30}
# d={}
# sk=sorted(a1,key=a1.get,reverse=True)
# for i in sk:
#     d[i]=a1[i]
# print(d)

# a1 = {'a':1, 'b':13, 'd':4, 'c':2, 'e':30}
# d={}
# s=sorted(a1,key=a1.get)
# for i in s:
#         d[i]=a1[i]
# print(d)


#                               depend on values

# d={1: 41, 2: 93, 32: 4}
# s=sorted(d.keys())
# print(s)
# sd={}
# for i in s:
#         for j in d.values():
#                 if d[i]==j:
#                         sd[j]=d[j]
#                         break
# print(sd)


# d={23:1,2:9,39:4}
# s=sorted(d.values(),reverse=True)
# sd={}
# for i in s:
#         for j in d.keys():
#                 if d[j]==i:
#                         sd[j]=d[j]
#                         break
# print(sd)

