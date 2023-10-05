import sqlite3

def table():
    connect1 = sqlite3.connect('database.db')
    cur = connect1.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS storage(id INTEGER PRIMARY KEY, title TEXT, author TEXT, year INT, isbn INT)')
    connect1.commit()
    connect1.close()

def view():
    table()
    connect1 = sqlite3.connect('database.db')
    cur = connect1.cursor()
    cur.execute('SELECT * from storage')
    rows=cur.fetchall()
    connect1.close()
    return rows

def insert(title,author,year,isbn):
    connect1 = sqlite3.connect('database.db')
    cur = connect1.cursor()
    cur.execute("INSERT INTO storage VALUES(NULL,?,?,?,?)",(title,author,year,isbn))
    connect1.commit()
    connect1.close()

def delete(id):
    connect1 = sqlite3.connect('database.db')
    cur = connect1.cursor()
    cur.execute("DELETE FROM storage WHERE id=? ",(id,))
    connect1.commit()
    connect1.close()

def update(id,title,author,year,isbn):
    connect1 = sqlite3.connect('database.db')
    cur = connect1.cursor()
    cur.execute("UPDATE storage SET title=?, author=?, year=?, isbn=? WHERE id=? ",(title,author,year,isbn,id))
    connect1.commit()
    connect1.close()

def search(title='',author='',year=0,isbn=0):
    connect1 = sqlite3.connect('database.db')
    cur = connect1.cursor()
    cur.execute("SELECT * FROM storage WHERE title=? OR author=? OR year=? OR isbn=?",(title,author,year,isbn))
    rows= cur.fetchall()
    connect1.commit()
    connect1.close()
    return rows

def delete_all():
    Connect1 = sqlite3.connect('database.db')
    cur = Connect1.cursor()
    cur.execute('DELETE FROM storage')
    Connect1.commit()
    Connect1.close()


#add('english','matt',2001,7967868)
#update('english','touseef888', 20144,857857)
#delete(1)
#update(3,'urdu1','mos',4000,686868)
#print(search(author='mat'))