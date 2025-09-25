# Given list of tuples (name, surname, age, profession, City location)
# 1 - Add your new record o the beginning of the given list
# 2 - In modified list swap elements with indexes 1 and 5 (1<->5). Print result
# 3 - check that all people in modified list with records indexes 6, 10, 13
#   have age >=30. Print condition check result

people_records = [
  ('John', 'Doe', 28, 'Engineer', 'New York'),
  ('Alice', 'Smith', 35, 'Teacher', 'Los Angeles'),
  ('Bob', 'Johnson', 45, 'Doctor', 'Chicago'),
  ('Emily', 'Williams', 30, 'Artist', 'San Francisco'),
  ('Michael', 'Brown', 22, 'Student', 'Seattle'),
  ('Sophia', 'Davis', 40, 'Lawyer', 'Boston'),
  ('David', 'Miller', 33, 'Software Developer', 'Austin'),
  ('Olivia', 'Wilson', 27, 'Marketing Specialist', 'Denver'),
  ('Daniel', 'Taylor', 38, 'Architect', 'Portland'),
  ('Grace', 'Moore', 25, 'Graphic Designer', 'Miami'),
  ('Samuel', 'Jones', 50, 'Business Consultant', 'Atlanta'),
  ('Emma', 'Hall', 31, 'Chef', 'Dallas'),
  ('William', 'Clark', 29, 'Financial Analyst', 'Houston'),
  ('Ava', 'White', 42, 'Journalist', 'San Diego'),
  ('Ethan', 'Anderson', 36, 'Product Manager', 'Phoenix')
]

# Task 1
people_records.insert(0, ('Tony', 'Stark', 35, 'Iron Man', 'New York'))
print(f"Task 1: {people_records[0]}")

# Task 2
temp_tuple = people_records[1]
people_records.insert(1, people_records[5])
people_records.insert(5, temp_tuple)
print(f"Task 2: tuple from index 5 now under index 1 -> {people_records[1]}")
print(f"Task 2: tuple from index 1 now under index 5 -> {people_records[5]}")

#Task 3
people_older_than_30 = (people_records[6], people_records[10], people_records[13])
print(f"Task 3: tuple people_older_than_30 :\n{people_older_than_30}")
for person in people_older_than_30:
    if person[2] >= 30:
        print(f"{person[0]} is older than 30")
    else:
        print(f"{person[0]} is not older than she is {person[2]} years old")
