# TO-DO LIST

Tasks = dict() # defining global dictionary of the to-do list

def main():

    # Greeting the user
    print("WELCOME TO YOUR TO-DO LIST!")

    # Reading the file that contains the saved To-do list
    try:
        with open("TODO.txt","r") as file:
            for line in file:
                key, value = line.split(" | ",1)
                Tasks.update({key.strip(): value.rstrip("\n").strip()})
    except Exception:
        pass

    while True:
        # Validating input and showing options menu
        choice = show_menu()
        # executing choices
        match choice:
            case 1:
                add_task()
            case 2:
                view_list()
            case 3:
                mark_done()
            case 4:
                remove_task()
            case 5:
                # Quitting the program
                print_sep()
                print("SEE YOU NEXT TIME!")
                break

    # Storing the To-do list inside a file for later retrieval
    print("TO-DO LIST SAVED INSIDE \"TODO.txt\".")
    with open("TODO.txt", "w") as file:
        for key in Tasks:
            file.write(f"{key} | {Tasks[key]}\n")


        

# Showing options menu
def show_menu():
    print_sep()
    print("""Options:                    
    1. Add a task
    2. View TO-DO list
    3. Mark task as DONE
    4. Remove a task
    5. Quit
    """)

    # Validating the input of the user
    while True:
        try:
            option = int(input("Choose Option: "))
            if option not in range(1,6):
                raise ValueError
            return option
        except ValueError:
            print("Please Enter a Valid choice!")

# Printing a Line Break for Styling
def print_sep():
    print("------------------------")

# Adding tasks to the Todo list
def add_task(): 
    # Get the task from the user
    while True:
        task = input("Enter a task: ")
        # Check if the task is already in the list
        if task.upper().strip() in Tasks:
            print("Task is already in the list!")
        elif len(task) <= 1 or task.isdigit() or task.isspace():
            print("Enter a valid task!")
        else:
            Tasks.update({task.upper().strip(): "PENDING"})
            print_sep()
            print("Task ADDED successfully.")
            break

# Viewing the Todo list
def view_list():
    if check_length():
        print_list()

# Printing the Todo list
def print_list():
    print_sep()
    for i,task in enumerate(Tasks):
        print(f"{i+1}. {task} ---> {Tasks[task]}")
        

# Marking tasks DONE
def mark_done(): 
    if not check_length():
        return
    number = check_task_no("MARK DONE")    
    for i, k in enumerate(Tasks):
        if number == i + 1:
            if Tasks[k] == "DONE":
                print_sep()
                print("Task is Already marked DONE.")
            else:
                Tasks[k] = "DONE"
                print_sep()
                print("Task CHECKED OFF successfully.")
            break

# Removing a task from the Todo list 
def remove_task():
    if not check_length():
        return
    number = check_task_no("REMOVE")
    for i, k in enumerate(Tasks):
        if i + 1 == number:       
            del Tasks[k]
            print_sep()
            print("Task REMOVED successfully.")
            break
    
    
# Checking whether the list is empty
def check_length():
    length = len(Tasks)
    if length == 0:
        print("TO-DO list is EMPTY...")
        return False
    return True

# Validate the order of the task to remove or check of
def check_task_no(prompt):
    while True:
            print_list()
            try:
                task_no = int(input(f"Choose a task to {prompt}:"))
                if not(task_no in range(len(Tasks) + 1)) or task_no <= 0:
                    print("Enter a valid number!")
                    continue
                return task_no    
            except ValueError:
                print("Enter a digit!")


if __name__ == "__main__":
    main()
