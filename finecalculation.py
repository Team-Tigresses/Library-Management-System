import sqlite3
from tkinter import *
from tkinter import ttk
import math

# making a connection
connection = sqlite3.connect('Borrowing_history.db')

# making a cursor
cursor = connection.cursor()

# creating the users table
cursor.execute("""create table if not exists users (
id integer primary key,
name text,
book_name text,
borrow_date date,
return_date date,
fine float default 0.0)""")

# commiting the changes
connection.commit()


# GUI design variables
lf_bg = '#ffc2cd'  # Left Frame Background Color
rtf_bg = '#ffc3cd'  # Right Top Frame Background Color
rbf_bg = '#ff93ac'  # Right Bottom Frame Background Color
btn_hlb_bg = '#ff6289'  # Background color for Head Labels and Buttons

lbl_font = ('Palentino Linotype', 13)  # Font for all labels
entry_font = ('Palentino Linotype', 12)  # Font for all Entry widgets
btn_font = ('Palentino Linotype', 13)

# GUI window
root = Tk()
root.title("Calculation System")
root.geometry("400x400")
root.config(bg=lf_bg)

# calculate fine function
def calculate_fine():
    try:
        # get user input from the entry box
        user_id = int(user_id_entry.get())
        return_date = return_date_entry.get()
        
        # calculate fine
        cursor.execute(f"SELECT borrow_date FROM users WHERE id == {user_id}")
        borrow_date = cursor.fetchone()[0]
        days = (int(return_date[-2:]) - int(borrow_date[-2:]))
        fine_per_day = 1
        fine = days * fine_per_day
        
        # update the database
        cursor.execute(f"UPDATE users SET fine = {fine} WHERE id == {user_id}")
        connection.commit()
        
        # display the result
        result_label.config(text="Fine: Rs." + str(fine))
    except Exception as e:
        # if an error occurs, display a message to the user
        result_label.config(text="Error: " + str(e))

# GUI design
# create a label for user ID
user_id_label = Label(root, text="User ID:", bg=lf_bg, fg='#ff084a', font=lbl_font)
user_id_label.pack(pady=10)

# create an entry box for user ID
user_id_entry = Entry(root, font=entry_font, width=30)
user_id_entry.pack()

# create a label for return date
return_date_label = Label(root, text="Return Date (YYYY-MM-DD):", fg='#ff084a', bg=lf_bg, font=lbl_font)
return_date_label.pack(pady=10)

# create an entry box for return date
return_date_entry = Entry(root, font=entry_font, width=30)
return_date_entry.pack()

# create a button to calculate fine
calculate_btn = Button(root, bg=btn_hlb_bg, text="Calculate Fine", font=btn_font, fg='#ffc2cd', command=calculate_fine)
calculate_btn.pack(pady=10)

# create a label to display the result
result_label = Label(root, bg=lf_bg, fg='#ff084a', font=lbl_font)
result_label.pack(pady=10)

# start the GUI mainloop
root.mainloop()

# close the database connection
connection.close()
