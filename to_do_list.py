
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------
tasks=[]
next_task_id=max((task['id'] for task in tasks),default=0)+1
import re
from pathlib import Path
base_dir=Path(__file__).resolve().parent
task_file=base_dir/'tasks.json'

def is_valid_title(title)->bool:
    '''validate the task title.'''
    title_pattern=re.compile(r'[A-Za-z_][A-Za-z0-9_ ]{0,29}')
    if re.fullmatch(title_pattern,title): 
        return True
    return False
def is_valid_due_date(due_date)->bool:
    '''check whether the due date matches the expected YYYY-MM-DD format.'''
    date_pattern=re.compile(r'\d{4}-\d{2}-\d{2}')
    if re.fullmatch(date_pattern,due_date):
        return True
    return False

def add_task(title: str,description: str,priority: str,due_date: str): 
    '''Create a task and add it to the task list.'''
    task={'id':next_task_id,'title':title,'status':False,'priority':priority,'due_date':due_date,'description':description}
    tasks.append(task)
    return
# -----------------------------------------------------------------------------------------------------------------------------------------------------------------
def view_all_tasks():
    '''Display all tasks'''
    if not tasks:
        print('No tasks exist yet.')
        return
    print(' All tasks '.title().center(50,'='))
    for task in tasks:
        if task['status'] is False:
            result='pending'
        elif task['status'] is True:
            result='completed'
        print(f'Task ID : {task['id']}')
        print(f'Title : {task['title']}')
        print(f'Description : {task['description']}')
        print(f'Priority : {task['priority']}')
        print(f'Due date : {task['due_date']}')
        print(f'Status : {result}')
        print('-'*50)
    return
#----------------------------------------------------------------------------------------------------------------------------------------------------------------
def view_task(task):
    '''Display the details of a single task.'''
    if task['status'] is False:
        result='pending'
    elif task['status'] is True:
        result='completed'
    print(f'Task ID = {task['id']}')
    print(f'Title = {task['title']}')
    print(f'Description = {task['description']}')
    print(f'Priority = {task['priority']}')
    print(f'Due date = {task['due_date']}')
    print(f'Status = {result}')
    print('-'*50)
    return


# -----------------------------------------------------------------------------------------------------------------------------------------------------------------
def search_task(id:int)->None|dict:
    '''Find a task by its ID'''
    for task in tasks:
        if task['id'] == id:
            return task
    return None
# -----------------------------------------------------------------------------------------------------------------------------------------------------------------
def edit_task(id:int,field:str,new_value)->bool:
    '''Update a field of a task'''
    search=search_task(id)
    if search is None:
        return False
    search[field] = new_value   
    return True
# -----------------------------------------------------------------------------------------------------------------------------------------------------------------
def delete_task(id:int)->bool:
    '''Delete a task by its ID.'''
    search=search_task(id)
    if search is None:
        return False
    tasks.remove(search)
    return True
# -----------------------------------------------------------------------------------------------------------------------------------------------------------------
def mark_as_complete(id)->bool:
    '''Mark a task as completed.'''
    search=search_task(id)
    if search is None:
        return False
    search['status'] = True
    return True
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------
def view_tasks_by_status(status:bool):        
    '''Display tasks filtered by completion status.'''                   
    if not tasks:
        print('No tasks exist yet')         
        return
    if status is True:
        print('All completed task'.title().center(50,'='))
    elif status is False:
        print('All pending task'.title().center(50,'='))
    for task in tasks:
        if task['status'] == status:
            print(f'Task ID = {task['id']}')
            print(f'Title = {task['title']}')                              
            print(f'Description = {task['description']}')
            print(f'Priority = {task['priority']}')
            print(f'Due date = {task['due_date']}')
            print('-'*50)
    return
#---------------------------------------------------------------------------------------------------------------------------------------------------------------
import json
def save_tasks(tasks):
    with open(task_file,'w',encoding='utf-8') as file:
        json.dump(tasks,file,ensure_ascii=False,indent=4)

