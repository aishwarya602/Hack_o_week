import re

def extract_entities(query):

    query = query.lower()

    # -----------------------------
    # Extract Semester
    # -----------------------------
    semester_pattern = r"(sem|semester)\s*(\d+)"
    semester_match = re.search(semester_pattern, query)
    semester = semester_match.group(2) if semester_match else None

    # -----------------------------
    # Extract Course Code (e.g., CS101, MA202)
    # -----------------------------
    course_pattern = r"\b[A-Z]{2,4}\d{0,3}\b"
    course_match = re.search(course_pattern, query.upper())
    course = course_match.group() if course_match else None

    # -----------------------------
    # Extract Date (simple formats)
    # -----------------------------
    date_pattern = r"\b\d{1,2}\s*(jan|feb|mar|apr|may|jun|jul|aug|sep|oct|nov|dec|january|february|march|april|june|july|august|september|october|november|december)\b"
    date_match = re.search(date_pattern, query)
    date = date_match.group() if date_match else None

    return semester, course, date


# -----------------------------
# Interactive Loop
# -----------------------------

print("Student Query Entity Extraction System")
print("Type 'exit' to quit.\n")

while True:
    user_input = input("Enter your query: ")

    if user_input.lower() == "exit":
        print("Goodbye!")
        break

    semester, course, date = extract_entities(user_input)

    print("\nExtracted Entities:")
    print("Semester:", semester)
    print("Course:", course)
    print("Date:", date)
    print()
