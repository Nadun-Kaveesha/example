#main menu
#initialize the variables
choice=0
Project_code=0
Clients_name=''
Start_date=0
End_date=0
No_workers=0
Project_status=0
Save=0
Project_code=0
Project_status=0
Update=0
No_projects=0
No_cprojects=0
No_oprojects=0
workers=0
Aproject=0

#input
print("\nMain Menu")
print("1.Add a new project to existing projects")
print("2.Remove a completed project from existing project")
print("3.Add new workers to available workers group")
print("4.Update detail on on going projects")
print("5.Project statics")
print("6.Exit")
choice=int(input("\nInput Your choice :"))

if choice==1 :
    
#add new project
#initializethe variables
    
#input the values
    def Add_a_new_project():
        print("\nAdd a new project")
        Project_code=int(input("Project Code :"))
        Clients_name=str(input("Client's Name :"))
        Start_date=str(input("Project Starting Date :"))
        End_date=str(input("Expected project ending date :"))
        No_workers=input("Number of workers :")
        Project_status=str(input("Project status :"))
        Save=input("Do you want to save the project?(Yes/No) :")
        Add=[[Project_code],[Clients_name],[Start_date],[End_date],[No_workers],[Project_status],[Save]]
        print(Add)
#process
    Add_a_new_project()    
elif choice==2:
     
#remove completed project
#initialize the variables
    Project_code=0
    Remove=0
#input the values
    def RemoveProject():
        global Project_code,Remove
        print("\nRemove completed project :")
        Project_code=input("Project Code :")
        Remove=input("Do you want to remove the project?(Yes/No) :")
          
#process
    RemoveProject()
elif choice==4:
    

#update project details
#initialize the variabbles
    
    def update():
        print("\nUpdated project details")
        Project_code=int(input("Enter project code :"))
        Clients_name=str(input("Enter client's name :"))
        Start_date=(input('Enter input date :'))
        End_date=str(input("Expected project ending date :"))
        Project_status=str(input("Project status :"))
        Update=input("Do you want to update the project?(Yes/No) :")
    update=[[Project_code],[Clients_name],[Start_date],[End_date],[Project_status],[Update]]    
#process    
    update()
elif choice==5:
    
#project statics
#initialize the variables
    
    def statics():
        print("\nProject Statics")
        No_projects=int(input("Enter the number of ongoing projects :"))
        No_cprojects=int(input("Enter the number of completedd projects :"))
        No_oprojects=int(input("Enter the number of onhold pprojects :"))
        workers=int(input('Enter the number of workers available to assign :'))
        Aproject=(input("Do you want to add the project(Yes/No) :"))
        if Aproject=='Yes':
            return Add_a_new_project()
        else:
            exitt()
        
#process
    statics()    
elif choice==3:
    No_workers=0
    dw_add=0
    def  workers():
        print("\nAdd new workers")
        No_workers=int(input("Enter the nuumber of workers to add"))
        dw_add=str(input("Do you want to add?(Yes/No):"))
#process
    workers()
elif choice==6:
    def exitt():
        print("You,ve succesfully exited the programme")
    exitt()     
    

else:
    print("Invalid Input")



# Function definitions


''''def add_new_project():
    print("\nAdd a new project")
    project_code = int(input("Project Code: "))
    clients_name = input("Client's Name: ")
    start_date = input("Project Starting Date: ")
    end_date = input("Expected project ending date: ")
    no_workers = input("Number of workers: ")
    project_status = input("Project status: ")
    save = input("Do you want to save the project? (Yes/No): ")
    return [[project_code], [clients_name], [start_date], [end_date], [no_workers], [project_status], [save]]


def remove_project():
    print("\nRemove completed project:")
    project_code = input("Project Code: ")
    remove = input("Do you want to remove the project? (Yes/No): ")
    return project_code, remove


def update_project():
    print("\nUpdate project details")
    project_code = int(input("Enter project code: "))
    clients_name = input("Enter client's name: ")
    start_date = input('Enter start date: ')
    end_date = input("Expected project ending date: ")
    project_status = input("Project status: ")
    update = input("Do you want to update the project? (Yes/No): ")
    return [[project_code], [clients_name], [start_date], [end_date], [project_status], [update]]


def project_statistics():
    print("\nProject Statistics")
    no_projects = int(input("Enter the number of ongoing projects: "))
    no_completed_projects = int(input("Enter the number of completed projects: "))
    no_on_hold_projects = int(input("Enter the number of on-hold projects: "))
    workers_available = int(input('Enter the number of workers available to assign: '))
    add_project = input("Do you want to add a project? (Yes/No): ")
    if add_project == 'Yes' or add_project == 'yes':
        return add_new_project()
    else:
        return None  


def add_workers():
    print("\nAdd new workers")
    no_workers = int(input("Enter the number of workers to add: "))
    add_workers = input("Do you want to add? (Yes/No): ")
    return no_workers, add_workers


def exit_program():
    print("You've successfully exited the program")


choice = int(input("\nMain Menu\n"
                   "1. Add a new project to existing projects\n"
                   "2. Remove a completed project from existing projects\n"
                   "3. Add new workers to available workers group\n"
                   "4. Update details on ongoing projects\n"
                   "5. Project statistics\n"
                   "6. Exit\n"
                   "Input Your choice: "))

if choice == 1:
    new_project_data = add_new_project()
    print(new_project_data)

elif choice == 2:
    project_code, remove = remove_project()
    print(f"Project code: {project_code}, Remove: {remove}")

elif choice == 3:
    no_workers, add_workers = add_workers()
    print(f"No. of workers: {no_workers}, Add workers: {add_workers}")

elif choice == 4:
    updated_data = update_project()
    print(updated_data)

elif choice == 5:
    statistics_data = project_statistics()
    if statistics_data:
        print(statistics_data)

elif choice == 6:
    exit_program()

else:
    print("Invalid Input")
'''