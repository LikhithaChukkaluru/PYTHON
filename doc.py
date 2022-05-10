#  1.
# d1 = {'a': 100, 'b': 200, 'c': 300}
# d2 = {'a': 300, 'b': 200, 'd': 400}
# d3= {'a' : 278, 'c': 78 , 'd': 89 }
# for i in d2:
#     if i in d1 :
#         d1[ i ] = d1[ i ] +d2[ i ]
#     else :
#         d1[ i ] = d2[ i ]
# print(d1)


# 2.
# st='w3resource'
# d={}
# for i in st:
#     d[i]=st.count(i)
# print(d)

# t='w3resource'
# d={}
# for i in t:
#     if i in d:
#         d[i]+=1
#     else:
#         d[i]=1
# print(d)


#  3.
# n=int(input("enter the n:"))
# d={}
# for i in range(1,n):
#     d[i]=i*i
# print(d)


# 5.
# d1={1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
# d={}
# s=sorted(d1,key=d1.get)
# for i in s:
#     d[i]=d1[i]
# print(d)

# d={}
# s=sorted(d1.values())
# for i in s:
#     d[i]=d1[i]
# print(d)


# 6.
# d={0: 10, 1: 20}
# d.update({2:30})
# # d[2]=30
# print(d)


# 7.
# dic1={1:10, 2:20}
# dic2={3:30, 4:40}
# dic3={5:50}
# d={}
# for i in dic1,dic2,dic3:
#     d.update(i)
# print(d)


# 9.
# def check(dict,key):
#     if key in dict.keys():
#         print("exists in dictionary")
#     else:
#         print("not exists in dictionary")
# dict={1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
# key=1
# check(dict,key)

# d={'A':1,'B':2,'C':3}
# k=input("Enter key to check:")
# if k in d.keys():
#       print("K is present and value of the key is:",d[k])
# else:
#       print("Key isn't present!")


# 10.
# d={1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
# for i,j in d.items():
#     print(i,j)


# 11.
# l={1:2,2:4,3:6,4:8,5:25}
# l1={3:3,3:6,3:9}
# l3={}
# for i in l,l1:
#     l3.update(i)
# print(l3)


# 13.
# l={1:2,2:4,3:6,4:8,5:25}
# sum=0
# for i in l:
#     sum+=l[i]
# print(sum)


# 14.
# l={1:2,2:4,3:6,4:8,5:25}
# pro=1
# for i in l:
#     pro*=i
#     # pro*=l[i]
# print(pro)


# 15.
# l={1:2,2:4,3:6,4:8,5:25}
# l.pop(4)
# print(l)
# l.popitem()
# print(l)


# 16.
# list1=["one","two","three","four","five"]
# list2=[1,2,3,4,5,]
# d={}
# for i in range(0,len(list1)):
#     d[list1[i]]=list2[i]
# print(d)


# 17.
# d=l={1:2,2:4,7:98,3:6,4:8,5:25}
# s=sorted(d.keys())
# print(s)


# 18.
# l={1:2,2:4,7:98,3:6,4:8,5:25}
# m=0
# for i in l.values():
#     if i>m :
#         m=i
#         res=i
# print(res)

# l={1:2,2:4,7:98,3:6,4:8,5:25}
# b=list(l.values())
# m=b[0]
# for i in m:
#     if i<m:
#         m=i
# print(m)

# 19.
# student_data = {'id1':{'name': ['Sara'],'class': ['V'],'subject_integration': ['english', 'math', 'science']},
# 'id2':{'name': ['David'],'class': ['V'],'subject_integration': ['english', 'math', 'science']},
# 'id3':{'name': ['Sara'],'class': ['V'],'subject_integration': ['english', 'math', 'science']},
# 'id4':{'name': ['Surya'],'class': ['V'],'subject_integration': ['english', 'math', 'science']},}
# d={}
# for i,j in student_data.items():
#     if j not in d.values():
#         d[i]=j
# print(d)


