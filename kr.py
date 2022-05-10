import requests
import os
import json

file=os.path.exists("course.json")
if file==False:
    a=requests.get("https://api.merakilearn.org/courses")
    get_url=a.json()
    my_file=open("course.json","w")
    b=json.dump(get_url,my_file,indent=6)

    serial=0
    for i in range(len(get_url)):
        for k,v in get_url[i].items():
            if k=="name":
                serial+=1
                print(serial,v,"-",get_url[i]["id"])
    choose=int(input("which course do you want please enetr :"))

    id=get_url[choose-1]["id"]
    url="https://api.merakilearn.org/courses/"+str(id)+"/exercises"

    get_data=requests.get(url)
    data=get_data.json()
    file=open("course_exercises.json","w")
    json.dump(data,file,indent=4)
    print(get_url[choose-1]["name"],"-",get_url[choose-1]["id"])

    serial=1
    serial1=1
    list1=[]
    list2=[]

    for i in data["course"]["exercises"]:
        if i["parent_exercise_id"]==None:
            print(serial,i["name"])
            print("  ",serial1,i["slug"])
            serial+=1
            list1.append(i)
            list2.append(i)
        elif i["parent_exercise_id"]==i["id"]:
            print(serial,i["name"])
            serial+=1
            list1.append(i)
            new_no=1
        elif i["parent_exercise_id"]!=i["id"]:
            print("  ",new_no,i["name"])
            new_no+=1
            list2.append(i)
    
    file=open("list1.json","w")
    json.dump(list1,file,indent=4)
    file1=open("list2.json","w")
    json.dump(list2,file1,indent=4)

    parent_id=int(input("which parent id you want to please enter :"))

    serial=1
    idd=list1[parent_id-1]["id"]
    for i in list1:
        if i["parent_exercise_id"]==i["id"]:
            print(serial,list1[parent_id-1]["name"])
            serial+=1
            break
        else:
            if i["parent_exercise_id"]!=idd:
                print(serial,list1[parent_id-1]["name"])
                print("  ",list1[parent_id-1]["content"])
                serial+=1
                break
    l=[]
    l1=[]
    new_no=1
    idd=list1[parent_id-1]["id"]

    for j in list2:
        if j["parent_exercise_id"]==idd:
            print("  ",new_no,j["name"])
            l.append(j["name"])
            l1.append(j["content"])
            new_no+=1
    
    child_id=int(input("which child id you want plese enetr :"))

    for i in range(len(l)):
        if child_id==i:
            print(l[i])
            print(l1[i])
            break

elif file==True:
    my_file=open("course.json","r")
    get_url=json.load(my_file)

    serial=0
    for i in range(len(get_url)):
        for k,v in get_url[i].items():
            if k=="name":
                serial+=1
                print(serial,v,"-",get_url[i]["id"])
    choose=int(input("which course do you want please enetr :"))

    idd=get_url[choose-1]["id"]
    file=os.path.exists("course_exercises.json")

    if file==False:

        url="https://api.merakilearn.org/courses/"+str(idd)+"/exercises"

        get_data=requests.get(url)
        data=get_data.json()
        file=open("courses_exercise.json","w")
        json.dump(data,file,indent=4)
        print(get_url[choose-1]["name"],"-",get_url[choose-1]["id"])

        serial=1
        serial1=1
        list1=[]
        list2=[]

        for i in data["course"]["exercises"]:
            if i["parent_exercise_id"]==None:
                print(serial,i["name"])
                print("  ",serial1,i["slug"])
                serial+=1
                list1.append(i)
                list2.append(i)
            elif i["parent_exercise_id"]==i["id"]:
                print(serial,i["name"])
                serial+=1
                list1.append(i)
                new_no=1
            elif i["parent_exercise_id"]!=i["id"]:
                print("  ",new_no,i["name"])
                new_no+=1
                list2.append(i)
        
        file=open("list1.json","w")
        json.dump(list1,file,indent=4)
        file1=open("list2.json","w")
        json.dump(list2,file1,indent=4)

        parent_id=int(input("which parent id you want to please enter :"))

        serial=1
        idd=list1[parent_id-1]["id"]
        for i in list1:
            if i["parent_exercise_id"]==i["id"]:
                print(serial,list1[parent_id-1]["name"])
                serial+=1
                break
            else:
                if i["parent_exercise_id"]!=idd:
                    print(serial,list1[parent_id-1]["name"])
                    print("  ",list1[parent_id-1]["content"])
                    serial+=1
                    break
        l=[]
        l1=[]
        new_no=1
        idd=list1[parent_id-1]["id"]

        for j in list2:
            if j["parent_exercise_id"]==idd:
                print("  ",new_no,j["name"])
                l.append(j["name"])
                l1.append(j["content"])
                new_no+=1
        
        child_id=int(input("which child id you want plese enetr :"))

        for i in range(len(l)):
            if child_id==i:
                print(l[i])
                print(l1[i])
                break

    elif file==True:
        my_file=open("course_exercises.json","r")
        data=json.load(my_file)

        print(get_url[choose-1]["name"],"-",get_url[choose-1]["id"])

        serial=1
        serial1=1
        list1=[]
        list2=[]

        for i in data["course"]["exercises"]:
            if i["parent_exercise_id"]==None:
                print(serial,i["name"])
                print("  ",serial1,i["slug"])
                serial+=1
                list1.append(i)
                list2.append(i)
            elif i["parent_exercise_id"]==i["id"]:
                print(serial,i["name"])
                serial+=1
                list1.append(i)
                new_no=1
            elif i["parent_exercise_id"]!=i["id"]:
                print("  ",new_no,i["name"])
                new_no+=1
                list2.append(i)
        file=os.path.exists("list1.json")
        file1=os.path.exists("list2.json")

        if file==True and file1==True:

            a=open("list1.json","r")
            b=json.load(a)
            a=open("list2.json","r")
            b=json.load(a)

            parent_id=int(input("which parent id you want to please enter :"))

            serial=1
            idd=list1[parent_id-1]["id"]
            for i in list1:
                if i["parent_exercise_id"]==i["id"]:
                    print(serial,list1[parent_id-1]["name"])
                    serial+=1
                    break
                else:
                    if i["parent_exercise_id"]!=idd:
                        print(serial,list1[parent_id-1]["name"])
                        print("  ",list1[parent_id-1]["content"])
                        serial+=1
                        break
            l=[]
            l1=[]
            new_no=1
            idd=list1[parent_id-1]["id"]

            for j in list2:
                if j["parent_exercise_id"]==idd:
                    print("  ",new_no,j["name"])
                    l.append(j["name"])
                    l1.append(j["content"])
                    new_no+=1
            
            child_id=int(input("which child id you want plese enetr :"))

            for i in range(len(l)):
                if child_id==i:
                    print(l[i])
                    print(l1[i])
                    break
        else:
            print("file not exists")

