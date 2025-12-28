import sys

def validate_task(task_data):
    valid_statuses = ["todo","inprogress","done"]

    if not task_data["taskName"] or not task_data["taskName"].strip():
        print("Invalid value: task_name cannot be empty or only spaces")
        sys.exit(1)

    if not task_data["description"] or not task_data["description"].strip():
        print("Invalid value: description cannot be empty or only spaces")
        sys.exit(1)

    if task_data["status"] not in valid_statuses:
        print(f"Invalid status: must be one of {', '.join(valid_statuses)}")
        sys.exit(1)

    return

def validate_update_task(task_data, task_field):
    valid_statuses = ["todo","inprogress","done"]
    if task_field == "status":
        if task_data[task_field] not in valid_statuses:
            print(f"Invalid status: must be one of {', '.join(valid_statuses)}")
            sys.exit(1)
        if not task_data[task_field] or not task_data[task_field].strip():
            print(f"Invalid value: {task_field} cannot be empty or only spaces")
            sys.exit(1)