# 20.
# d={}
# if d=={}:
#     print("empty dictionary")
# else:
#     print("not a empty dictionary")

# if  not bool(d):
#     print("empty dictionary")
# else:
#     print("not a empty dictionary")


# 21.
# d=[{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"},{"V":"S009"},{"VIII":"S007"}]
# t=[]
# s=[]
# for i in d:
#     for j in i.values():
#         t.append(j)
#         for k in t:
#             if k  not in s:
#                 s.append(k)
# print(s)  


# 22.
# l={'1':['a','b'], '2':['c','d']}
# d=list(l.values())
# for i in d[0]:
#     for j in d[1]:
#         print(i+j)


# 23.
# from collections import Counter
# my_dict = {'t': 3, 'u': 4, 't': 6, 'o': 5, 'r': 21}
# k = Counter(my_dict)
# high = k.most_common(4)
# print("Dictionary with 3 highest values:")
# print("Keys: Values")
# for i in high:
#    print(i[0]," :",i[1]," ")

# d={1:2,2:4,7:98,3:6,4:8,5:25}
# m=0
# for i in d:
#     if d[i]>m:
#         m=d[i]
# print(m)
# m1=0
# for i in d:
#     if d[i]>m1:
#         if d[i]!=m:
#             m1=d[i]
# print(m1)
# m2=0
# for i in d:
#     if d[i]>m2:
#         if d[i]!=m and d[i]!=m1:
#             m2=d[i]
# print(m2)


#  24.
# d=[{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, {'item': 'item1','amount': 750}]
# s={}
# for i in d:
#     if i ["item"] not in s:
#         s[i["item"]]=i["amount"]
#     else:
#         s[i['item']] += i['amount'] 
# print(s)


# 26.
# d={'C1':[1,2,3],'C2':[5,6,7],'C3':[9,10,11]}
# for i in d:
#     print(i,end=" ")
# a=[]
# for i in d:
#     b=d[i]
#     a.append(b)
# print()
# i=0
# while i<len(a):
#     j=0
#     while j<len(a[i]):
#         sum=a[j][i]
#         print(sum,end=" ")
#         j+=1
#     print()
#     i+=1


# 27.
# d=[{'id': 1, 'success': True, 'name': 'Lary'},{'id': 2, 'success': False, 'name': 'Rabi'},
# {'id': 3, 'success': True, 'name': 'Alex'}]
# sum=0
# for i in d:
#     for j in i:
#         if j=="id" :
#             sum+=i[j]
# print(sum)


# 28.
# d=[1, 2, 3, 4,7]
# l={}
# s=l
# for i in d:
#     l[i]={}
#     l=l[i]
# print(s)


# 29.
# n= {'n1': [2, 3, 1], 'n2': [5, 1, 2], 'n3': [3, 2, 4]}
# s={i:sorted(j) for i,j in n.items()}
# print(s)
#                                 # or

# for i,j in n.items():
#     s={i:sorted(j)}
#     print(s)

# 30.
# d={'S 001': ['Math', 'Science'], 'S 002': ['Math','English']}
# d1={}
# for i in d:
#     c=""
#     for j in range (len(i)):
#         print(i[j])
#         if i[j] != " ":
#             c+=i[j]
#     d1[c]=d[i]
# print(d1)

# for i in d:
#     c=" "
#     j=0
#     while j<len(i):
#         if i[j] != " ":
#             c+=i[j]
#         j+=1
#     d1[c]=d[i]
# print(d1)


# 31.
# l={'item1': 45.50, 'item2':35, 'item3': 41.30, 'item4':55,'item5': 24}
# m=0
# for  i in l:
#    if l[i]>m:
#        m=l[i]
#        key=i
# print(key,m)
# m1=0
# for i in l:
#     if l[i]>m1:
#         if l[i]!=m:
#             m1=l[i]
#             key=i
# print(key,m1)
# m2=0
# for i in l:
#     if l[i]>m2:
#         if l[i] !=m and l[i] !=m1:
#             m2=l[i]
#             key=i
# print(key,m2)


