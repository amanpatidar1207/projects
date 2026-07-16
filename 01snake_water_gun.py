import random

computer =random.choice([1,2,3])
my = input("enter the your choice      :")
mydict = {"s": 1,
          "w": 2,
          "g": 3}

reversedict ={1 : "🐍",
              2 : "🌊",
              3 : "🔫"}
mychoice = mydict[my]

print(f"enter your choice {reversedict[mychoice]}\ncomputer choise {reversedict[computer]}")

if(computer==mychoice):
    print("the match is drowwww")

else:
    if(computer==1 and mychoice==2):
        print("computer  win")

    elif(computer==2 and mychoice==1):
        print("i am win   win")

    elif(computer==2 and mychoice==3):
        print("computer   win")

    elif(computer==3 and mychoice==2):
        print("i am win   win")

    elif(computer==3 and mychoice==1):
        print("computer   win")

    elif(computer==1 and mychoice==3):
        print("i am win   win")

    else:
        print("some thing is wrong ma chuda")
