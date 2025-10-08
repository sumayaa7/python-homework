#Task1

import json

# Read JSON file
with open("students.json", "r") as f:
    data = json.load(f)

# Print each student's details
for student in data["students"]:
    print("Name:", student["name"])
    print("Age:", student["age"])
    print("Grade:", student["grade"])
    print("-" * 20)

#Task2

import requests

API_KEY = "9e8331644eab4cd57885d54dd137276a"
city = "Tashkent"

url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

response = requests.get(url)
data = response.json()  

if response.status_code == 200:
    data = response.json()
    print("City:", data["name"])
    print("Temperature:", data["main"]["temp"], "°C")
    print("Humidity:", data["main"]["humidity"], "%")
    print("Weather:", data["weather"][0]["description"])
else:
    print("Error:", response.status_code, response.text)


#Task3

import json
import os

filename = "books.json"

#checks if there any file or no, if no than creates
if not os.path.exists(filename) or os.path.getsize(filename) == 0:
    default_books = [
        {"title": "Python Basics", "author": "John Smith", "year": "2021"},
        {"title": "AI for Beginners", "author": "Sara Lee", "year": "2022"},
        {"title": "Data Science 101", "author": "Ali Karimov", "year": "2023"}
    ]
    with open(filename, "w") as f:
        json.dump(default_books, f, indent=4)
    print("Created new books.json with default data.")

#reads correctly
with open(filename, "r") as f:
    books = json.load(f)

print("Books loaded successfully!")
for book in books:
    print(f"{book['title']} by {book['author']} ({book['year']})")

#Task4

import requests
import random

API_KEY = "695a876c"  
genre = input("Enter movie genre: ")

url = f"http://www.omdbapi.com/?apikey={API_KEY}&s={genre}&type=movie"
response = requests.get(url)
data = response.json()

if "Search" in data:
    movie = random.choice(data["Search"])
    print("Title:", movie["Title"])
    print("Year:", movie["Year"])
    print("IMDB ID:", movie["imdbID"])
else:
    print("No movies found for this genre.")
