import random
import string

print ("Namaste sir 🙏 swagat hai hamari password generate webside pe ")

length = int(input("Sir Enter the lengthe of password do  you need "))

print("\n")

charactors = string.ascii_letters + string.digits
# ye aman bahi yye kar raha hai ki yye alphabate orr digit hi lega 

password = ""

for i in range(length):
    password += random.choice(charactors)


print(f"sir your password is   😎    [ {password} ]")

print("thanks for visit webside  have a nice day ✌️")
