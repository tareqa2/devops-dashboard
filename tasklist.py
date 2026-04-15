def manage_tasks():
    tasks = []

    while True:
        print("\n=== Task List ===")
        print("[1] Add Task")
        print("[2] View Tasks")
        print("[3] Remove Task")
        print("[0] Back to Main Menu")

        choice = input("Select an option: ")

        if choice == "1":
            task = input("Enter new task: ")
            tasks.append(task)
            print("Task added.")

        elif choice == "2":
            if not tasks:
                print("No tasks available.")
            else:
                print("\nTasks:")
                for i, task in enumerate(tasks, start=1):
                    print(f"{i}. {task}")

        elif choice == "3":
            if not tasks:
                print("No tasks to remove.")
            else:
                for i, task in enumerate(tasks, start=1):
                    print(f"{i}. {task}")
                try:
                    num = int(input("Enter task number to remove: "))
                    if 1 <= num <= len(tasks):
                        removed = tasks.pop(num - 1)
                        print(f"Removed: {removed}")
                    else:
                        print("Invalid number.")
                except ValueError:
                    print("Please enter a valid number.")

        elif choice == "0":
            break

        else:
            print("Invalid choice, try again.")
