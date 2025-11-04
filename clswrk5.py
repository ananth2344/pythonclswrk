python_students = {"Alice", "roy", "Clara"}
data_science_students = {"David", "Eva", "Clara"}

python_students.add("Frank")

data_science_students.remove("Eva")

both_courses = python_students.intersection(data_science_students)
print("Students in both courses:", both_courses)
only_python = python_students.difference(data_science_students)
print("Students only in Python:", only_python)

all_students = python_students.union(data_science_students)
print("All students (no duplicates):", all_students)

courses = {
    "Python": len(python_students),
    "Data Science": len(data_science_students)
}

for course, count in courses.items():
    print(f"Course: {course}, Students: {count}")

growth_projection = {course: count * 2 for course, count in courses.items()}
print("Expected growth:", growth_projection)

