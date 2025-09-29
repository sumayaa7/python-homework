from datetime import datetime, timedelta
import time
import re
import phonenumbers
from zoneinfo import ZoneInfo

# 1. Age Calculator
birthdate_str = input("Enter your birthdate (YYYY-MM-DD): ")
birthdate = datetime.strptime(birthdate_str, "%Y-%m-%d")
today = datetime.today()
age_years = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
age_months = (today.month - birthdate.month) % 12
age_days = (today - birthdate.replace(year=today.year)).days if today.month >= birthdate.month else (today - birthdate.replace(year=today.year-1)).days
print(f"Your age: {age_years} years, {age_months} months, {age_days} days")

# 2. Days Until Next Birthday
next_birthday = birthdate.replace(year=today.year)
if next_birthday < today:
    next_birthday = next_birthday.replace(year=today.year + 1)
days_remaining = (next_birthday - today).days
print(f"Days until next birthday: {days_remaining}")

# 3. Meeting Scheduler
current_str = input("Enter current date and time (YYYY-MM-DD HH:MM): ")
current_dt = datetime.strptime(current_str, "%Y-%m-%d %H:%M")
hours = int(input("Enter meeting duration hours: "))
minutes = int(input("Enter meeting duration minutes: "))
end_time = current_dt + timedelta(hours=hours, minutes=minutes)
print("Meeting ends at:", end_time)

# 4. Timezone Converter
date_str = input("Enter date and time (YYYY-MM-DD HH:MM): ")
from_zone = input("Enter your current timezone (e.g. Asia/Tashkent): ")
to_zone = input("Enter target timezone: ")
dt = datetime.strptime(date_str, "%Y-%m-%d %H:%M")
dt = dt.replace(tzinfo=ZoneInfo(from_zone))
converted = dt.astimezone(ZoneInfo(to_zone))
print("Converted time:", converted)

# 5. Countdown Timer
future_str = input("Enter future date and time (YYYY-MM-DD HH:MM:SS): ")
future_dt = datetime.strptime(future_str, "%Y-%m-%d %H:%M:%S")
print("Countdown started...")
while True:
    now = datetime.now()
    remaining = future_dt - now
    if remaining.total_seconds() <= 0:
        print("Time's up!")
        break
    print("Time remaining:", remaining)
    time.sleep(1)

# 6. Email Validator
email = input("Enter email: ")
pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
if re.match(pattern, email):
    print("Valid email")
else:
    print("Invalid email")

# 7. Phone Number Formatter
number = input("Enter phone number: ")
parsed = phonenumbers.parse(number, "US")
print("Formatted number:", phonenumbers.format_number(parsed, phonenumbers.PhoneNumberFormat.NATIONAL))

# 8. Password Strength Checker
password = input("Enter password: ")
if (len(password) >= 8 and
    any(c.islower() for c in password) and
    any(c.isupper() for c in password) and
    any(c.isdigit() for c in password)):
    print("Strong password")
else:
    print("Weak password")

# 9. Word Finder
sample_text = "Python is fun. Python is powerful. I like Python."
word = input("Enter word to find: ")
indices = [m.start() for m in re.finditer(word, sample_text)]
print(f"Occurrences of '{word}': {indices}")

# 10. Date Extractor
text = input("Enter text with dates (e.g. 2025-09-29 or 29/09/2025): ")
date_pattern = r"\b\d{4}-\d{2}-\d{2}\b|\b\d{2}/\d{2}/\d{4}\b"
dates = re.findall(date_pattern, text)
print("Dates found:", dates)
