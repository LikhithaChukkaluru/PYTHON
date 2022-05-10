import json
import requests
import os 

path_exists=os.path.exists("krishna.json")
if path_exists==False:
    url=requests.get('https://api.merakilearn.org/courses')
    r=json.loads(url.text)
    with open("krishna.json","w") as f:
        json.dump(r,f,indent=4)

    serial=0
    for i in range(len(r)):
        for k,v in r[i].items():    
            if k=="name":
                serial+=1
                print(serial,v,"-",r[i]["id"])
    course=int(input("select which course you want display  :"))
    print(course,r[course-1]["name"])

    course_id=r[course-1]["id"]
    url1=requests.get('https://api.merakilearn.org/courses/'+str(course_id)+"/exercises")
    r1=json.loads(url1.text)
    with open("krish.json","w") as f2:
        json.dump(r1,f2,indent=6)
    print(r[course-1]['name'],"-",r[course-1]["id"])

    serial=1
    serial1=1
    list=[]
    list1=[]

    for i in r1["course"]["exercises"]:
        if i["parent_exercise_id"]==None:
            print(serial,i["name"])
            print(" ",serial1,i["slug"])
            serial+=1
            list.append(i)
            list1.append(i)
        elif i["parent_exercise_id"]==i["id"]:
            print(serial,i["name"])
            serial+=1
            list.append(i)
            new=1  
        elif i["parent_exercise_id"]!=i["id"]:
            print(" ",new,i["name"])
            new+=1
            list1.append(i)

    file=open("kri.json","w")
    json.dump(list,file,indent=3)
    file=open("kri1.json","w")
    json.dump(list1,file,indent=3)
    parent_id=int(input(" which parent id you want to enter : "))

    serial=1
    idd=list[parent_id-1]["id"]
    for i in list:
        if i["parent_exercise_id"]==i["id"]:
            print(serial,list[parent_id-1]["name"])
            serial+=1
            break

        else:
            if i["parent_exercise_id"]!=i['id']:
                print(serial,list[parent_id-1]["name"])
                print(" ",list[parent_id-1]["content"])
                serial+=1
                break

    l=[]
    l1=[]
    new_no=1
    idd=list[parent_id-1]["id"]
    for j in list1:
        if j["parent_exercise_id"]==idd:
            print(" ",new_no,j["name"])
            l.append(j["name"])
            l1.append(j["content"])
            new_no+=1

    child_id=int(input("which child id you do you want enter  :"))
    for i in range (len(l)):    
        if child_id-1==i:
            print(l[i])
            print(l1[i])
            break

elif path_exists==True:
    url=open("krishna.json","r")
    r=json.load(url)

    serial=0
    for i in range(len(r)):
        for k,v in r[i].items():    
            if k=="name":
                serial+=1
                print(serial,v,"-",r[i]["id"])
    course=int(input("select which course you want display  :"))
    print(course,r[course-1]["name"])


    course_id=r[course-1]["id"]
    file=os.path.exists("krish.json")

    if file==False:
        url1=requests.get('https://api.merakilearn.org/courses/'+str(course_id)+"/exercises")
        r1=json.loads(url1.text)
        with open("krish.json","w") as f2:
            json.dump(r1,f2,indent=6)
        print(r[course-1]['name'],"-",r[course-1]["id"])

        serial=1
        serial1=1
        list=[]
        list1=[]

        for i in r1["course"]["exercises"]:
            if i["parent_exercise_id"]==None:
                print(serial,i["name"])
                print(" ",serial1,i["slug"])
                serial+=1
                list.append(i)
                list1.append(i)
            elif i["parent_exercise_id"]==i["id"]:
                print(serial,i["name"])
                serial+=1
                list.append(i)
                new=1  
            elif i["parent_exercise_id"]!=i["id"]:
                print(" ",new,i["name"])
                new+=1
                list1.append(i)

        file=open("kri.json","w")
        json.dump(list,file,indent=3)
        file=open("kri1.json","w")
        json.dump(list1,file,indent=3)
        parent_id=int(input(" which parent id you want to enter : "))

        serial=1
        idd=list[parent_id-1]["id"]
        for i in list:
            if i["parent_exercise_id"]==i["id"]:
                print(serial,list[parent_id-1]["name"])
                serial+=1
                break

            else:
                if i["parent_exercise_id"]!=i['id']:
                    print(serial,list[parent_id-1]["name"])
                    print(" ",list[parent_id-1]["content"])
                    serial+=1
                    break

        l=[]
        l1=[]
        new_no=1
        idd=list[parent_id-1]["id"]
        for j in list1:
            if j["parent_exercise_id"]==idd:
                print(" ",new_no,j["name"])
                l.append(j["name"])
                l1.append(j["content"])
                new_no+=1

        child_id=int(input("which child id you do you want enter  :"))
        for i in range (len(l)):    
            if child_id-1==i:
                print(l[i])
                print(l1[i])
                break
    
    elif file==True:
        url1=open("krish.json","r")
        r1=json.load(url1)
        print(r[course-1]["name"],"-",r[course-1]["id"])

        serial=1
        serial1=1
        list=[]
        list1=[]

        for i in r1["course"]["exercises"]:
            if i["parent_exercise_id"]==None:
                print(serial,i["name"])
                print(" ",serial1,i["slug"])
                serial+=1
                list.append(i)
                list1.append(i)
            elif i["parent_exercise_id"]==i["id"]:
                print(serial,i["name"])
                serial+=1
                list.append(i)
                new=1  
            elif i["parent_exercise_id"]!=i["id"]:
                print(" ",new,i["name"])
                new+=1
                list1.append(i)

        file=os.path.exists("kri.json")
        file1=os.path.exists("kri1.json")

        if file==True and file1==True:
            a=open("kri.json","r")
            b=json.load(a)
            a1=open("kri1.json","r")
            b1=json.load(a1)

            parent_id=int(input("which parent id you do you want please enter :"))

            serial=1
            idd=list[parent_id-1]["id"]
            for i in list:
                if i["parent_exercise_id"]==i["id"]:
                    print(serial,list[parent_id-1]["name"])
                    serial+=1
                    break

                else:
                    if i["parent_exercise_id"]!=i['id']:
                        print(serial,list[parent_id-1]["name"])
                        print(" ",list[parent_id-1]["content"])
                        serial+=1
                        break

            l=[]
            l1=[]
            new_no=1
            idd=list[parent_id-1]["id"]
            for j in list1:
                if j["parent_exercise_id"]==idd:
                    print(" ",new_no,j["name"])
                    l.append(j["name"])
                    l1.append(j["content"])
                    new_no+=1

            child_id=int(input("which child id you do you want enter  :"))
            for i in range (len(l)):    
                if child_id-1==i:
                    print(l[i])
                    print(l1[i])
                    break
        else:
            print("actually  the file is not exists ")

        