#  32.
# l={1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
# count=0
# for i,j in l.items():
#     if j in l.values():
#         count+=1
# # print("key","value","count")
#         print(i,j,count)


# 33.
# s = {'Aex':{'class':'V','rolld_id':2},'Puja':{'class':'V','roll_id':3}}
# for i in s:
#     print(i)
#     for j in s[i]:
#        print(j,":",s[i][j])


# 35.
# d={'Alex': ['subj1', 'subj2', 'subj3'], 'David': ['subj1', 'subj2']}
# count=0
# for i in d.values():
#     for j in i:
#         count+=1
# print(count)


# 36.
# d={'key1': 1, 'key2': 3, 'key3': 2}
# d1= {'key1': 1, 'key2': 2}
# for i in d:
#     for j in d1:
#         if i==j and d[i]==d1[j]:
#             print(i,":",d[i])


# 37.
# d={'x': [11, 12, 13, 14, 15, 16, 17, 18, 19],'y': [21, 22, 23, 24, 25, 26, 27, 28, 29],'z': [31, 32, 33, 34, 35, 36, 37, 38, 39]}
# for i in d:
#     print(d[i][4])


# 38.
# d={'c1': 'Red', 'c2': 'Green', 'c3': None}
# d1={}
# for i,j in d.items():
#     if j is not  None:
#         d1.update({i:j})
# print(d1)


# 39.
# d={'Cierra Vega': 175, 'Alden Cantrell': 180, 'Kierra Gentry': 165, 'Pierre Cox': 190}
# d1={}
# for i,j in d.items():
#     if j>170: 
#         d1[i]=j
# print(d1)


#  40.
# d=['S001', 'S002', 'S003', 'S004']
# d1=['Adina Park', 'Leyton Marsh', 'Duncan Boyle', 'Saim Richards']
# d2=[85, 98, 89, 92]
# l=[]
# for i in range (len(d)):  
#     t={} 
#     t.update({d[i]:{d1[i]:d2[i]}})
    # print(t)
#     l.append(t)
# print(l)

# 41.
# d={'Cierra Vega': (6.2, 70), 'Alden Cantrell': (5.9, 65), 'Kierra Gentry': (6.0, 68), 'Pierre Cox': (5.8,66)}
# d1={}
# for i,j in d.items():
#     if j > (6,70):
#         d1[i]=j
# print(d1)


# 42.
# d={'Cierra Vega': 12, 'Alden Cantrell': 12, 'Kierra Gentry': 10, 'Pierre Cox': 12}
# n=12
# # for i in d.values():
# for i in d:
#     if d[i]==n:
#         print("true")
#     else :
#         print("false")

# def check (d,n):
#     for i in d.values():
#         if i==n:
#             return (True)
#         else:
#             return(False)
# d={'Cierra Vega': 12, 'Alden Cantrell': 12, 'Kierra Gentry': 12, 'Pierre Cox': 12}
# n=12
# print(check(d,n))


# 43.
# l=[('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
# d={}
# for i in l:
#     if i[0] not in d.keys():
#         d.update({i[0]:[i[1]]})
#     elif i[0] in d.keys():
#         d[i[0]].append(i[1])
# print(d)

# 44.
# [{'Science': 88, 'Language': 77}, {'Science': 89, 'Language': 78}, {'Science': 62, 'Language':
# 84}, {'Science': 95, 'Language': 80}]


# d={'Science': [88, 89, 62, 95], 'Language': [77, 78, 84, 80]}
# d1=[]
# for i,j in d.items():
#     t={}
#     for k in j:
#         t.update({i:k})
#         print(t)
#         d1.append(t)
# print(d1)


# 45.
# d=[{'id': '#FF0000', 'color': 'Red'}, {'id': '#800000', 'color': 'Maroon'}, {'id': '#FFFF00', 'color':
# 'Yellow'}, {'id': '#808000', 'color': 'Olive'}]
# l=[]
# nid= "#FF0000"
# for i in d:
#     if i.get("id")!=nid:
#         l.append(i)
# print(l)


