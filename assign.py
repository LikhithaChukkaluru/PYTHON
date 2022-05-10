# l1=[{1:'a',2:'b'},{3:'c',4:'d'}]
# d1={}
# for i in l1:
#     d1.update(i)
# print (d1)

# l1=['red','blue','orange']
# d1=dict.fromkeys(l1,"colors")
# print (d1)

# l1 = [[1,2],[3,4],[5,[6,7]]]
# d1={}
# for i in l1:
#     d1.update({i[0]:i[1]})
# d1={x[0]:x[1] for x in l1}
# print(d1)

# l1=['a','b','c','d']
# d=dict(enumerate(l1))
# print (d)

# rec = {"Name" : "Python", "Age":"20","Addr" : "NJ", "Country" :"USA"}
# id1 = id(rec)
# del rec():
# rec = {"Name" : "Python", "Age":"20", "Addr" : "NJ", "Country" : "USA"}
# id2 = id(rec)
# print(id1 == id2)

# d={'Theodore': 19, 'Roxanne': 20, 'Mathew': 21, 'Betty': 20}
# l=[]
# for i in d.values():
#     l.append(i)
# print(l)

# for i in d.keys():
#     l.append(i)
# print(l)

# d={'Red': 1, 'Green': 3, 'White': 5, 'Black': 2, 'Pink': 4}
# d1=[]
# for i,j  in d.items():
#     d1.append((i,j))
# print(d1)

# s=list(d.items())
# print(s)

# a=['a', 'b', 'c', 'd', 'e', 'f']
# b=[1, 2, 3, 4, 5,6]
# d={}
# for i in range(0,len(a)):
#     d[a[i]]=b[i]
# print(d)

# d={'Theodore': 19, 'Roxanne': 20, 'Mathew': 21, 'Betty': 20}
# b=20
# l=[]
# for i,j in d.items():
#     if j==b:
#         l.append(i)
# print(l)

# d=[{'name': 'Theodore', 'age': 18}, {'name': 'Mathew', 'age': 22}, {'name': 'Roxanne', 'age': 20}, 
# {'name': 'David', 'age': 18}]
# l=[]
# for i in d:
#     s=i.get("age")
#     l.append(s)
# print(l)

# def max(list):
#     max=0
#     for  i in l:
#         if i>max:
#             max=i
#     return max
# l={1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100, 11: 121, 12:
# 144, 13: 169, 14: 196, 15: 225}
# print(max(l))


# d={1 : 25, 2 : 21, 3 : 23}
# l=[]
# for i in d.values():
#     l.append(i)
# print(l)

# d1 = {1: "Amit", 2 : "Suman"}
# d2 = {4 : "Ravi", 5 : "Kamal"}
# d3={}
# for i in d1,d2:
#     d3.update(i)
# print(d3)

# d1 = {1: "Amit", 2 : "Suman"}
# i=1
# for k in d1.values():
#     if i==k:
#         print("yes")
#         break
#     else:
#         print("no")

# d={}
# n=int(input("enter n:"))
# for i in range(n):
#     d.update({i:i*5})
# print(d)

# d1 = {1:2, 2: 90, 3: 50}
# sum=1
# for i in d1.values():
#     sum*=i
# print(sum)

# d1 = {1 : 2, 2 : 90, 3 : 50}
# k=2
# if k in d1:
#         d1.pop(k)
#         print(d1)
# else:
#         print("key not found")


# d={1 : "Aman", 2: "Suman", 3: "Aman"}
# d1={}
# for i,j in d.items():
#     if j not in d1.values():
#         d1.update({i:j})
# print(d1)

# d1={1:"Aman",2:"Suman",3:"Aman",4:"Kranti",5:"Suman"}
# c=0
# for i in d1:
#     c+=1
# print(c)

# p={1:("Amit",25000),2:("Suman",30000),3:("Ravi",36000)}
# d=list(p.values())
# for i in d:
#     if i[1]>25000:
#         print(i[0])

# d={}
# s=0
# for i in range(5):
#     rn = int(input("Enter roll number"))
#     nm = input("Enter name ")
#     mrk = input("Enter marks")
#     temp=(nm, mrk)
#     d[rn]=temp
# for i in d:
#     L=d[i]
#     s=s+int(L[1])
# print("Sum of marks ", s)

