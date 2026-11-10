from pathlib import Path

Path("student_info.text").write_text(
    "Name:Tom\n"
    "Course: Introduction to Computer Science\n"
    "Favorite Programming Language: Python\n"
    "Current Semester: Fall 2026\n"
)
read_text = Path("student_info.text").read_text()
print(read_text)


