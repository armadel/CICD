# Define an empty list to store tasks
tasks = []

# Function to add a task
def add_task(task):
    tasks.append(task)
    print(f"Task '{task}' added!")

# Function to list tasks
def list_tasks():
    if not tasks:
        print("No tasks found.")
    else:
        print("Tasks:")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")

# Function to remove a task
def remove_task(task_number):
    try:
        task_number = int(task_number)
        if 1 <= task_number <= len(tasks):
            removed_task = tasks.pop(task_number - 1)
            print(f"Task '{removed_task}' removed!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input. Please enter a valid task number.")

# Main loop
while True:
    print("\nOptions:")
    print("1. Add task")
    print("2. List tasks")
    print("3. Remove task")
    print("4. Quit")

    choice = input("Enter your choice: ")

    if choice == '1':
        task = input("Enter task: ")
        add_task(task)
    elif choice == '2':
        list_tasks()
    elif choice == '3':
        task_number = input("Enter task number to remove: ")
        remove_task(task_number)
    elif choice == '4':
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a valid option.")
