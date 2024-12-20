def display_tasks(tasks):
    if not tasks:
        print("Your to-do list is empty!")
    else:
        print("Your To-Do List:")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")

def add_task(tasks):
    task = input("Enter the task you want to add: ")
    tasks.append(task)
    print(f"Task '{task}' added!")

def update_task(tasks):
    display_tasks(tasks)
    task_index = int(input("Enter the task number you want to update: ")) - 1
    if 0 <= task_index < len(tasks):
        new_task = input("Enter the new task: ")
        tasks[task_index] = new_task
        print("Task updated!")
    else:
        print("Invalid task number.")

def delete_task(tasks):
    display_tasks(tasks)
    task_index = int(input("Enter the task number you want to delete: ")) - 1
    if 0 <= task_index < len(tasks):
        removed_task = tasks.pop(task_index)
        print(f"Task '{removed_task}' deleted!")
    else:
        print("Invalid task number.")

def to_do_list_app():
    tasks = []
    while True:
        print("\nOptions: 1. Add Task 2. Update Task 3. Delete Task 4. View Tasks 5. Exit")
        choice = input("Choose an option: ")
        
        if choice == '1':
            add_task(tasks)
        elif choice == '2':
            update_task(tasks)
        elif choice == '3':
            delete_task(tasks)
        elif choice == '4':
            display_tasks(tasks)
        elif choice == '5':
            print("Exiting the To-Do List application.")
            break
        else:
            print("Invalid option. Please try again.")

to_do_list_app()
number_guessing_game()