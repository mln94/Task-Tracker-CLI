import sys
import task_service
import storage


def start_args():
    expected_arguments = ["add","update","delete","list","filter"]

    print("type --help or -h for available command")

    if len(sys.argv) > 1 and sys.argv[1] in ["--help","-h"]:
        print("""
            Available commands:
            add      : Add a new task (taskName, description, status)
            update   : Update a task by ID (task_id, field, value)
            delete   : Delete a task by ID (task_id)
            list     : List all tasks
            filter   : Filter tasks  
             Options:
               status <todo|inprogress|done>
               date   <dateAdded|dateUpdated> <DD/MM/YYYY>
            filter   : Filter tasks by status or date
              
            Status values:
                todo | inprogress | done

            Usage:
            
            python cli.py <command> [arguments]
            python cli.py --help | --h  # display this message
        """)
        sys.exit(1)

    print(len(sys.argv))
    if len(sys.argv) < 2:
        print("Command is missing")
        sys.exit(1)

    if len(sys.argv) > 5:
        print("Too much commands")
        sys.exit(1)

    user_command = sys.argv[1]
    user_args = sys.argv[2:]

    if not user_command in expected_arguments:
        print(f"Unknown command: {user_command}")
        print(f"Available commands: {', '.join(expected_arguments)}")
        sys.exit(1)
    return user_command, user_args

def main():
    command,args = start_args()
    
    if command == "add":
        new_task = task_service.add_task(args)
        tasks = storage.load_task()
        save_tasks = storage.save_task(tasks,new_task)

        print("Task added successfully.")
        
        sys.exit(0)
    
    if command == "list":
        tasks = storage.load_task()
        task_service.list_tasks(tasks)

    if command == "update":
        tasks = storage.load_task()
        updated_tasks = task_service.update_task(tasks,args)
        save_updated_tasks = storage.save_updated_task(updated_tasks)
    
    if command == "delete":
        tasks = storage.load_task()
        deleted_tasks = task_service.delete_task(tasks, args)
        save_delete_tasks = storage.save_updated_task(deleted_tasks)
    
    if command == "filter":
        tasks = storage.load_task()
        task_service.filter_task(tasks, args)


if __name__ == "__main__":
    main()