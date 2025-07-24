# def hello(name):
#     print("ค่าที่รับเข้ามาแสดงจาก function:" ,name)

# name = input("ค่าที่รับ : ")
# hello(name)


# def sum(a,b):
#      result = a + b
#      return result
    
# num1 = int(input("กรอกเลข1 : "))
# num2 = int(input("กรอกเลข2 : "))

# result = sum(num1,num2)
# print(result)

# def add(num1,num2):
#     result = num1 + num2
#     return result

# def main():
#     num1 = int(input("กรอกเลขที่1 : "))
#     num2 = int(input("กรอกเลขที่2 : "))
#     result = add(num1,num2)
#     print("ผลลัพธ์์จากการบอกคือ : " ,result)

# main()

def add(num1,num2):
    result = num1 + num2
    return result

def minus(num1,num2):
    result = num1 - num2
    return result

def mutiple(num1,num2):
    result = num1 * num2
    return result

def divide(num1,num2):
    result = num1 / num2
    return result
    # รอทำให้มันบอกว่าหารลงตัวหรือไม่

def is_even(num):
    result = num % 2
    if (result == 0):
        return("เป็นเลขคู่")
    else:
        return("เป็นเลขคี่")


def main():
    num1 = int(input("กรอกเลขที่1 : "))
    num2 = int(input("กรอกเลขที่2 : "))
    print(" + - * / เอาอันไหน : ")
    print("[1] +")
    print("[2] -")
    print("[3] *")
    print("[4] /")
    operation = input("เลือกสักอัน : ")

    if (operation == "1"):
        result = add(num1,num2)
        print("ผลลัพธ์จากการบอกคือ : " ,result)
    elif (operation == "2"):
        result = minus(num1,num2)
        print("ผลลัพธ์จากการลบคือ : " ,result)
    elif (operation == "3"):
        result = mutiple(num1,num2)
        print("ผลลัพธ์จากการคูณคือ : " ,result)
    elif (operation == "4"):
        result = divide(num1,num2)
        print("ผลลัพธ์จากการหารคือ : " ,result)

    print(is_even(result))

main()