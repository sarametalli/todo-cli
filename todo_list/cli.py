#!/usr/bin/env python3

import sys
from .utils import delete_line, write_task

TODO_FILE = "todo_list/tasks.txt"
COMPLETED_FILE = "todo_list/completed.txt"


def add_task(task):
    write_task(TODO_FILE, task)
    print(f"Added task: {task}")


def check_task(task_number):
    try:
        with open(TODO_FILE, "r") as f:
            tasks = f.readlines()
            if 0 < task_number <= len(tasks):
                write_task(COMPLETED_FILE, tasks[task_number - 1].strip())
                delete_line(TODO_FILE, task_number - 1)
    except Exception as e:
        print(f"Error: {e}")


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
    elif command == "check":
        if len(sys.argv) < 3:
            print("Error: specify the task number to mark as done")
        else:
            check_task(int(sys.argv[2]))
    else:
        print("Error: unrecognized command. Use 'add' or 'list'")
        
if __name__ == "__main__":
    main()
