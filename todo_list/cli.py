#!/usr/bin/env python3

import sys

TODO_FILE = "tasks.txt"

def add_task(task):
    with open(TODO_FILE, "a") as f:
        f.write(task + "\n")
    print(f"Added task: {task}")

def list_tasks():
    try:
        with open(TODO_FILE, "r") as f:
            tasks = f.readlines()
        if not tasks:
            print("Empty list")
        else:
            print("📋 TODO LIST:")
            for i, task in enumerate(tasks, 1):
                print(f"{i}. {task.strip()}")
    except FileNotFoundError:
        print("Empty list")

def main():
    if len(sys.argv) < 2:
        print("Usage: todolist <add/list> [task]")
        sys.exit(1)

    command = sys.argv[1]

    if command == "add":
        if len(sys.argv) < 3:
            print("Error: specify the task to add")
        else:
            add_task(" ".join(sys.argv[2:]))
    elif command == "list":
        list_tasks()
    else:
        print("Error: unrecognized command. Use 'add' or 'list'")

if __name__ == "__main__":
    main()
