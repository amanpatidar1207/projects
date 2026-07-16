def todo_app():
    todo_list = []
    print("welcome sir in todo list app apka swagat karta hai  ")

    while True:
        print("\n1 for viwe todo list ")
        print("2 for add task   ")
        print("3 for remove task  ")
        print("4 for exit ")

        chose = input("enter the nuber btw (1 - 4)")

        if chose == '1':
            if not todo_list:
                print ("\n😁your todo list is empty  swahhhaaa \n")

            else:
                print("\n--- Your Current Tasks ---\n")
                for index, task in enumerate(todo_list, 1):
                    print(f"{index}. {task}") 


        elif chose == '2':
            new_task = input("enter the task which do you added   :")
            if new_task:
                todo_list.append(new_task)
                print(f"new task is added ({new_task})")

            else:
                print ("no task innter in input  ")


        elif chose == '3':
            if not todo_list:
                print("todo  list is empaty     ")

            else:
                print("\n--- Current Tasks ---")
                for index, task in enumerate(todo_list, 1):
                    print(f"{index}. {task}")

                try :
                    task_num = int(input("\nEnter the number of the task to delete: "))
                    if 1 <= task_num <= len(todo_list):
                        removed = todo_list.pop(task_num - 1)
                        print(f"Task '{removed}' has been deleted!")
                    else:
                        print("Invalid task number!")
                except ValueError:
                    print("Please enter a valid number.")

        elif chose == '4':
            print("you are exit from todo list 🎉🙏")
            
            break


todo_app()
