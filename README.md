# Task Manager CLI
Source project: https://roadmap.sh/projects/task-tracker

Available commands:

  add        : Add a new task (taskName, description, status)
  update     : Update a task by ID (task_id, field, value)
  delete     : Delete a task by ID (task_id)
  list       : List all tasks

  filter     : Filter tasks

    Options:
      status <todo|inprogress|done>
      date   <dateAdded|dateUpdated> <DD/MM/YYYY>

    Examples:
      python cli.py filter status todo
      python cli.py filter date dateAdded 28/12/2025

Status values:
  todo | inprogress | done

Usage:

  python cli.py <command> [arguments]
  python cli.py --help | --h    # Display this help message

A simple Python command-line task manager that allows you to create, list, update, delete and filter tasks stored in a `tasks.json` file.

Each task contains:

* `task_id`
* `taskName`
* `description`
* `status`
* `dateAdded`
* `dateUpdated`

Status values are validated and must be one of:

```
todo | inprogress | done
```

---

## 📦 Installation

Clone the project and install Python dependencies (no external libs required).

```
git clone <repo>
cd task-manager-cli
```

Ensure you are using **Python 3.8+**.

---

## ▶️ How to Run

```
python cli.py <command> [arguments]
```

Display help:

```
python cli.py --help
python cli.py -h
```

---

## 🧩 Available Commands

### ✔ Add a Task

```
add <taskName> <description> <status>
```

Example:

```
python cli.py add "Buy groceries" "Milk and eggs" todo
```

The task will automatically receive:

* a UUID `task_id`
* `dateAdded`
* `dateUpdated`

Validation rules:

* `taskName` cannot be empty or only spaces
* `description` cannot be empty or only spaces
* `status` must be one of `todo | inprogress | done`

---

### 📋 List All Tasks

```
python cli.py list
```

If no tasks exist, an empty message is displayed.

---

### ✏ Update a Task

```
update <task_id> <field> <value>
```

Editable fields:

```
taskName
description
status
```

Protected fields (cannot be modified):

```
task_id
dateAdded
dateUpdated
```

Example:

```
python cli.py update 1234-uuid-5678 status done
```

The task automatically updates `dateUpdated`.

Status validation is enforced.

---

### ❌ Delete a Task

```
delete <task_id>
```

Example:

```
python cli.py delete 1234-uuid-5678
```

Deletes the matching task from `tasks.json`.

---

### 🔎 Filter Tasks

Filter by **status**:

```
python cli.py filter todo
```

If no tasks match, a message is displayed.

Planned enhancements include:

* filter by `dateAdded`
* filter by `dateUpdated`

---

## 🗂 Storage

Tasks are stored in:

```
tasks.json
```

Behavior:

1. If the file does not exist → an empty list is created
2. The first task is added and written to the file
3. On subsequent operations → tasks are loaded, updated, and rewritten

---

## 🧪 Input Validation

Validation rules are implemented in `utils.py`.

On task creation:

* `taskName` must not be empty
* `description` must not be empty
* `status` must be valid

On update:

* Protected fields cannot be modified
* `status` is re-validated
* Empty or whitespace-only values are rejected

Errors stop execution with a clear message.

---

## 🚀 Next Improvements (Suggestions)

Here are meaningful next steps you might consider:

* add colored CLI output
* support multi-word arguments without quotes
* implement filter by date
* add search by keyword
* add export to CSV
* add task priority
* add categories or tags

Tell me if you want help implementing any of these — especially date filtering or better UX 👍
