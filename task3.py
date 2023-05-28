import sqlite3

def generate_report():
    # Connect to the database
    conn = sqlite3.connect("student_marks.db")
    cursor = conn.cursor()

    # Execute a query to retrieve students with scores > 60
    query = "SELECT * FROM student_marks WHERE score > 60"
    cursor.execute(query)
    students = cursor.fetchall()

    # Close the database connection
    conn.close()

    # Display the report
    print("Students with scores > 60:")
    for student in students:
        print("Name:", student[0], student[1])
        print("Grade:", student[2])
        print("Subject:", student[3])
        print("Score:", student[4])
        print("----------------------")

# Call the generate_report function to generate the report
generate_report()
