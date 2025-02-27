# Task and Habit Tracker

## Video Demo: <https://youtu.be/B6JI9eELF0c>

## My Introduction

My name is Dhanush Gowda and I am from Bengaluru, India. I am an under graduate of mechanical engineering, now working  in an mechanical company and learning Python on self interest.

## Description

My project is a tracker app where user can track the tasks or habits or any information provided. The feature of the program inculdes adding a task, updating status of the tasks, viewing the progress of task, deleting task after completion and last quiting from the program. Please see the video link above for a full demo of the program.

Project Structure:

    -project.py
    -tasks.csv
    -test_project.py
    -requirements.txt
    -README.md

## Libraries

### CSV

 The so-called CSV (Comma Separated Values) format is the most common import and..[(Read more)](<https://docs.python.org/3/library/csv.html>)

### datetime

 The datetime module supplies classes for manipulating dates and times...[(Read more)](<https://docs.python.org/3/library/datetime.html>)

### pytest

 The pytest framework makes it easy to write small, readable tests, and..[(Read more)](<https://docs.pytest.org/en/stable/>)

## Installing libraries

there is a a requirements.txt file that has all the libraries used.

and simply can be installed by the mentioned pip command:

    pip install -r requirements.txt

## Usage

Run the mentioned command in terminal

        python project.py

📅 Welcome to the Task and Habit Tracker! 📅

        Please select the below options as per the need.
        1. ➕ Add a task
        2. ✅ Mark task as completed
        3. 📊 View task progress summary
        4. 🚮 Delete tasks
        5. ❌ Quit
        Choose an option

here user is prompted to choose any option from the listed options to quit the program can choose 5th option

        Choose an option: 1
        Enter task name: coding
        Enter frequency (daily/weekly): daily
        Enter end date (YYYY-MM-DD): 2024-11-5

        ✅ Task added successfully 👍
        📌 Task: coding
        🔄 Frequency: Daily
        📆 Deadline: 2024-11-05
        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

after entering the values user will be again prompted for values to exit or continue.

    Please select the below options as per the need.
        1. ➕ Add a task
        2. ✅ Mark task as completed
        3. 📊 View task progress summary
        4. 🚮 Delete tasks
        5. ❌ Quit
        Choose an option

## Functions

there are total 7 functions including main() function in the project.py

## add_task()

the user input value after selecting option 1 is appended to the tasks list if only the input of date is in mentioned formart else returns a error warning message and prompts again for value.

## mark_task_completed()

when user choose option 2 checks for the input value in file/data, if found returns a string value with emoji and if not found returns error message and propmts user for value again

## get_progress_summary()

when user choose option 3 generates a report of all tasks showing all details if data/task exist in the file else returns a error message and prompts user for a value.

## save_task()

saves all the input values(tasks) to the mentioned csv file if all condition satisfied.

## load_task()

loads the data from the csv file into tasks list,
if no value found returns a string to output as error message

## delete_tasks

when user choose option 4 prompts user for a value(task) and removes the mentioned task from the csv file.If not found returns a error message.

## main()

loads the data if present in the mentioned csv file and asks the user for input values according to the option selected performs the particular selection options function and prints the data. If user choose option 5 it prints a thankyou message by quitting the program.
