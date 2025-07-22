distance = int(input("enter your distance = "))

if (distance <= 4):
    print("0 bath")
elif (distance <= 50):
    print("10 bath")
elif (distance <= 100):
    print("15 bath")
elif (distance <= 300):
    print("20 bath")
elif (distance <= 500):
    print("25 bath")
else :
    print("45 bath")