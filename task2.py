import tkinter as tk
from tkinter import ttk

def add_student():
    # Retrieve input values
    first_name = entry_first_name.get()
    last_name = entry_last_name.get()
    dob = entry_dob.get()
    parent_name = entry_parent_name.get()
    address = entry_address.get()
    city = entry_city.get()
    phone_number = entry_phone_number.get()

    # Add student data to the table or database

    # Clear the input fields
    entry_first_name.delete(0, tk.END)
    entry_last_name.delete(0, tk.END)
    entry_dob.delete(0, tk.END)
    entry_parent_name.delete(0, tk.END)
    entry_address.delete(0, tk.END)
    entry_city.delete(0, tk.END)
    entry_phone_number.delete(0, tk.END)

def show_students():
    # Fetch student data from the table or database

    # Display the student data in a table or list

# Create the main window
window = tk.Tk()
window.title("Student Details")
window.geometry("500x300")

# Create labels and entry fields for student details
label_first_name = tk.Label(window, text="First Name:")
label_first_name.pack()
entry_first_name = tk.Entry(window)
entry_first_name.pack()

label_last_name = tk.Label(window, text="Last Name:")
label_last_name.pack()
entry_last_name = tk.Entry(window)
entry_last_name.pack()

label_dob = tk.Label(window, text="Date of Birth:")
label_dob.pack()
entry_dob = tk.Entry(window)
entry_dob.pack()

label_parent_name = tk.Label(window, text="Parent's Name:")
label_parent_name.pack()
entry_parent_name = tk.Entry(window)
entry_parent_name.pack()

label_address = tk.Label(window, text="Address:")
label_address.pack()
entry_address = tk.Entry(window)
entry_address.pack()

label_city = tk.Label(window, text="City:")
label_city.pack()
entry_city = tk.Entry(window)
entry_city.pack()

label_phone_number = tk.Label(window, text="Phone Number:")
label_phone_number.pack()
entry_phone_number = tk.Entry(window)
entry_phone_number.pack()

# Create buttons for adding and showing students
button_add = tk.Button(window, text="Add Student", command=add_student)
button_add.pack()

button_show = tk.Button(window, text="Show Students", command=show_students)
button_show.pack()

# Create a table or list to display the student data

# Start the GUI event loop
window.mainloop()
