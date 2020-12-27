user_number=int(input("please input users number : "))


informations=[]

while user_number>0:
    first_name=input("please input first name : ")
    last_name=input("please input last name : ")
    age=int(input("please input age : "))
    d_year=int(input("please input date of birth (just year) : "))
    c={"first_name":first_name,"last_name":last_name,"age":age,"d_year":d_year}
    informations.append(c)
    user_number-=1  

for i in informations:
    print("first_name: {}\nlast_name: {}\nage: {}\nd_year: {}".format(i["first_name"],i["last_name"],i["age"],i["d_year"]))
    if i["age"]<=18 or i["d_year"]>=2002:
        print("----> {} is cant go out because it's too dengerous !!".format(i["first_name"]))
    else:
        print("----> {} is can go out the street".format(i["first_name"]))        