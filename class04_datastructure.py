# x = ["Sun","Tik"]

# print(x)

# x[1] = "Vava"

# print(x)

# x.append("Ton")

# print(x)

# x = ["Sun","Tik"]

# x.pop()

# print(x)

# x = ["Sun","Tik","Ton","Vava","Gap"]

# print(len(x))
# len ใช้บอกจำนวน

# for i in range(len(x)):
#     print(x[i])

# for speaker in x:
#     print(speaker)

# score = [99,10,23,50]
# sum = 0

# for i in range(len(score)):
#     print(sum)
#     sum += score[i]

# print("total : ",sum)

# num = [1,2,3,4,5,6,7,8,9,10]

# for number in num:
#     if (number % 2 == 0):
#         print("Even : ",number)
#     else:
#         print("Odd : ",number)

# x = {"name","Sun","sid":681305}
                        
# x["score"] = 100

# x["name"] = "Tik"

# print(x)

# student = [ 
#     {"name":"Sun","id":681305,"score":100},
#     {"name":"Tik","id":681305,"score":1000},
# ]

# for student in student:
#     print(student["name"])

student = [
    {"name":"Tom","id":11,"score":85},
    {"name":"Tood","id":12,"score":75},
    {"name":"Lek","id":13,"score":65},
]

for student in student:
    if (student["score"] >= 80):
        student["score"] = "A"
    elif (student["score"] >= 70):
        student["score"] = "B"
    elif (student["score"] >= 60):
        student["score"] = "C"
    else:
        student["score"] = "F"
    print(student)