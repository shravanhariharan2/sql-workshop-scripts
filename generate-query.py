import random
import names

# students
majors = ["Computer Science", "Math-CS", "Computer Engineering", "Data Science", "CogSci"]
grad_years = [2022, 2023, 2024, 2025, 2026]

# courses
courses = ["CSE 12L", "CSE 13", "MATH 184", "CSE 100L", "CSE 143", "ECE 15L"]
titles = [
  "Reversing Linked Lists - Lab",
  "Mediocre Data Structures",
  "Statistics for Day Traders",
  "Reversing Doubly-Linked Lists - Lab",
  "Computer Architecture - A PC-Builder Perspective",
  "Binary - Lab"
]
professors = [
  "Larry Lillespie",
  "Cardi B",
  "Johnathan Ma",
  "some Google recruiter",
  "Linus Sebastian",
  "Ada Lovelace"
]
quarters_offered = ["Fall", "Winter", "Spring"]
years_offered = [2018, 2019, 2020, 2021, 2022, 2023]

create_table_students = "CREATE TABLE students (id SERIAL PRIMARY KEY, first_name VARCHAR(255), last_name VARCHAR(255), pid VARCHAR(10), major VARCHAR(255), graduation_year INTEGER);\n"
create_table_courses = "CREATE TABLE courses (id SERIAL PRIMARY KEY, code VARCHAR(255), title VARCHAR(255), professor VARCHAR(255), quarter_offered VARCHAR(10), year_offered INTEGER);\n"

query = ""

# build students insertions
for _ in range(1000):
  first_name = names.get_first_name()
  last_name = names.get_last_name()
  pid = "A" + str(random.randint(15000000, 17000000))
  major = random.choice(majors)
  grad_year = random.choice(grad_years)

  insert_into_students = "INSERT INTO students (first_name, last_name, pid, major, graduation_year) " 
  values = f"VALUES ('{first_name}', '{last_name}', '{pid}', '{major}', {grad_year});\n"

  query += (insert_into_students + values)

query += "\n\n\n"

# build courses insertions
for i in range(len(courses)):
  course = courses[i]
  title = titles[i]
  prof = professors[i]
  q_offered = random.choice(quarters_offered)
  y_offered = random.choice(years_offered)

  insert_into_courses = "INSERT INTO courses (code, title, professor, quarter_offered, year_offered) "
  values = f"VALUES ('{course}', '{title}', '{prof}', '{q_offered}', {y_offered});\n"

  query += (insert_into_courses + values)


print(query)