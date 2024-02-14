# Bryan Bibb, CPT187-W12, Feb 4, 2024
# Program:  Task List
# Purpose:  Keeps a list of tasks in two tasklists, Personal and Business. User
#           can view tasks in either list, add and delete tasks, and mark tasks complete.

from objects import dataclass
import csv

## -----------------------objects tier------------------------------##

# Task class creates object for each task
@dataclass
# attributes for the name of the task and its state
class Task:
    description:str = ""
    __state:str = "open"

# methods to set and get the state, which will be open, complete, or deleted
    def set_state(self, state):
        self.__state = state
    def get_state(self):
        return self.__state

# Tasklist class creates objects for a list of tasks
@dataclass
class Tasklist:
    description:str = ""

# post_init statement to create the list that is the primary data in the object
    def __post_init__(self):
        self.__tasks = []

# methods to add, list, and delete tasks from the list
    def add_task(self, task):
        self.__tasks.append(task)

    def get_task(self, number):
        # the 'number' will be from 1, so subtraction is necessary for 0 index
        index = number - 1
        return self.__tasks[index]

    def delete_task(self, task):
        self.__tasks.remove(task)

# method to make this object iterable
    def __iter__(self):
        for task in self.__tasks:
            # each task becomes one row in the list of lists
            yield task

# the count property is used to tell if the list is empty
    @property
    def count(self):
        return len(self.__tasks)

## -----------------------business tier------------------------------##
# take the tasks in the object and write them to a list of lists.
def write_tasklist(tasklist, name):
    rows = []
    for task in tasklist:
        row = []
        row.append(task.description)
        row.append(task.get_state())
        rows.append(row)
# write that list of lists to a CSV file
    filename = "task_list_" + name.lower() + '.csv'
    with open(filename, "w", newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(rows)

# load the values in the CSV file and create an object with them
def load_tasklist(name):
    # the name for the two lists comes from the list selection dialogue
    filename = "task_list_" + name.lower() + '.csv'
    selected_list = Tasklist(name)
    # read the file and write the data to the object just created
    with open(filename, newline='') as csvfile:
        reader = csv.reader(csvfile)
        # read each row and create a task for each
        for row in reader:
            task = Task(row[0])
            # add each task to the selected tasklist
            selected_list.add_task(task)
    return selected_list

# command menu
def print_menu():
    print("COMMAND MENU")
    print("1. choose            - Choose a tasklist")
    print("2. list open         - List open tasks")
    print("3. list completed    - list completed tasks")
    print("4. add               - Add a task")
    print("5. complete          - Complete a task")
    print("6. delete            - Delete a task")
    print("7. exit              - Exit the program")
    print()

# list the tasks in the selected tasklist object
def list_tasks(selected_list):
    # indicate if that list is empty
    if selected_list.count == 0:
        print("No tasks")
    else:
        # print each open task, one per line, enumerated
        print(f"Open tasks for {selected_list.description}:")
        print()
        for i, task in enumerate(selected_list, start=1):
            if task.get_state() == "open":
                print(f"{i}. {task.description}")

# same structure as list_tasks, but checking for completed tasks
def list_completed(selected_list):
     if selected_list.count == 0:
         print("No tasks")
     else:
         print(f"Completed tasks for {selected_list.description}:")
         print()
         for i, task in enumerate(selected_list, start=1):
             if task.get_state() == "complete":
                 print(f"{i}. {task.description}")

# add a task to the selected tasklist
def add_task(selected_list):
    # user input of task's content
    description = input("Description: ")
    # create new task object with that description and add to the list object
    new_task = Task()
    new_task.description = description
    selected_list.add_task(new_task)
    list_tasks(selected_list)

# mark tasks as completed or deleted
def change_state(selected_list, task, state):
    if state == 0:
        print(f"Task '" + selected_list.get_task(task).description + "' has been deleted.")
        removed = selected_list.get_task(task)
        # change state in the task object and remove from the tasklist
        removed.set_state("deleted")
        selected_list.delete_task(removed)

    if state == 2:
        print(f"Task '" + selected_list.get_task(task).description + "' has been completed.")
        removed = selected_list.get_task(task)
        # change state to complete
        removed.set_state("complete")
        # this remove/add sequence moves the completed task to the bottom of the list,
        # which helps with the enumeration step in list_tasks
        selected_list.delete_task(removed)
        selected_list.add_task(removed)

## -----------------------presentation tier------------------------------##

def main():
    print("-------------------------------------------------------------")
    print("Welcome to the Task List Manager Program! ")
    print("-------------------------------------------------------------")
    print()
    print("First, choose a list to view and edit.")
    print()
    print_menu()

#initialize tasklists and set a default starting list
    business = load_tasklist("business")
    personal = load_tasklist("personal")
    business.description = "Business List"
    personal.description = "Personal List"
    selected_list = personal
    listname = "personal"

# loop to accept user choice of commands
    while True:
        command_choice = int(input("Command: "))
        # two lists are hard coded in this version of the program
        if command_choice == 1:  # change task list
            print("1. Business")
            print("2. Personal")
            choice = input("Choose a list number to select: ")
            # based on the list selected, set variables for the list and name
            if choice == "1":
                selected_list = business
                listname = "business"
            elif choice == "2":
                selected_list = personal
                listname = "personal"
            print(f"Selected list: {selected_list.description}")
            print()
            print_menu()
        elif command_choice == 2:  # list tasks
            list_tasks(selected_list)
        elif command_choice == 3:  # list completed tasks
            list_completed(selected_list)
        elif command_choice == 4:  # add a task
             add_task(selected_list)
        elif command_choice == 5:  # complete a task
            # a fresh list of tasks enables user input of which task to complete
            list_tasks(selected_list)
            task_to_complete = int(input("Select a task number to complete: "))
            change_state(selected_list, task_to_complete, 2)
        elif command_choice == 6:  # delete a task
            # a fresh list of tasks enables user input of which task to delete
            list_tasks(selected_list)
            task_to_delete = int(input("Select a task number to delete: "))
            change_state(selected_list, task_to_delete, 0)
        elif command_choice == 7:
            # write the current state of the list to the CSV file
            write_tasklist(selected_list, listname)
            print("Goodbye.")
            # ends the program
            break
        # error message if selection is out of bounds
        else:
            print("Invalid command. Try again")

main()