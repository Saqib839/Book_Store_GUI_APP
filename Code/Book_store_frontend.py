from tkinter import *
import Book_store_backend as be

window = Tk()
window.wm_title('Book store')
inp1 = StringVar()
inp2 = StringVar()
inp3 = StringVar()
inp4 = StringVar()

def command_view():
    List1.delete(0,END)
    for row in be.view():
        List1.insert(END,row)
def command_search():
    List1.delete(0,END)
    for row in be.search(inp1.get(),inp2.get(),inp3.get(),inp4.get()):
        List1.insert(END,row)
def command_insert():
    be.insert(inp1.get(),inp2.get(),inp3.get(),inp4.get())
    List1.delete(0,END)
    command_view()
def command_delete_all():
    be.delete_all()
    List1.delete(0,END)
def get_selected_row(event):
    try:
        global selected_tuple
        index = List1.curselection()[0]
        selected_tuple= List1.get(index)
        E1.delete(0,END)
        E1.insert(END,selected_tuple[1])
        E2.delete(0,END)
        E2.insert(END,selected_tuple[2])
        E3.delete(0,END)
        E3.insert(END,selected_tuple[3])
        E4.delete(0,END)
        E4.insert(END,selected_tuple[4])
    except IndexError:
        pass
def command_delete():
    be.delete(selected_tuple[0])
    command_view()
def command_update():
    be.update(selected_tuple[0],E1.get(),E2.get(),E3.get(),E4.get())
    command_view()
    


L1 =Label(window, text= 'Title' , width=14)
L1.grid(row=0, column=0, columnspan=1)
E1 = Entry (window, textvariable=inp1)
E1.grid(row=0, column=1)
L2 =Label(window, text = 'Author' , width=14)
L2.grid(row=0, column=2, columnspan=1)
E2 = Entry (window, textvariable=inp2)
E2.grid(row=0, column=3)

L3 =Label(window, text= 'Year')
L3.grid(row=1, column=0, columnspan=1)
E3 = Entry (window, textvariable=inp3)
E3.grid(row=1, column=1)
L4 =Label(window, text = 'ISBN')
L4.grid(row=1, column=2, columnspan=1)
E4 = Entry (window, textvariable=inp4)
E4.grid(row=1, column=3)

List1 = Listbox(window, height =10, width=45)
List1.grid(row=3, column=0, rowspan=6, columnspan=3)
scrol1 = Scrollbar(window)
scrol1.grid(row=3, column=2,rowspan=6 )
List1.configure(yscrollcommand=scrol1.set)
scrol1.configure(command=List1.yview)
List1.bind('<<ListboxSelect>>',get_selected_row)


B1= Button(window, text= 'View all', width=14, command=command_view)
B1.grid(row=2, column=3, columnspan=1)
B2= Button(window, text= 'Search Entry', width=14, command=command_search)
B2.grid(row=3, column=3, columnspan=1)
B3= Button(window, text= 'Add Entry', width=14,command=command_insert)
B3.grid(row=4, column=3, columnspan=1)
B4= Button(window, text= 'Update Selected', width=14,command=command_update)
B4.grid(row=5, column=3, columnspan=1)
B5= Button(window, text= 'Delete Selected', width=14, command=command_delete)
B5.grid(row=6, column=3, columnspan=1)
B6= Button(window, text= 'Delete all', width=14, command=command_delete_all)
B6.grid(row=7, column=3, columnspan=1)
B7= Button(window, text= 'Close', width=14, command=window.destroy)
B7.grid(row=8, column=3, columnspan=1)


window.mainloop()