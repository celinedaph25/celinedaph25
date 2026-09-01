
# ===== Importing external modules ===========
'''This is the section where you will import modules'''

from datetime import datetime

# ==== Class Object ====


class Task:
    def __init__(self, assigned, task, desc, date, due, complete):
        self.assigned = assigned
        self.task = task
        self.desc = desc
        self.date = date
        self.due = due
        self.complete = complete

    def __str__(self):
        return (f'''
        {"__" * 30}
        Task Title: \t\t{self.task}
        Assigned to: \t\t{self.assigned}
        Date assigned: \t\t{self.date}
        Due date: \t\t{self.due}
        Task Complete? \t\t{self.complete}
        Task description: \t{self.desc}''')

# ==== Login Section ====


accounts = []

with open('user.txt', 'r+') as file:
    '''read file'''
    for line in file:
        list = line.strip().split(', ')
        accounts.append(list)
        '''strip and split strings append into list'''


def load_user():
    with open('user.txt', 'r') as file:
        user_data = file.read().split("\n")
    username_password = {}

    for user in user_data:
        if user:
            username, password = user.split(", ")
            username_password[username] = password
    return username_password


def reg_user():
    user_pass = load_user()
    username = input("Enter a new username: ")

    if username in user_pass:
        print("Username exists")
        return

    password = input("Enter password: ")
    confirm = input("Re-enter password: ")

    if password == confirm:
        user_pass[username] = password
        print("New user added successfully\n")
        with open("user.txt", "w+") as file:
            names = []
            for k in user_pass:
                names.append(f"{k}, {user_pass[k]}")
            file.write("\n".join(names))
    else:
        print("Passwords do not match")


tasks = []


def read_file():
    tasks.clear()
    with open('tasks.txt', 'r') as file:
        '''read file'''
        for line in file:
            each = line.strip().split(', ')
            assigned = each[0]
            task = each[1]
            desc = each[2]
            date = each[3]
            due = each[4]
            complete = each[5]

            work = Task(assigned, task, desc, date, due, complete)

            tasks.append(work)
            '''strip and split strings append into list'''


def add_task():
    with open('tasks.txt', 'a+') as file:
        '''ammend file with a new task'''
        task_user = input("Enter username assigned to task: ")
        title = input("Enter task title: ")
        desc = input("Enter task description: ")

        print("Enter task due date below... ")
        day = input("Date (DD): ")
        month = input("Month (Mo): ").title()
        year = input("Year (YYYY): ")
        new_due = (f"{day} {month} {year}")

        complete = "No"
        current = datetime.now()
        '''find current date/time'''

        date_month_year = current.strftime("%d %b %Y")
        '''format to existing format'''

        file.write(f"\n{task_user}, {title}, {desc}, {date_month_year}, {new_due}, {complete}")
        '''add similar format to file'''

        print("Task added. \n")
        '''notification for success'''


def view_all():
    read_file()
    for row in tasks:
        print(row)
    print("\n")


my_tasks = []
other_tasks = []


def view_mine():
    number = 0
    found = False
    for sublist in tasks:
        if login_user in sublist.assigned:
            '''check if username exists in document'''
            number += 1
            print(f"#{number}: {sublist.task}")
            my_tasks.append(sublist)
            found = True
        else:
            other_tasks.append(sublist)

    if found:
        update_task()
    if not found:
        print(f'No assigned task for {login_user}')


def update_task():
    update = int(input('\nUpdate task by indicating task number, or enter 0 for main menu: '))

    if 0 < update <= len(my_tasks):
        update -= 1
        for number, sublist in enumerate(my_tasks):
            if number == update:
                change = int(input('''
                    #1 - Mark as complete
                    #2 - Edit Task
                    : '''))
                if change == 1:
                    sublist.complete = "Yes"
                elif change == 2:
                    if sublist.complete == "No":
                        option = int(input('''Choose one:
                        1 - Change user only
                        2 - Change due date
                        3 - Change both
                        :'''))
                        if option == 1:
                            new_assign = input("Who is the task assigned to? ")
                            sublist.assigned = new_assign
                        elif option == 2:
                            print("Enter task due date below... ")
                            day = input("Date (DD): ")
                            month = input("Month (Mo): ").title()
                            year = input("Year (YYYY): ")
                            new_due = (f"{day} {month} {year}")
                            sublist.due = new_due
                        elif option == 3:
                            new_assign = input("Who is the task assigned to? ")
                            sublist.assigned = new_assign
                            print("Enter task due date below... ")
                            day = input("Date (DD): ")
                            month = input("Month (Mo): ").title()
                            year = input("Year (YYYY): ")
                            new_due = (f"{day} {month} {year}")
                            sublist.due = new_due
                        else:
                            print("Invalid entry")
                    else:
                        print("All tasks are complete.")
                else:
                    print("Invalid entry")

        tasks.clear()
        tasks.extend(my_tasks)
        tasks.extend(other_tasks)

        with open('tasks.txt', 'w+') as file:
            for task in tasks:
                file.write(f"{task.assigned}, {task.task}, {task.desc}, {task.date}, {task.due}, {task.complete}\n")

    elif update == 0:
        my_tasks.clear()
        other_tasks.clear()
        return
    
    else:
        print("Invalid entry")

    print("Task updated\n")


def view_completed():
    try:
        for index in tasks:
            '''assign each section of line'''
            if "yes" in index.complete.lower():
                print(index)
            else:
                print("No complete tasks")
    except ValueError:
        print("Unable to identify")
    print("\n")


