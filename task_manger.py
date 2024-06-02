def task():
    tasks=[] # empty list
    print("Welcome to task manager................")
    total_task=int(input("How many tasks you want to add: "))
    for i in range(1,total_task+1):
        task_name=input(f"Enter the name of the task {i}=")
        tasks.append(task_name)

    print(f"Todays tasks are\n{tasks}")  

    while(True):
        operation=int(input("Enter 1 for Add\nEnter 2 for Update\nEnter 3 for Delete\nEnter 4 for View\nEnter 5 for Exit/Stop"))  
        if operation ==1:
            add=input("Enter your task you want to add:")
            tasks.append(add)
            print(f"task {add} has been added..........")
        elif operation==2:
            updated_val=input("Enter your task  name you want to update:")
            if updated_val in tasks:
                up=input("Enter the new task")
                ind=tasks.index(updated_val)
                tasks[ind]=up
                print(f"your updated task {up} has been updated.......")
        elif operation==3:
            del_task=input("enter the task you want to delete:")
            if del_task in tasks:
                ind=tasks.index(del_task) 
                del tasks[ind]
                print(f"your task {del_task} has been removed...") 
        elif operation==4:
            print(f"your tasks are {tasks}") 
        elif operation==5:
            print("the task manager is sing out....")    
        else:
            print("Enter a valid input please..")
task()            


                


