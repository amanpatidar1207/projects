print("namaste sir welcome aman projecj name calculator 🙏")

def add(x,y):
    return x + y

def sub(x,y):
    return x-y

def mul(x,y):
    return x*y

def devide(x,y):
    if (y==0):
        return "number is invalide for sub "
    return x/y


def calculator():
    print("1 for addition ")
    print("2 for subraction")
    print("3 for multiply")
    print("4 for divide ")
    print ("5 for exit the calculator")

    while True:
        choice =input("\nthe choise in (1/2/3/4/5)     :")
        print("\n")

        if choice =='5':
            print("you are exit  from calculator  byeee sir   :")
            break
         
        if choice in ("1/2/3/4"):
            try:
                num1 = float(input("enter the number 1st  :"))
                num2 = float(input("enter the number 2bd  :"))

            except ValueError:
                print("you inter the invallid number   ")

            if choice == '1':
                print (f"{num1} + {num2}  == {add(num1,num2)}")
            elif choice == '2':
                print (f"{num1} - {num2}  == {sub(num1,num2)}")
            elif choice == '3':
                print (f"{num1} * {num2}  == {mul(num1,num2)}")
            elif choice == '4':
                print (f"{num1} / {num2}  == {devide(num1,num2)}")
             
    
         


calculator()
         