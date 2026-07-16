import random

print("welcome in man gaming seris🙏 ")
print("this game is made by aman in 24-6-2026  😎 ")
print("the game name is perfect gusss ✌️\n")



randomNO = random.randint(1,100)

gusses = 0
a = -1
while(a != randomNO):
    gusses += 1
    a = int (input("Enter the your number   🙌:"))
    if (a<randomNO):
        print ("thoda bada number socho  ")

    elif(a>randomNO):
        print("thoda chota number socho \n")

    else:
        print(f"your choice is correct  in  🤜   ({gusses})   🤛   attempts")


print("\n")
print("thanks to playing this game i hope you are fellin happy  😊😁")