# t = {'red':12,'green':9,'black':123, 'white':678}
# s=sorted(t.items())
# print(dict(s))
# print(sorted(t.values()))
# for i in sorted(t):
#     print(t[i],i)


# d=[{'Math':90,'Science':92}, {'Math':89,'Science':94},{'Math':92,'Science':88}]
# l=[]
# for i in d:
#     for j,k in i.items():
#         if "Math" in j:
#            l.append(k)
# print(l)


# d={1:'Geek', 2: {3: {4: {}}}}
# count=0
# for i in d.values():
#         count+=1
# print(count)

# d= {'V': 10, 'VI': 10, 'VII': 40, 'VIII': 20, 'IX': 70, 'X': 80, 'XI': 40, 'XII': 20}
# dict={}
# for i in d.values():
#     if i in dict:
#         dict[i]+=1
#     else:
#         dict[i]=1
# print(dict)

# d=[{'student_id': 1, 'name': 'Jean Castro', 'class': 'V'}, 
# {'student_id': 2, 'name': 'Lula Powell', 'class': 'V'}, 
# {'student_id': 3, 'name': 'Brian Howell', 'class': 'VI'}, 
# {'student_id': 4, 'name': 'Lynne Foster', 'class': 'VI'}, 
# {'student_id': 5, 'name': 'Zachary Simon', 'class': 'VII'}]
# l=[]
# for i in d:
#     l1=[]
#     for j in i.values():
#         l1.append(j)
#     l.append(l1)
# print(l)
    
# d={'V':[10,12],'VI':[1    0],'VII':[10,20,30,40],'VIII':[20],'IX':[10,30,50,70],'X':[80]}


# sum=0
# d={'#FF0000': 'Red', '#800000': 'Maroon', '#FFFF00': 'Yellow', '#808000': 'Olive'}
# for i in d.values():
#     count=0
#     for j in i:
#         count+=1
#     sum+=count
# print(sum)

# t={}   
# d={8:['Ora Mckinney','Mathew Gilbert'],7:['Theodore Hollandl','Mae Fleming','Ivan Little']}
# for i,j in d.items():
#     t.update({j:i})
# print(t)

# d=[7, 23, 3.2, 3.3, 8.4] 
# d1={}
# for i in range(len(d)):
#     d1.update({int(d[i]):d[i]})
# print(d1)

# l=['Red', 'Green', 'Black', 'White', 'Pink']
# d={}
# for i in range(len(l)):
#     d.update({len(l[i]):[l[i]]})
# print(d)


# d={10: 'Theodore', 11: 'Mathew', 9: 'Roxanne'}
# d1={}
# for i,j in d.items():
#     d1.update({j:i})
# print(d1)

# d={'Theodore':{'user':'Theodore','age':45},'Roxanne':{'user':'Roxanne','age':15},'Mathew':{'user':'Mathew','age':21}}
# t={}
# for i,j in d.items():
#     for x,y in j.items():
#         if "age" in j.keys():
#             t.update({i:y})
# print(t)

# d={'Theodore': 19, 'Roxanne': 20, 'Mathew': 21, 'Betty': 20}
# d1=[]
# for i,j in d.items():
#     if j==20:
#         d1.append(i)
# print(d1)

# d={'Red': 1, 'Green': 3, 'White': 5, 'Black': 2, 'Pink': 4}
# l=[]
# for i,j in d.items():
#     l.append((i,j))
# print(l)


# d={1: 2, 3: 4, 4: 3, 2: 1, 0: 6}
# i=0
# max=0
# while i<len(d):
#     if max < d[i]:
#         max=d[i]
#         key=i
#     i+=1
# print(max)
# print(key)


# d={3:5,6:{"a":30,"b":5},7:2}
# sum=0
# for i,j in d.items():
#     if type (j)==dict:
#         for x,y in j.items():
#             sum+=y
#     else:
#         if type(i)==int:
#             sum+=i
#         if type(j)==int:
#             sum+=j
#     print(sum)


# d={10:"a",20:"b","c":{30:"e" , 40:"d"},5:"f"}
# sum=0
# for i,j in d.items():
#     if type(i)==int:
#         sum+=i
#     elif type(j)==dict:
#         for x,y in j.items():
#             sum+=x
# print(sum)


# l=[{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"},{"V":"S009"},{"VIII":"S007"}]
# l1=[]
# for i in l:
#     for x,y in i.items():
#         l1.append(y)
# print(set(l1))