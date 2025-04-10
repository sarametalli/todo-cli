#!/usr/bin/env python3

import sys
from .manage_tasks import add_task, list_tasks, check_task, read_completed_tasks

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
    elif command == "completed":
        read_completed_tasks()
    else:
        print("Error: unrecognized command. Use 'add', 'list' or 'check'")
        
if __name__ == "__main__":
    main()
