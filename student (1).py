from tkinter import *
from tkinter import ttk, messagebox
import backend
from database import Database
from backend import search


class student:
        def __init__(self,window):
            self.window = window
            
            self.database = Database(db='books.db')
            
            self.frame = Frame(self.window, bg = '#ff93ac', width=700,height=400)

            self.label = Label(self.frame,text='Student User',bg='#ff93ac',font=('Palentino Linotype',30,'bold'))
            self.label.place(x=20,y=20,width=400,height=50)

            self.label_title = Label(self.frame, text='TITLE',bg='#ff93ac',font=('Palentino Linotype',14,'bold'))
            self.label_title.place(x=20,y=100,width=100,height=50)

            self.label_year = Label(self.frame, text='YEAR',bg='#ff93ac',font=('Palentino Linotype',14,'bold'))
            self.label_year.place(x=20,y=150,width=100,height=30)

            self.label_author = Label(self.frame, text='AUTHOR',bg='#ff93ac',font=('Palentino Linotype',14,'bold'))
            self.label_author.place(x=350,y=100,width=100,height=30)

            self.label_isbn = Label(self.frame, text='ISBN',bg='#ff93ac',font=('Palentino Linotype',14,'bold'))
            self.label_isbn.place(x=350,y=150,width=100,height=30)

            self.title_text=StringVar()
            self.entry_title = Entry(self.frame, fg='#ff084a',textvariable=self.title_text,width=25,font=('Palentino Linotype',12,'bold'))
            self.entry_title.place(x=120,y=100,width=150,height=30)

            self.year_text=StringVar()
            self.entry_year = Entry(self.frame, fg='#ff084a',textvariable=self.year_text,width=25,font=('Palentino Linotype',12,'bold'))
            self.entry_year.place(x=120,y=150,width=150,height=30)

            self.author_text=StringVar()
            self.entry_author = Entry(self.frame, fg='#ff084a',textvariable=self.author_text,width=25,font=('Palentino Linotype',12,'bold'))
            self.entry_author.place(x=470,y=100,width=150,height=30)

            self.isbn_text=StringVar()
            self.entry_isbn = Entry(self.frame, fg='#ff084a',textvariable=self.isbn_text,width=25,font=('Palentino Linotype',12,'bold'))
            self.entry_isbn.place(x=470,y=150,width=150,height=30)

            # self.listbox = Listbox(self.frame)
            # self.listbox.place(x=100,y=200,width=500,height=100)
            self.treeview = ttk.Treeview(self.window)
            
            #treeview
            self.tree = ttk.Treeview(self.frame, columns = ('title', 'year', 'author', 'isbn'))
            self.tree.heading('#0', text = 'ID')
            self.tree.heading('title', text = 'Title')
            self.tree.heading('year', text = 'Year')
            self.tree.heading('author', text = 'Author')
            self.tree.heading('isbn', text = 'ISBN')
            self.tree.column('#0', width = 50)
            self.tree.column('title', width = 200)
            self.tree.column('year', width = 100)
            self.tree.column('author', width = 200)
            self.tree.column('isbn', width = 100)
            self.tree.place(x = 100, y = 200, width = 500, height = 100)

            self.button_view = Button(self.frame,text='View All', command=self.view_command)
            self.button_view.place(x=100,y=320,width=100,height=40)

            self.button_search = Button(self.frame,text='Search ', command=self.search_command)
            self.button_search.place(x=200,y=320,width=100,height=40)

            self.button_issue = Button(self.frame,text='Issue', command=self.issue_command)
            self.button_issue.place(x=300,y=320,width=100,height=40)

            self.button_request = Button(self.frame, text='Request', command = self.request_command)
            self.button_request.place(x=400, y=320,width=100,height=40)

            self.button_issue = Button(self.frame, text='Clear Fields', command=self.clear_command)
            self.button_issue.place(x=500, y=320,width=100,height=40)

            self.frame.pack()

        def clear_command(self):
            self.treeview.delete(*self.treeview.get_children())
            self.title_text.set('')
            self.year_text.set('')
            self.author_text.set('')
            self.isbn_text.set('')

        def request_command(self):
            # backend.request_insert(self.title_text.get(),self.author_text.get(),self.year_text.get(),self.isbn_text.get())
            # self.listbox.delete(0,END)
            # self.listbox.insert(END,(self.title_text.get(),self.author_text.get(),self.year_text.get(),self.isbn_text.get()))

            title = self.title_text.get()
            year = self.year_text.get()
            author = self.author_text.get()
            isbn = self.isbn_text.get()

            # TODO: Implement request functionality


        def issue_command(self):
            # selected_tuple=self.listbox.curselection()
            # value = self.listbox.get(selected_tuple)
            # self.entry_title.delete(0,END)
            # self.entry_title.insert(END,value[1])
            # self.entry_year.delete(0,END)
            # self.entry_year.insert(END,value[2])
            # self.entry_author.delete(0,END)
            # self.entry_author.insert(END,value[3])
            # self.entry_isbn.delete(0,END)
            # self.entry_isbn.insert(END,value[4])
            # backend.issue_insert(value[0])

            selected_items = self.treeview.selection()
            if len(selected_items) == 0:
                messagebox.showwarning('Warning', 'Please select an item to issue.')
            else:
                item = self.treeview.item(selected_items[0])
                id = item['text']
                title = item['values'][0]
                year = item['values'][1]
                author = item['values'][2]
                isbn = item['values'][3]
    
                # TODO: Implement issue functionality

        def view_command(self):
            # Clear existing data in the Treeview
            for item in self.tree.get_children():
                self.tree.delete(item)
            # Add new data to the Treeview
            for book in self.database.view():
                self.tree.insert("", 'end', text=book[0], values=(book[1], book[2], book[3], book[4]))
                
        def search_command(self):
            # self.listbox.delete(0,END)
            # for row in backend.search(self.title_text.get(),self.author_text.get(),self.year_text.get(),self.isbn_text.get()):
            #     self.listbox.insert(END,row)
            title = self.title_text.get().strip()
            author = self.author_text.get().strip()
            year = self.year_text.get().strip()
            isbn = self.isbn_text.get().strip()

            # clear existing items in treeview
            self.tree.delete(*self.tree.get_children())

            # search for books that match the given criteria
            books = search(title = title, author = author, year = year, isbn = isbn)

            # add matching books to treeview
            for book in books:
                self.tree.insert('', 'end', text = book[0], values = book[1:])
                
                
        def add_command(self):
            # backend.insert(self.title_text.get(),self.author_text.get(),self.year_text.get(),self.isbn_text.get())
            # self.listbox.delete(0,END)
            # self.listbox.insert(END,(self.title_text.get(),self.author_text.get(),self.year_text.get(),self.isbn_text.get()))

            title = self.title_text.get().strip()
            author = self.author_text.get().strip()
            year = self.year_text.get().strip()
            isbn = self.isbn_text.get().strip()

            # add book to database
            add_book(title = title, author = author, year = year, isbn = isbn)

            # clear existing items in treeview
            self.tree.delete(*self.tree.get_children())

            # refresh treeview with updated book list
            self.view_command()
            
            
        def delete_command(self):
            # selected_tuple=self.listbox.curselection()
            # value = self.listbox.get(selected_tuple)
            # self.entry_title.delete(0,END)
            # self.entry_title.insert(END,value[1])
            # self.entry_year.delete(0,END)
            # self.entry_year.insert(END,value[2])
            # self.entry_author.delete(0,END)
            # self.entry_author.insert(END,value[3])
            # self.entry_isbn.delete(0,END)
            # self.entry_isbn.insert(END,value[4])
            # backend.delete(value[0])

            # get the currently selected book ID
            selection = self.tree.selection()
            if selection:
                book_id = self.tree.item(selection[0], 'text')
    
                # delete book from database
                delete_book(book_id)
    
                # remove book from treeview
                self.tree.delete(selection[0])
                
                
        def update_command(self):
            # selected_tuple=self.listbox.curselection()
            # value = self.listbox.get(selected_tuple)
            # self.entry_title.delete(0,END)
            # self.entry_title.insert(END,value[0])
            # self.entry_year.delete(0,END)
            # self.entry_year.insert(END,value[1])
            # self.entry_author.delete(0,END)
            # self.entry_author.insert(END,value[2])
            # self.entry_isbn.adelete(0,END)
            # self.entry_isbn.insert(END,value[3])
            # backend.update(value[0],self.title_text.get(),self.author_text.get(),self.year_text.get(),self.isbn_text.get())

            selected_item = self.treeview.focus()
            if selected_item:
                old_data = self.treeview.item(selected_item)['values']
                if self.title_text.get() == '' or self.author_text.get() == '' or self.year_text.get() == '' or self.isbn_text.get() == '':
                    messagebox.showerror('Error', 'All fields are required')
                else:
                    new_data = (
                    self.title_text.get(), self.author_text.get(), self.year_text.get(), self.isbn_text.get())
                    self.db.update(old_data, new_data)
                    self.view_command()
                    messagebox.showinfo('Success', 'Book Updated Successfully')
            else:
                messagebox.showerror('Error', 'Please select a book to update')
'''
window = Tk()
window.title('Student_User')
window.geometry('700x400')
obj = student(window)
window.mainloop()'''