def delete_line(filename, line_number):
    with open(filename, 'r') as file:
        lines = file.readlines()
    if 0 < line_number <= len(lines):
        del lines[line_number - 1]
    with open(filename, 'w') as file:
        file.writelines(lines)


def write_task(file, task):
    with open(file, "a") as f:
        f.write(task + "\n")

def read_tasks(filename):
    try: 
        with open(filename, 'r') as f:
            tasks = f.readlines()
        if not tasks:
            return 
        else:
            return tasks
    except FileNotFoundError:
        print("Empty list")