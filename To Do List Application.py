#create a function for adding tasks to the task list
def Add_Task():
    #prompt the user what task they want to add
    add_task = input("What task would you like to add? ")
    #add a status to the task, default 'incomplete'
    add_task = add_task + " (incomplete)"
    #format the task string
    add_task = add_task.capitalize()
    #add the task to the task list
    task_list.append(add_task)

#make a function to view tasks formatted in a specific way
def View_Tasks():
    #iterate through the list of tasks, leaving out the last element
    for i in range(len(task_list) - 1):
        #print out each element, separating each element with a comma and space
        print(task_list[i], end = ", ")
    #then print out the last item in the list
    print(task_list[-1])

#create a function that allows the user to mark tasks as complete
def Mark_Complete():
    #prompt the user for which task they want to complete
    completed_task = input("Which task would you like to mark as complete? ")
    #capitalize the task specified to match the formatting of the added tasks
    completed_task = completed_task.capitalize()
    #iterate through the list of tasks
    for i in range(len(task_list)):
        #if the completed task is in the task list, replace the 'incomplete' status with a 'completed' status
        if completed_task in task_list[i]:
            task_list[i] = task_list[i].replace("incomplete", "completed")
            #exit the loop once a status is changed
            break

#make a function to delete tasks from the task list
def Delete_Task():
    #prompt the user for what task they would like to delete
    remove_task = input("What task would you like to remove? ")
    #format the user input to match the formatting of the tasks in the list
    remove_task = remove_task.capitalize()
    #iterate throught the list of tasks
    for i in range(len(task_list)):
        #if the task the user would like to delete is in the list of tasks, remove it from the list
        if remove_task in task_list[i]:
            task_list.remove(task_list[i])
            #exit the loop once the task is removed to avoid errors
            break

#make a new list 
task_list = []

#introduce the user to the app and give them a list of items to select from
print("Welcome to the To-Do List App!")
print("Menu:")
print("1. Add a task")
print("2. View tasks")
print("3. Mark a task as complete")
print("4. Delete a task")
print("5. Quit")

#prompt the user to make a selection and convert it to an integer, test it to make sure they enter a whole number
try:
    user_selection = int(input("Which selection would you like to make? "))
#if the user doesn't enter a whole number, prompt them to select a valid input, then set user_selection to zero
except ValueError:
    print("Please choose the number of the selection you want to make.")
    user_selection = 0

#use a while loop to allow the user to make multiple selections until they want to quit the app
while user_selection != 5:
    #add a selection for adding tasks and use the predefined Add_Task function
    if user_selection == 1:
        Add_Task()
    #add a selection for viewing tasks using the View_Task function
    elif user_selection == 2:
        View_Tasks()
    #add a selection for maring tasks as complete using the Mark_Complete function
    elif user_selection == 3:
        Mark_Complete()
    #add a selection for deleting tasks with the Delete_Task function
    elif user_selection == 4:
        Delete_Task()
    #this is a default selection that restarts the loop without any more prompts or output
    elif user_selection == 0:
        pass
    #handles any numeric input that is outside the bounds of our options, sets user_selection to zero
    elif user_selection > 5 or user_selection < 0:
        print("Please make a valid selection.")
        user_selection = 0

    #the end of the loop that feeds back in to the beginnging, prompting the user to make another selection
    try:
        #test the selection to make sure it is a proper input
        user_selection = int(input("Which selection would you like to make? "))
    #if it is not a whole number, request the user select a valid input and set user_selection to zero to restart the loop
    except ValueError:
        print("Please choose the number of the selection you want to make.")
        user_selection = 0

#thank the user for using the app once they have quit
print("Thank you for using the To-Do List App! Good-bye!")