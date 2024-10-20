# Simple To-Do List Application (1-tier architecture)


def display_tasks(tasks):
    if not tasks: print("No tasks")
    else:
        print("To-Do List")
        for idx, task in enumerate(tasks, start=1):
            print(f"{idx}, {task}")

def add_task(tasks):
    task = input("")
    tasks.append(task)
    print(f"Task {task} added.")

def delete_task(tasks):
    display_tasks(tasks)
    if tasks:
        task_num = int(input("Enter the task number to delete: "))
    if 1 <= task_num <= len(tasks):
        removed_task = tasks.pop(task_num - 1)
        print(f"Task '{removed_task}' deleted.")
    else:
        print("Invalid task number.")

def main():
    print("Tasks Menu")
    print("1: View Tasks, 2: Add Tasks, 3: Delete Tasks, 4: Exit")

if __name__ == "__main__":
    main()

def main():
    tasks = []
    while True:
        print("\nSimple To-Do List")
        print("1. View tasks")
        print("2. Add task")
        print("3. Delete task")
        print("4. Exit")
        choice = input("Enter choice (1/2/3/4): ")
        if choice == '1':
            display_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
        elif choice == '3':
            delete_task(tasks)
        elif choice == '4':
            print("Exiting the application.")
            break
        else:
            print("Invalid input")
if __name__ == "__main__":
    main()