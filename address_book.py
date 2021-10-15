from tkinter import *
import sqlite3 as sql

root = Tk()
root.title('Address Book')
root.geometry("400x400")
root.iconbitmap("G:\Projects\GUI\Icons\matrix.ico")

# Create a database or connect to one
conn = sql.connect('address_book.db')

# Create a cursor
c = conn.cursor()

# Create table
# c.execute("""CREATE TABLE addresses (
#         first_name text,
#         last_name text,
#         city text,
#         state text,
#         zipcode integer 
#         )
#     """)


# Create Function to delete
def delete():
     # Create a database or connect to one
    conn = sql.connect('address_book.db')

    # Create a cursor
    c = conn.cursor()

    c.execute("DELETE FROM addresses WHERE oid = " + select_box.get())

    # Commit changes
    conn.commit()

    # Close Connection
    conn.close() 


# Create Submt fucntion
def submit():
    # Create a database or connect to one
    conn = sql.connect('address_book.db')

    # Create a cursor
    c = conn.cursor()

    # Insert into table
    c.execute("INSERT INTO addresses VALUES (:f_name, :l_name, :city, :state, :zipcode)",
        {
            'f_name' : f_name.get(),
            'l_name' : l_name.get(),
            'city' : city.get(),
            'state' : state.get(),
            'zipcode' : zipcode.get()
        }
        )

    # Commit changes
    conn.commit()

    # Close Connection
    conn.close() 

    # Clear textboxes
    f_name.delete(0, END)
    l_name.delete(0, END)
    city.delete(0, END)
    state.delete(0, END)
    zipcode.delete(0, END)


# Create query functions
def query():
    # Create a database or connect to one
    conn = sql.connect('address_book.db')

    # Create a cursor
    c = conn.cursor()

    # Query the database
    c.execute("SELECT *, oid FROM addresses")
    records = c.fetchall()
    # print(records)
    print_record = ''
    for record in records:
        print_record += str(record) + "\n"
    s_records = Label(root, text="Records").grid(row = 12, column = 0, columnspan = 2)
    query_label = Label(root, text = print_record).grid(row = 13, column = 0, columnspan = 2)
    # Commit changes
    conn.commit()

    # Close Connection
    conn.close() 


# Create save update function
def save_update():
     # Create a database or connect to one
    conn = sql.connect('address_book.db')

    # Create a cursor
    c = conn.cursor()
    record_id = select_box.get()
    c.execute("""UPDATE addresses SET
            first_name = :first,
            last_name = :last,
            city = :city,
            state = :state,
            zipcode = :zipcode 

            WHERE oid = :oid
            """,
        {
            'first' :  f_name_editor.get(),
            'last' : l_name_editor.get(),
            'city' : city_editor.get(),
            'state' : state_editor.get(),
            'zipcode' : zipcode_editor.get(),
            'oid' : record_id

        }    
        )

    # Commit changes
    conn.commit()

    # Close Connection
    conn.close() 

    editor.destroy()

    

# Create an update function
def update():

    # Create a database or connect to one
    conn = sql.connect('address_book.db')

    # Create a cursor
    c = conn.cursor()

    record_id = select_box.get()
    # Query the database
    c.execute("SELECT *, oid FROM addresses WHERE oid =" + record_id)
    records = c.fetchall()
    global editor
    editor = Tk()
    editor.title('Update Record')
    editor.geometry("400x400")
    editor.iconbitmap("G:\Projects\GUI\Icons\matrix.ico")

    # Create global variables for text box name
    global f_name_editor
    global l_name_editor
    global city_editor
    global state_editor
    global zipcode_editor


    # Create text boxes
    f_name_editor = Entry(editor, width = 30)
    f_name_editor.grid(row = 0, column = 1, padx = 20, pady = (10, 0))

    l_name_editor = Entry(editor, width = 30)
    l_name_editor.grid(row = 1, column = 1, padx = 20)

    city_editor = Entry(editor, width = 30)
    city_editor.grid(row = 2, column = 1, padx = 20)

    state_editor = Entry(editor, width = 30)
    state_editor.grid(row = 3, column = 1, padx = 20)

    zipcode_editor = Entry(editor, width = 30)
    zipcode_editor.grid(row = 4, column = 1, padx = 20)

    

    # Create Text Box Labels
    f_name_label_editor = Label(editor, text = "First Name").grid(row = 0, column = 0, pady = (10, 0))
    l_name_label_editor = Label(editor, text = "Last Name").grid(row = 1, column = 0)
    city_label_editor = Label(editor, text = "City").grid(row = 2, column = 0)
    state_label_editor = Label(editor, text = "State").grid(row = 3, column = 0)
    zipcode_label_editor = Label(editor, text = "Zipcode").grid(row = 4, column = 0)
    
    # Loop through Results
    for record in records:
        f_name_editor.insert(0, record[0])
        l_name_editor.insert(0, record[1])
        city_editor.insert(0, record[2])
        state_editor.insert(0, record[3])
        zipcode_editor.insert(0, record[4])

    # create save Button
    save_button = Button(editor, text = "Save", command = save_update).grid(row = 5, column = 0, columnspan = 2, pady = 10, padx = 10, ipadx = 155)

    # Commit changes
    conn.commit()

    # Close Connection
    conn.close() 


# Create text boxes
f_name = Entry(root, width = 30)
f_name.grid(row = 0, column = 1, padx = 20, pady = (10, 0))

l_name = Entry(root, width = 30)
l_name.grid(row = 1, column = 1, padx = 20)

city = Entry(root, width = 30)
city.grid(row = 2, column = 1, padx = 20)

state = Entry(root, width = 30)
state.grid(row = 3, column = 1, padx = 20)

zipcode = Entry(root, width = 30)
zipcode.grid(row = 4, column = 1, padx = 20)

select_box = Entry(root, width = 30)
select_box.grid(row = 9, column = 1)

# Create Text Box Labels
f_name_label = Label(root, text = "First Name").grid(row = 0, column = 0, pady = (10, 0))
l_name_label = Label(root, text = "Last Name").grid(row = 1, column = 0)
city_label = Label(root, text = "City").grid(row = 2, column = 0)
state_label = Label(root, text = "State").grid(row = 3, column = 0)
zipcode_label = Label(root, text = "Zipcode").grid(row = 4, column = 0)
select_box_lable = Label(root, text = "Select ID").grid(row = 9, column = 0)

# Create Submit Button
submit_button = Button(root, text = "Submit", command = submit).grid(row = 5, column = 0, columnspan = 2, pady = 10, padx = 10, ipadx = 100)

# Create a Query button
query_button = Button(root, text = "Show Records", command = query).grid(row = 6, column = 0, columnspan = 2, pady = 10, padx = 10, ipadx = 137)

# Create a delete Button
delete_button = Button(root, text = "Delete Records", command = delete).grid(row = 10, column = 0, columnspan = 2, pady = 10, padx = 10, ipadx = 137)

# Create a update Button
update_button = Button(root, text = "Update Records", command = update).grid(row = 11, column = 0, columnspan = 2, pady = 1, padx = 10, ipadx = 135)


# Commit changes
conn.commit()

# Close Connection
conn.close() 


root.mainloop()