def load_tasks():
    try:
        with open(task_file,'r',encoding='utf-8') as file:
            tasks = json.load(file)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError as error:
        print(f'Error -> tasks.json contains invalid json'f'line({error.lineno},column {error.colno}).')
        raise SystemExit(1)
    if not isinstance(tasks,list):
        print('Error -> tasks.json must contain a list of tasks.')
        raise SystemExit(1)
    return tasks  
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------
tasks=load_tasks()
while True:
    print('=== TO-DO LIST ===')
    print('1- Add Task')
    print('2- View All Tasks')
    print('3- Search Task by ID')
    print('4- Edit Task')
    print('5- Delete Task')
    print('6- Mark Task as Completed')
    print('7- View Pending Tasks')
    print('8- View Completed Tasks')
    print('9- Exit')
    choice=input('Choose an option : ').strip()
    if choice not in {'1','2','3','4','5','6','7','8','9'}:
        print('Error -> Invalid choice.Please enter a number from 1 to 10')
        continue
    if choice == '1':
        while True:
            title=input('Enter task title : ').strip()
            if not is_valid_title(title):
                print('Error -> Invalid title.Please try again. ')
                continue
            break
        while True:
            print('1-Add a description')
            print('2- No description')
            description_choice=input('Choose an option : ').strip()
            if description_choice not in {'1','2'}:
                print('Error -> Invalid choice.Please enter 1 or 2 ')
                continue
            if description_choice == '1':
                description=input('Enter your description : ').strip()   
                if not description:
                    description = 'No description' 
                break 
            elif description_choice == '2':
                description= 'No description'
                break 
        while True:
            print('1- High')
            print('2- Medium')
            print('3- Low')
            priority_choice=input('Choose task priority : ').strip()
            if priority_choice not in {'1','2','3'}:
                print('Error -> Invalid choice.Please enter 1,2 or 3 ')
                continue
            if priority_choice == '1':
                priority='High'
                break
            elif priority_choice == '2':
                priority='Medium'
                break
            elif priority_choice == '3':
                priority='Low'
                break
        while True:
            print('1- Set a due date')
            print('2- No due date')
            due_date_choice=input('Choose an option : ').strip()
            if due_date_choice not in {'1','2'}:
                print('Error -> Invalid choice.Please enter 1 or 2')
                continue
            if due_date_choice == '1':
                while True:
                    due_date=input('Enter due date (YYYY-MM-DD) : ').strip()
                    if not is_valid_due_date(due_date):
                        print('Error -> Invalid date format.Please use YYYY-MM-DD. ')
                        continue
                    break
                break    
            elif due_date_choice == '2':                                   
                due_date= 'No due date'
                break
            
        add_task(title,description,priority,due_date)
        print(' task added successfully')
        save_tasks(tasks)
    elif choice == '2':
        view_all_tasks()
    elif choice == '3':
        while True:
            try:
                task_id=int(input('Enter the task ID to search for : ').strip())
            except ValueError:
                print('Error -> Invalid task ID.Please enter a whole number.')
                continue
            break
        search=search_task(task_id)
        if search is None:
            print('Error -> No task found with that ID.')
            continue
        view_task(search)
    elif choice == '4':
        while True:
            try:
                task_id=int(input('Enter the task ID to edit : ').strip())   
            except ValueError:
                print('Error -> Invalid task ID.Please enter a whole number ')   
                continue
            if search_task(task_id) is None:
                print('Error -> No task found with that ID.')
                break
            print('1- Edit Title')
            print('2- Edit Description')          
            print('3- Edit Priority')
            print('4- Edit Due date')
            print('5- Cancel Editing')
            edit_choice=input('Choose an option : ')
            if edit_choice not in {'1','2','3','4','5'}:
                print('Error -> Invalid choice.Please enter a number from 1 to 5 ')
                continue
            if edit_choice == '1':
                while True:
                    new_title=input('Enter the new task title : ').strip()
                    if not is_valid_title(new_title):
                        print('Error -> Invalid title.Please try again.')
                        continue
                    break
                title_edit=edit_task(task_id,'title',new_title)
                if title_edit is True:
                    print('Task updated successfully')
                    save_tasks(tasks)
                    continue 
            elif edit_choice == '2':
                while True:
                    print('1-Add a description')
                    print('2- No description')
                    new_description_choice=input('Choose an option : ').strip()
                    if new_description_choice not in {'1','2'}:
                        print('Error -> Your choice should be between 1 or 2 : ')
                        continue
                    if new_description_choice == '1':
                        new_description=input('Enter your task description : ').strip() 
                        if not new_description:
                            new_description ='No description' 

                    elif new_description_choice == '2':
                        new_description= 'No description'

                    description_edit=edit_task(task_id,'description',new_description)
                    if description_edit is True:
                        print('Task updated successfully')
                        save_tasks(tasks)
                        break
            elif edit_choice == '3':
                while True:
                    print('1- High')
                    print('2- Medium')
                    print('3- Low')
                    new_priority_choice=input('Choose the new task priority : ').strip()
                    if new_priority_choice not in {'1','2','3'}:
                        print('Error -> Invalid choice.Please enter 1 , 2 or 3.')
                        continue
                    if new_priority_choice == '1':
                        new_priority='High'
                        
                    elif new_priority_choice == '2':
                        new_priority='Medium'
                        
                    elif new_priority_choice == '3':
                        new_priority='Low'
                    priority_edit=edit_task(task_id,'priority',new_priority)
                    if priority_edit is True:
                        print('Task updated successfully')
                        save_tasks(tasks)
                        break
            elif edit_choice == '4':
                while True:
                    print('1- Set a new due date')
                    print('2- Remove the due date')
                    new_due_date_choice=input('Choose an option : ').strip()
                    if new_due_date_choice not in {'1','2'}:
                        print('Error -> your Choose should be between 1 or 2')
                        continue
                    if new_due_date_choice == '1':
                        while True:
                            new_due_date=input('Enter the new due date (YYYY-MM-DD) : ').strip()
                            if not is_valid_due_date(new_due_date):
                                print('Error -> Invalid date format.Please use (YYYY-MM-DD) ')
                                continue
                            break
                    elif new_due_date_choice == '2':                        
                        new_due_date= 'No due date'
                    due_date_edit=edit_task(task_id,'due_date',new_due_date)
                    if due_date_edit is True:
                        print('Task updated successfully')
                        save_tasks(tasks)
                        break
            elif edit_choice =='5':
                break
    elif choice == '5':
        while True:
            try:
                task_id=int(input('Enter the task ID to delete : ').strip())
            except ValueError:
                print('Error -> Invalid task ID.Please enter a whole number.')
                continue
            break
        search=search_task(task_id)
        if search is None:
            print('No task found with that ID.')
            continue
        while True:
            view_task(search)
            print('Are you sure you want to delete this task ?')
            print('1- Yes')
            print('2- No')
            delete_choice=input('Choose an option : ')
            if delete_choice not in {'1','2'}:
                print('Error -> Invalid choice.Please enter 1 or 2 ')
                continue
            if delete_choice == '1':
                delete_task(task_id)
                print('Task deleted successfully')
                save_tasks(tasks)
                break
            elif delete_choice == '2':  
                break        
    elif choice == '6':
        while True:
            try:
                task_id=int(input('Enter the task ID : ').strip())
            except ValueError:
                print('Error -> Invalid task ID.Please enter a whole number.')
                continue
            break
        change_status=mark_as_complete(task_id)
        if change_status is False:
            print('Error -> No task found with that ID.')
            continue
        if change_status is True:
            print('Task marked as completed') 
            save_tasks(tasks)                          
    elif choice == '7':
        view_tasks_by_status(False)
    elif choice == '8':
        view_tasks_by_status(True)
    elif choice == '9':
        break
        







        
            



