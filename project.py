import sys

students=["sevval yo","betul ak","erdem ku","hilal yil"]

counter=3
while counter>0:
    name_surname=input("please enter the name and surname (Write to all lowercase) : ")

    if name_surname not in students:
        counter-=1
        if counter==0:
            sys.exit("Please try again later")
        print("try again, you have",+ counter,"turns")

    else:
        print("welcome",name_surname)  
        break

count=0
dersler=[]
while 3>=count or count<5:
    print("Once you have written enough lessons, press q to exit.")
    ders=input("please input lessons name :  " )
    dersler.append(ders)
    count+=1
    if ders=="q":
        dersler.pop()
        if len(dersler)<3: 
            print("you can't less than 3 lessons")
            print("please enter some  lesson")
            ders=input("please input some lesson name : " )
            dersler.append(ders)

        break
    
print("lessons : ",dersler)

import random
lesson=random.choice(dersler)
print("please you input the ", lesson.upper(),"lesson grades")
midterm=int(input("midterm grade : "))
final=int(input("final grades : "))
project=int(input("project grade : "))
grades={"midterm":midterm,"final":final,"project":project}
print(grades)


passing_grade=(grades.get("midterm")*30/100) + (grades.get("final")*50/100) + (grades.get("project")*20/100)
print("passing grade is : ",passing_grade)   
if passing_grade > 90:
    print("AA")
elif passing_grade>70 and passing_grade <90:
    print("BB")         
elif passing_grade>50 and passing_grade <70:
    print("CC")
elif passing_grade>30 and passing_grade <50:
    print("DD")
else:
    print("FF")
    print("you are failure this lesson")            
