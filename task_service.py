import utils
import sys
import os
import json
import uuid
from datetime import datetime

def add_task(args):
    print("Add task called with args:", args)

    if len(args) < 3:
        print(f"Error: {3 - len(args)} parameter(s) missing. You must provide taskName, description, and status.")
        sys.exit(1)

    taskName = args[0]
    description = args[1]
    status = args[2]

    now = datetime.now().strftime("%d/%m/%Y")

    task_data = {
        "task_id": str(uuid.uuid4()),
        "taskName": taskName,
        "description": description,
        "status": status,
        "dateAdded": now,
        "dateUpdated": now
    }

    utils.validate_task(task_data)

    return task_data

def list_tasks(tasks):
    print("\n=== Task List ===")

    if len(tasks) == 0:
        print("No tasks found. The task list is empty.")
        return
    
    for task in tasks: 
        print(f""""task_id":{task["task_id"]},\n"taskName: {task["taskName"]},\n"description":{task["description"]},\n"status":{task["status"]},\n"dateAdded":{task["dateAdded"]},\n"dateUpdated":{task["dateUpdated"]}\n""")

def update_task(tasks,args):
    protected_fields = ["task_id", "dateAdded", "dateUpdated"]

    if args[1] in protected_fields:
        print("Error: You cannot update this field.")
        sys.exit(1)

    # if args[1] == "status":
    #     if args[2] 

    task_id = args[0]
    task_field = args[1]
    task_value = args[2]

    for index,task in enumerate(tasks):
        if task["task_id"] == task_id:
            task[task_field] = task_value
            utils.validate_update_task(tasks[index],task_field)

    task["dateUpdated"] = datetime.now().strftime("%d/%m/%Y")
    
    return tasks

def delete_task(tasks,args):
    for index,task in enumerate(tasks):
        if task["task_id"] == args[0]:
            tasks.pop(index)
    return tasks

def filter_task(tasks,args):
    for task in tasks:
        if task["status"] == args[0]:
            print(task)
            sys.exit(0)
            
    print(f"No task with status {args[0]} found")


