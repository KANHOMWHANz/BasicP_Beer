# sum = 0
# n = 3

# for i in range(n):
#    sum += i+1

# print(sum)


# for i in range(10):
#    print(i*i)



#x = int(input("สูตรคูณแม่"))
#n = 13

#for i in range(n):
#    print(x, "x" , i , "=" ,x*i)

#start = True
#while start:
#    print("ให้ทาย")
#    print("อันที่1")
#    print("อันที่2")
#    x = int(input("กรุณากรอกเลข"))
#    if (x == 1):
#        print("เลือกข้อที่ 1")
#    elif (x == 2):
#        print("เลือกข้อที่ 2")
#    start = false


monster = 100

weapon1 = 40
weapon2 = 30
weapon3 = 20

gamestart = True
while gamestart:
    print("----Welcome----")
    print("ต่อสู้มอนเตอร์(1) หรือ ออก(2)")
    choose = int(input("1 or 2 :"))
    if choose == 1:
        print("จำนวนครั้งในการโจมตี")
        count = int(input("จำนวนครั้ง"))
        for i in range(count):
            print("เลือกอาวุธ")
            print("อาวุธที่1ดาเมจ : " ,weapon1)
            print("อาวุธที่2ดาเมจ : " ,weapon2)
            print("อาวุธที่3ดาเมจ : " ,weapon3)

            print("เลือดของมอนเตอร์ : " ,monster)
            print("จำนวนครั้งในการโจมตีที่เหลืออยู่", count - i)
            weapon = int(input("เลือกอาวุธในรอบนี้ : "))
            print("อาวุธที่คุณเลือก" ,weapon)
            if (weapon == 1):
                monster -= weapon1
                if (monster < 0):
                    print("ตีแรงเกินไปเลือดมอนเตอร์เด้งไปเหลือ 20 !!!")
                    monster = 20
            elif

            else
            

    if choose == 2:
        print("ออก")
        break