def delete_task():
    if login_user == 'admin':
        list = 0

        if list <= len(tasks):
            print("\nTasks available")
            for index in tasks:
                task = index.task
                '''look for task names only'''
                list += 1
                print(f"\t{list} - Task: {task}")
        else:
            print("No task available")

        select = int(input('''\nWhich task number do you want to delete? '''))

        if 0 < select <= list:
            select -= 1
            del tasks[select]

            with open('tasks.txt', 'w+') as file:
                for i, task in enumerate(tasks):
                    if i > 0:
                        file.write("\n")
                    file.write(f"{task.assigned}, {task.task}, {task.desc}, {task.date}, {task.due}, {task.complete}")

            print("Task deleted\n")

        else:
            print("The number does not exist\n")
    else:
        print("You have entered an invalid input. Please try again\n")


def task_stats():
    comp = 0
    incomp = 0
    late = 0
    current = datetime.now()
    '''for format and counting'''

    for index in tasks:
        if index.complete == "Yes":
            comp += 1
        elif index.complete == "No":
            incomp += 1
            due_object = datetime.strptime(index.due, "%d %b %Y")
            if due_object < current:
                late += 1

    perc_incomp = round(incomp / len(tasks) * 100)
    if incomp != 0:
        perc_late = round(late / incomp * 100)
    else:
        perc_late = 0
    '''calculate percentages for each user'''

    try:
        with open('task_overview.txt', 'w') as file:
            file.write(f'''**Task Report**
    Complete tasks: {comp}
    Incomplete tasks: {incomp}
    Past due tasks: {late}
    Percent of incomplete tasks: {perc_incomp}%
    Percent of overdue tasks: {perc_late}%''')
    except Exception:
        print("An error has occured.")


def user_stats():
    users = {}
    for names in tasks:
        user = names.assigned
        if user in users:
            users[user] += 1
        else:
            users[user] = 1
        '''Count tasks per user'''

    user_names = {names.assigned for names in tasks}
    total_users = len(user_names)
    total_tasks = len(tasks)
    '''count total tasks and total users'''

    try:
        with open('user_overview.txt', 'w') as file:
            file.write(f'''
{"__" * 30}
**User Report**
Total users: {total_users}
Total tasks: {total_tasks}\n''')
    except Exception:
        print("An error has occured")

    for user in users:
        comp = 0
        incomp = 0
        late = 0
        current = datetime.now()
        '''for format and counting'''

        for index in tasks:
            if index.complete == "Yes" and index.assigned == user:
                comp += 1
            elif index.complete == "No" and index.assigned == user:
                incomp += 1
                due_object = datetime.strptime(index.due, "%d %b %Y")
                if due_object < current:
                    late += 1
        '''count each occurence'''

        total_per_user = round((users[user]) / total_tasks * 100)
        '''percent of tasks per user'''

        perc_comp = round(comp / users[user] * 100)
        perc_incomp = round(incomp / users[user] * 100)
        if incomp != 0:
            perc_late = round(late / incomp * 100)
        else:
            perc_late = 0

        try:
            with open('user_overview.txt', 'a+') as file:
                file.write(f'''
    {"__" * 30}
    {user} has {users[user]} tasks
    Percent of tasks for {user} is {total_per_user}%
    Complete: {perc_comp}%
    Incomplete: {perc_incomp}%
    Late: {perc_late}%
                    ''')
        except Exception:
            print("An error has occured")


def gen_reports():
    try:
        task_stats()
        user_stats()
        print("Reports created\n")
        '''create reports'''
    except Exception:
        print("Unable to create reports")


def display_stats():
    gen_reports()
    task_report = []
    try:
        with open('task_overview.txt', 'r') as file:
            for line in file:
                each = line.strip().split(',')
                task_report.append(each)
    except FileNotFoundError:
        print("File does not exist")
    '''read text file if/once made'''
    print("\n")
    for line in task_report:
        print(*line)

    user_stats()
    user_report = []
    try:
        with open('user_overview.txt', 'r') as file:
            for line in file:
                each = line.strip().split(',')
                user_report.append(each)
    except FileNotFoundError:
        print("File does not exist")
    '''read text file if/once made'''
    for line in user_report:
        print(*line)


read_file()


login = False
while not login:
    login_user = input("Enter username: ")
    '''request username'''
    login_pass = input("Enter password: ")
    '''request password'''
    try:
        for username, password in accounts:
            if login_user == username and login_pass == password:
                '''check if valid username and password'''
                login = True
                '''break if true'''
                break
        else:
            print("Username and/or Password incorrect")
    except SyntaxError:
        print("Invalid entry")

if login:
    print("Logging in...\n")
    '''notifies if valid username/password'''

while True:
    '''Present the menu to the user and'''
    '''make sure that the user input is converted to lower case.'''

    if login_user == 'admin':
        '''admin menu'''
        menu = input('''Select one of the following options:
    r - register a user
    a - add task
    va - view all tasks
    vm - view my tasks
    vc - view completed tasks
    del - delete tasks
    ds - display statistics
    gr - generate reports

    e - exit
    : ''').lower()
    else:
        '''non-admin menu'''
        menu = input('''Select one of the following options:
    a - add task
    va - view all tasks
    vm - view my tasks
    e - exit
    : ''').lower()

    try:
        if menu == 'r':
            if login_user == 'admin':
                reg_user()
        elif menu == 'a':
            add_task()
        elif menu == 'va':
            view_all()
        elif menu == 'vm':
            view_mine()
        elif menu == 'vc':
            if login_user == 'admin':
                view_completed()
        elif menu == 'del':
            if login_user == 'admin':
                delete_task()
        elif menu == 'ds':
            if login_user == 'admin':
                display_stats()
        elif menu == 'gr':
            if login_user == 'admin':
                gen_reports()
        elif menu == 'e':
            print('Goodbye!!!')
            break
    except SyntaxError:
        print("Invalid input. Please try again.\n")
