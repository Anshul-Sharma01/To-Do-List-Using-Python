# A simple and basic to-do list:

tasks=[]
ans=True
while ans:
    print("-----------------------------------------------------------------------------")
    print("-----------------------------------------------------------------------------")
    print("--------------Welcome to To-do List--------------")
    print("1.Add a task")
    print("2.View your tasks")
    print("3.Remove a Task")
    print("4.Mark the task as Complete")
    print("5.Quit")
    print("-----------------------------------------------------------------------------")
    try:
        ch=int(input("Please enter your choice:-"))
    except ValueError:
        print("-----------------------Invalid Input-----------------------")
        continue
    if ch==1:
        task_description=input("Please enter your task:-")
        tasks.append({"Task":task_description,"Status":False})
        print("-----------------------Task Added Successfully-----------------------")
    elif ch==2:
        if not tasks:
            print("-----------------------No Tasks to Display-----------------------")
        else:
            print("Tasks:")
            for ind,task in enumerate(tasks):
               st="Completed" if task["Status"] else "Incomplete"
               print(f"{ind+1}.{task['Task']} --->({st})")
            print("-----------------------Tasks viewed successfully-----------------------")
    elif ch==3:
        if not tasks:
            print("-----------------------No Tasks to Remove-----------------------")
        else:
            print("Tasks:")
            for ind, task in enumerate(tasks):
                st = "Completed" if task["Status"] else "Incomplete"
                print(f"{ind + 1}.{task['Task']} --->({st})")
            print("-----------------------Tasks viewed successfully-----------------------")
            try:
               ele=int(input("Please enter the index of the task you want to delete:"))-1
               if 0 <=ele<len(tasks):
                  rem=tasks.pop(ele)
                  print(f"-----------------------The {rem} is successfully removed from the tasks list!!-----------------------")
               else:
                  print("-----------------------Invalid Input-----------------------")
            except ValueError:
               print("-----------------------Task Added Successfully-----------------------")
               continue

    elif ch==4:
        if not tasks:
            print("-----------------------No Tasks to mark complete-----------------------")
        else:
            print("Tasks:")
            for ind, task in enumerate(tasks):
                st = "Completed" if task["Status"] else "Incomplete"
                print(f"{ind + 1}.{task['Task']} --->({st})")
            print("-----------------------Tasks viewed successfully-----------------------")

            try:
               ele=int(input("Please enter the index of the task you want to mark as complete:"))-1
               if 0<=ele<len(tasks):
                   tasks[ele]["Status"]=True
                   print("-----------------------Task successfully marked Complete-----------------------")
               else:
                   print("-----------------------Invalid Input-----------------------")
            except ValueError:
               print("-----------------------Task Added Successfully-----------------------")

    elif ch==5:
        ans=False
        print("-----------------------Thanks for using-----------------------")

    else:
        print("-----------------------Invalid Choice-----------------------")
        print("Select again!!!")



#  this project is completed and can be modified by using tkinter
# completed on 12-09-23