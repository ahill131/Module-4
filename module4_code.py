import csv
import sqlite3

conn = sqlite3.connect('books.db')
curs = conn.cursor()
# curs.execute('''CREATE TABLE books
#    (title STRING PRIMARY KEY,
#     author STRING,
#     year INT)''')

#with open('books2.csv', 'rt') as fin:
#    cin = csv.reader(fin)
#    books2 = [row for row in cin]

#ins = 'INSERT INTO books (title, author, year) VALUES(?, ?, ?)'
#conn.execute(ins, ('The Weirdstone of Brisingamen', 'Alan Garner', 1960))
#conn.execute(ins, ('Perdido Street Station', 'China Miéville', 2000))
#conn.execute(ins, ('Thud!', 'Terry Pratchett', 2005))
#conn.execute(ins, ('The Spellman Files', 'Lisa Lutz', 2007))
#conn.execute(ins, ('Small Gods', 'Terry Pratchett', 1992))
#conn.execute(ins, ('Brain Plahgue', 'Joan Slonczewski', 2001))



#for row in range(1, 6):
#    curs.execute(ins, (books2[row]))
#    print(books2[row])

curs.execute('SELECT * FROM books')
rows = curs.fetchall()
print(rows)

curs.close()
conn.close()