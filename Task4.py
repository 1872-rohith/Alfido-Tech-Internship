# Task - 4 Simple To-Do List
#!/usr/bin/env python3
"""
Simple To-Do List (CLI)
Features:
 - Add a task
 - Remove a task (by number)
 - View all tasks
 - Data persists in todo.json
"""

import json
import os
from datetime import datetime

DATA_FILE = "todo.json"


def load_tasks():
    if not os.path.exists(DATA_FILE):
        return []
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except (json.JSONDecodeError, IOError):
        return []


def save_tasks(tasks):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(tasks, f, indent=2, ensure_ascii=False)


def add_task(tasks):
    title = input("Task title: ").strip()
    if not title:
        print("No title entered — task not added.")
        return

    due = input("Due date (optional, YYYY-MM-DD) : ").strip()
    if due:
        try:
            # validate date format
            datetime.strptime(due, "%Y-%m-%d")
        except ValueError:
            print("Invalid date format. Saving without due date.")
            due = ""

    task = {
        "title": title,
        "due": due,
        "created_at": datetime.now().isoformat(timespec="seconds"),
    }
    tasks.append(task)
    save_tasks(tasks)
    print("Task added.")


def remove_task(tasks):
    if not tasks:
        print("No tasks to remove.")
        return

    view_tasks(tasks)
    try:
        idx = int(input("Enter task number to remove (0 to cancel): ").strip())
    except ValueError:
        print("Invalid input.")
        return

    if idx == 0:
        print("Canceling removal.")
        return

    if 1 <= idx <= len(tasks):
        removed = tasks.pop(idx - 1)
        save_tasks(tasks)
        print(f"Removed: {removed['title']}")
    else:
        print("Task number out of range.")


def view_tasks(tasks):
    if not tasks:
        print("\nNo tasks. Your to-do list is empty.\n")
        return
    print("\nYour To-Do List:")
    print("-" * 40)
    for i, t in enumerate(tasks, start=1):
        due = f" (due: {t['due']})" if t.get("due") else ""
        created = t.get("created_at", "")
        print(f"{i}. {t['title']}{due}\n    added: {created}")
    print("-" * 40 + "\n")


def main():
    tasks = load_tasks()

    MENU = (
        "\nChoose an option:\n"
        "1. Add task\n"
        "2. Remove task\n"
        "3. View tasks\n"
        "4. Exit\n"
        "Enter choice: "
    )

    while True:
        choice = input(MENU).strip()
        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            remove_task(tasks)
        elif choice == "3":
            view_tasks(tasks)
        elif choice == "4" or choice.lower() in ("q", "quit", "exit"):
            print("Goodbye — tasks saved.")
            break
        else:
            print("Invalid choice. Pick 1-4.")


if __name__ == "__main__":
    main()
