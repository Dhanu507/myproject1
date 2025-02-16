"""
NAME
    Task and Habit Tracker

DESCRIPTION
    This program asks user to choose a option and propts the user to enter a values,
    where each option is a function in the program.

FUNCTIONS
    add_task() -> str
        appends the input values to the tasks list and returns a string.
    mark_task_completed() -> str
        checks for the input value in tasks, if found
        returns a string value with emoji and if not found returns error message.
    get_progress_summary() -> str
        generates a report of all tasks showing all details.
    save_task() -> None
        saves all the input values(tasks) to the mentioned csv file.
    load_task() -> None
        loads the data from the csv file into tasks list,
        if no value found returns a string to output as error message.
    delete_tasks -> str
        removes the mentioned task from the csv file.
        If not found returnd a error message.
"""

import csv
from datetime import datetime

def main() -> None:
    load_tasks()  # Load tasks from CSV when the program starts
    print("📅 Welcome to the Task and Habit Tracker! 📅")
    while True:
        print("\nPlease select the below options as per the need.")
        print("1. ➕ Add a task")
        print("2. ✅ Mark task as completed")
        print("3. 📊 View task progress summary")
        print("4. 🚮 Delete tasks")
        print("5. ❌ Quit")

        choice = input("Choose an option: ")
        if choice == "1":
            message = add_task()
            print(message)
        elif choice == "2":
            message = mark_task_completed()
            print(message)
        elif choice == "3":
            summary = get_progress_summary()
            print(summary)
        elif choice == "4":
            message = delete_tasks()
            print(message)
        elif choice == "5":
            save_tasks()
            print("🙏 Thanks for using Task and Habit Tracker 🙏. Have a nice day.")
            break
        else:
            print("⚠ Invalid option, please try again ⚠")

tasks = []

def add_task() -> str:
    task_name = input("Enter task name: ")
    frequency = input("Enter frequency (daily/weekly): ")

    while True:
        end_date = input("Enter end date (YYYY-MM-DD): ")
        try:
            end_date_valid = datetime.strptime(end_date, "%Y-%m-%d").date()
            break
        except ValueError:
            return "⚠ Invalid date format. Please enter date in YYYY-MM-DD format."

    task = {"task": task_name, "frequency": frequency, "end_date": end_date_valid, "completion_status": False}
    tasks.append(task)

    return (
        "\n✅ Task added successfully 👍\n"
        f"📌 Task: {task_name}\n"
        f"🔄 Frequency: {frequency.capitalize()}\n"
        f"📆 Deadline: {end_date_valid.strftime('%Y-%m-%d')}\n"
        + "~" * 50
    )

def mark_task_completed() -> str:
    task_name = input("Enter completed task: ")
    for task in tasks:
        if task["task"] == task_name:
            task["completion_status"] = True
            return f"\n ✅ Task: {task_name} completed. Congrats 🎉"
    return f"\n ❌ Task: {task_name} not found"

def get_progress_summary() -> str:
    if not tasks:
        return "No tasks found."

    summary_lines = []
    for task in tasks:
        status_emoji = "✅" if task["completion_status"] else "❌"
        status_words = "Completed" if task["completion_status"] else "Incomplete"
        summary_lines.append(
            f"📃 Task: {task['task']}\n"
            f"🔄 Frequency: {task['frequency'].capitalize()}\n"
            f"📆 Deadline: {task['end_date']}\n"
            f"📩 Status: {status_words} {status_emoji}\n" + "~" * 50
        )

    return "\n".join(summary_lines)

def save_tasks(filepath="tasks.csv") -> None:
    with open(filepath, "w", newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["task", "frequency", "end_date", "completion_status"])
        for task in tasks:
            writer.writerow([task["task"], task["frequency"], task["end_date"], task["completion_status"]])

def load_tasks(filepath="tasks.csv") -> None:
    global tasks
    try:
        with open(filepath, "r") as file:
            reader = csv.DictReader(file)
            tasks = [
                {
                    "task": row["task"],
                    "frequency": row["frequency"],
                    "end_date": datetime.strptime(row["end_date"], "%Y-%m-%d").date(),
                    "completion_status": row["completion_status"] == 'True'
                }
                for row in reader
            ]
    except FileNotFoundError:
        print("No previous task data found. Starting fresh!")

def delete_tasks() -> str:
    task_name = input("Enter the task name to delete: ")
    for task in tasks:
        if task["task"] == task_name:
            tasks.remove(task)
            return f"\n📃 Task: {task_name} has been deleted successfully 👍\n" + "~" * 50
    return f"\n❌ Task: {task_name} not found. Please enter a valid task\n" + "~" * 50

if __name__ == "__main__":
    main()
