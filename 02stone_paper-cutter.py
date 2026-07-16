import random 

computer = random.choice([1,-1,0])
you = input("Enter your choice ")
mydict = {"s" : 1,
          "p" : -1,
          "c" : 0}

reversedict = {1 : "🪨",
              -1 : "📃",
               0  : "🗡️" }

yourchoice = mydict[you]

print(f"your choice  {reversedict[yourchoice]}\ncomputerr choice  {reversedict[computer]}")

if (computer==yourchoice):
    print("droww")

else:
    if (computer == 1 and yourchoice == -1):
        print("you win ")
    elif(computer == -1  and yourchoice== 1):
        print("computer win ")  
    elif(computer == 1  and yourchoice == 0):
        print("computer win ")  
    elif(computer == 0  and yourchoice == 1):
        print("you win ")  
    elif(computer == -1  and yourchoice == 0):
        print("you win ")  
    elif(computer == 0  and yourchoice == -1):
        print("computer win ")  

    else :
        print("some thing is wrong ")


    