# # 46.
# d=[{'x': '10', 'y': '20', 'z': '30'}, {'p': '40', 'q': '50', 'r': '60'}]
# for i in d:
#     for j in i:
#         i[j]=int(i[j])
# print(d)

# d=[{'x': 10.12, 'y': 20.23, 'z': 30}, {'p': 40.00, 'q': 50.19, 'r': 60.99}]
# for i in d:
#     for j in i:
#         i[j]=str(i[j])
# print(d)


# 47.
# d={'C1': [10, 20, 30], 'C2': [20, 30, 40], 'C3': [12, 34]}
# for i in d:
#     d[i].clear()
# print(d)

# a={'C1': [10, 20, 30], 'C2': [20, 30, 40], 'C3': [12, 34]}
# for i in a.keys():
#         a[i]=[]
# print(a)

# a={'C1': [10, 20, 30], 'C2': [20, 30, 40], 'C3': [12, 34]}
# t={}
# for i,j in a.items():
#     if len(j)>0:
#         t.update({i:[]})
# print(t)


#  48.
# d={1: 'red', 2: 'green', 3: 'black', 4: 'white', 5: 'black'}
# b={}
# for i in d.values():
#     b[i]=len(i)
# print(b)

# b={'1': 'Austin Little', '2': 'Natasha Howard', '3': 'Alfred Mullins', '4': 'Jamie Rowe'}
# d={}
# for i in b.values():
#     d[i]=len(i)
# print(d)


# 49.
# num = {'physics': 80, 'math': 90, 'chemistry': 86}
# for i in num.keys():
#     print(i)


# 50.
# d={1: 'red', 2: 'green', 3: 'black', 4: 'white', 5: 'black'}
# l=[]
# for i,j in d.items():
#     l.append([i,j])
# print(l)

# d={'1': 'Austin Little', '2': 'Natasha Howard', '3': 'Alfred Mullins', '4': 'Jamie Rowe'}
# l=[]
# for i,j in d.items():
#     l.append([i,j])
# print(l)

# 51.
# d={'V': [1, 4, 6, 10], 'VI': [1, 4, 12], 'VII': [1, 3, 8]}
# d1={}
# for i,j in d.items():
#     l=[]
#     for k in j:
#         if k%2==0:
#             l.append(k)
#         d1[i]=l
# print(d1)

# d={'V': [1, 3, 5], 'VI': [1, 5], 'VII': [2, 7, 9]}
# d1={}
# for i,j in d.items():
#     l=[]
#     for k in j:
#         if k%2==0:
#             l.append(k)
#         d1[i]=l
# print(d1)

#  52.
# d={'a': 5, 'b': 14, 'c': 32, 'd': 35, 'e': 24, 'f': 100, 'g': 57, 'h': 8, 'i': 100}
# m=0
# l=[]
# for i in d:
#     if d[i]>m:
#         m=d[i]
#         key=i
# l.append(key)
# m1=0
# for i in d:
#     if d[i] > m1:
#         if d[i] !=m:
#             m1=d[i]
#             key=i
# l.append(key)
# m2=0
# for i in d:
#     if d[i] >m2:
#         if d[i] !=m and d[i] !=m1:
#             m2=d[i]
#             key=i
# l.append(key)
# print(l)


# # 53.
# l=[[1, 'Jean Castro', 'V'], [2, 'Lula Powell', 'V'], [3, 'Brian Howell', 'VI'], [4, 'Lynne Foster', 'VI'], [5,
# 'Zachary Simon', 'VII']]
# d={}
# for i in l:
#     d.update({i[0]:i[1:]})
# print(d)

#  # 54.
# d={1:['Jean Castro'],2:['Lula Powell'],3:['Brian Howell'],4:['Lynne Foster'],5:['Zachary Simon']}
# l=[]
# d1={}
# for i,j in d.items():
#     d1.update({i:j[0]})
# l.append(d1)
# print(l)  
