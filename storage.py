import os
import json

def load_task():
    # If "tasks.json" exists, load the tasks into a Python list.
    # If it does not exist (first time running the app), start with an empty list.
    # When a new task is added:
    #   1. For the first task: an empty list is created, the task dictionary is appended, 
    #      and then saved into "tasks.json" as a list.
    #   2. For subsequent tasks: the existing list is loaded from "tasks.json",
    #      the new task is appended, and the full list is saved back to the file.
    if os.path.exists("tasks.json"):
        with open("tasks.json", "r") as file:
            tasks = json.load(file)
    else:
        tasks = []
    
    return tasks

def save_task(tasks, new_task):
    tasks.append(new_task)
    with open("tasks.json","w") as f:
        json.dump(tasks,f,indent=2)
    
    return tasks

def save_updated_task(tasks):
    with open("tasks.json","w") as f:
        json.dump(tasks,f,indent=2)
    
    return tasks
    