import random

print("coin🪙 toss kiya ja raha hai aaapni choice batao  ")
coin = random.randint(1,2)
my = str(input("enter your choice    :"))


mydict = {
    "h" : 1,
    "t" : 2
}

reversedict = {
    1 : "head",
    2 : "tail"
}

mychoice = mydict[my]

print(f"the choice of aman is {reversedict[mychoice]} \n the result of toss of coin  {reversedict[coin]} ")

if (mychoice == coin ):
    print ("you are win the toss   ")

else:
    print("you are lose the toss   ")

# ye mera pehla bina kisi  help ke priject hai 

