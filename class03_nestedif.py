username = input ("Username: ")
password = input ("Pasword: ")

if username == "admin":
    if password == "admin123": 
        print("You're admin")
    else :
        print("wrong" )
elif username == "user":
    if password == "user123":  
        print("You're user" )
    else: 
        print("wrong" )
else: 
    print("not found" )


#-------------------------------

x = "ตะแน่ว"

x += "เดอะมอลบางกะปิ"

print(x)

x = "1"
y = "2"
z = "3"



story = input("ทำอะไรต่อ: ")
word = ""

if story == "1":
    word += "เนื้อเรื่อง 1"
    story2 = input("ทำอะไรต่อไป 1 หรือ 2 ")
    if story2 == 1:
        word += "ลุกขึ้น"
    elif story2 == 2: 
        word += "นอนต่อ"
elif story == "2":
    word += "เนื้อเรื่อง 2"
    story2 = input("ทำอะไรต่อไป 1 หรือ 2 ")
    if story2 == 1:
        word += "กินข้าว"
    elif story2 == 2:
        word += "อาบน้ำๆ"
