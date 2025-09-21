#ToDo List Application
class Task:
    def __init__(self, title, desc, due_date):
        self.title = title
        self.desc = desc
        self.due_date = due_date
        self.status = False  # False = incomplete, True = complete

    def mark_complete(self):
        self.status = True

    def __str__(self):
        return f"[{'✔' if self.status else '✘'}] {self.title} (Due: {self.due_date})"


class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def list_tasks(self):
        for t in self.tasks:
            print(t)

    def incomplete_tasks(self):
        for t in self.tasks:
            if not t.status:
                print(t)


# ---- CLI Simulation ----
todo = ToDoList()
todo.add_task(Task("Homework", "Math exercises", "2025-09-22"))
todo.add_task(Task("Shopping", "Buy milk", "2025-09-23"))

print("\nAll Tasks:")
todo.list_tasks()

print("\nIncomplete Tasks:")
todo.incomplete_tasks()

todo.tasks[0].mark_complete()
print("\nAfter marking complete:")
todo.list_tasks()


#Simple Blog System
class Post:
    def __init__(self, title, content, author):
        self.title = title
        self.content = content
        self.author = author

    def __str__(self):
        return f"{self.title} by {self.author}"


class Blog:
    def __init__(self):
        self.posts = []

    def add_post(self, post):
        self.posts.append(post)

    def list_posts(self):
        for p in self.posts:
            print(p)

    def posts_by_author(self, author):
        for p in self.posts:
            if p.author == author:
                print(p)

    def delete_post(self, title):
        self.posts = [p for p in self.posts if p.title != title]

    def edit_post(self, title, new_content):
        for p in self.posts:
            if p.title == title:
                p.content = new_content

    def latest_posts(self, n=3):
        for p in self.posts[-n:]:
            print(p)


# ---- CLI Simulation ----
blog = Blog()
blog.add_post(Post("First Post", "Hello world!", "Alice"))
blog.add_post(Post("Second Post", "Learning Python", "Bob"))
blog.add_post(Post("Third Post", "OOP Concepts", "Alice"))

print("\nAll Posts:")
blog.list_posts()

print("\nPosts by Alice:")
blog.posts_by_author("Alice")

print("\nLatest Posts:")
blog.latest_posts()


#Simple Banking System
class Account:
    def __init__(self, acc_no, name, balance=0):
        self.acc_no = acc_no
        self.name = name
        self.balance = balance

    def deposit(self, amt):
        self.balance += amt

    def withdraw(self, amt):
        if self.balance >= amt:
            self.balance -= amt
        else:
            print("Error: Insufficient funds")

    def __str__(self):
        return f"Account {self.acc_no} | {self.name} | Balance: {self.balance}"


class Bank:
    def __init__(self):
        self.accounts = {}

    def add_account(self, acc):
        self.accounts[acc.acc_no] = acc

    def check_balance(self, acc_no):
        acc = self.accounts.get(acc_no)
        return acc.balance if acc else "Account not found"

    def deposit(self, acc_no, amt):
        if acc_no in self.accounts:
            self.accounts[acc_no].deposit(amt)

    def withdraw(self, acc_no, amt):
        if acc_no in self.accounts:
            self.accounts[acc_no].withdraw(amt)

    def transfer(self, from_acc, to_acc, amt):
        if from_acc in self.accounts and to_acc in self.accounts:
            if self.accounts[from_acc].balance >= amt:
                self.accounts[from_acc].withdraw(amt)
                self.accounts[to_acc].deposit(amt)
            else:
                print("Error: Insufficient funds")


# ---- CLI Simulation ----
bank = Bank()
a1 = Account(101, "Alice", 500)
a2 = Account(102, "Bob", 300)
bank.add_account(a1)
bank.add_account(a2)

print("\nInitial Accounts:")
print(a1)
print(a2)

bank.deposit(101, 200)
bank.withdraw(102, 50)
bank.transfer(101, 102, 100)

print("\nAfter Transactions:")
print(a1)
print(a2)
