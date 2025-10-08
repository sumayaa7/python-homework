import sqlite3

conn = sqlite3.connect("starfleet.db")
cur = conn.cursor()
cur.execute("""
CREATE TABLE IF NOT EXISTS Roster (
    Name TEXT,
    Species TEXT,
    Age INTEGER
)
""")
cur.executemany("INSERT INTO Roster VALUES (?, ?, ?)", [
    ("Benjamin Sisko", "Human", 40),
    ("Jadzia Dax", "Trill", 300),
    ("Kira Nerys", "Bajoran", 29)
])
cur.execute("UPDATE Roster SET Name = ? WHERE Name = ?", ("Ezri Dax", "Jadzia Dax"))

#showing Name and Age all Bajoran
cur.execute("SELECT Name, Age FROM Roster WHERE Species = 'Bajoran'")
rows = cur.fetchall()

print("Bajoran crew members:")
for row in rows:
    print(f"Name: {row[0]}, Age: {row[1]}")

conn.commit()
conn.close()
