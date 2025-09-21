#Circle class
import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius**2

    def perimeter(self):
        return 2 * math.pi * self.radius


#Person Class
from datetime import date

class Person:
    def __init__(self, Sumaya, Tashkent, dob):
        self.name = Sumaya
        self.country = Tashkent
        self.dob = dob   # format: (year, month, day)

    def age(self):
        today = date.today()
        birth = date(*self.dob)
        return today.year - birth.year - ((today.month, today.day) < (birth.month, birth.day))


#Calculator Class
class Calculator:
    def add(self, a, b): return a + b
    def subtract(self, a, b): return a - b
    def multiply(self, a, b): return a * b
    def divide(self, a, b): 
        return a / b if b != 0 else "Error: Division by zero"


#Shape and Subclasses
import math

class Shape:
    def area(self): pass
    def perimeter(self): pass

class Circle(Shape):
    def __init__(self, r): self.r = r
    def area(self): return math.pi * self.r**2
    def perimeter(self): return 2 * math.pi * self.r

class Square(Shape):
    def __init__(self, s): self.s = s
    def area(self): return self.s**2
    def perimeter(self): return 4 * self.s

class Triangle(Shape):
    def __init__(self, a, b, c): self.a, self.b, self.c = a, b, c
    def perimeter(self): return self.a + self.b + self.c
    def area(self):
        s = self.perimeter() / 2
        return (s*(s-self.a)*(s-self.b)*(s-self.c))**0.5


#Binary search tree class
class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, root, key):
        if not root: return Node(key)
        if key < root.key:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)
        return root

    def search(self, root, key):
        if not root or root.key == key: return root
        return self.search(root.left, key) if key < root.key else self.search(root.right, key)



#Stack Data Structure
class Stack:
    def __init__(self):
        self.items = []

    def push(self, item): self.items.append(item)
    def pop(self): return self.items.pop() if self.items else "Stack Empty"



#Linked List Data Structure 
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new = Node(data)
        new.next = self.head
        self.head = new

    def delete(self, key):
        temp = self.head
        if temp and temp.data == key:
            self.head = temp.next
            return
        prev = None
        while temp and temp.data != key:
            prev, temp = temp, temp.next
        if temp: prev.next = temp.next

    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")


#Shopping cart class
class ShoppingCart:
    def __init__(self):
        self.items = {}

    def add_item(self, name, price):
        self.items[name] = self.items.get(name, 0) + price

    def remove_item(self, name):
        if name in self.items: del self.items[name]

    def total(self):
        return sum(self.items.values())



#Stack with display
class Stack:
    def __init__(self): self.items = []
    def push(self, item): self.items.append(item)
    def pop(self): return self.items.pop() if self.items else "Empty"
    def display(self): print(self.items)


#Queue Data Structure
class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item): self.items.append(item)
    def dequeue(self): return self.items.pop(0) if self.items else "Queue Empty"


#Bank class
class Bank:
    def __init__(self):
        self.accounts = {}

    def create_account(self, name, balance=0):
        self.accounts[name] = balance

    def deposit(self, name, amount):
        if name in self.accounts: self.accounts[name] += amount

    def withdraw(self, name, amount):
        if name in self.accounts and self.accounts[name] >= amount:
            self.accounts[name] -= amount

    def balance(self, name):
        return self.accounts.get(name, "No account found")
