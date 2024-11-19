import sqlalchemy as sa
from sqlalchemy import create_engine, MetaData, Table

# Connect to the SQLite database
engine = create_engine('sqlite:///books.db')
metadata = MetaData()

# Reflect the existing table
book_table = Table('book', metadata, autoload_with=engine)

# Create a session to interact with the database
with engine.connect() as connection:
    # Query all rows from the book table
    result = connection.execute(sa.select(book_table)).fetchall()
    print(result)
    # Print each row
    for row in result:
        print(row)



""" import sqlalchemy as sa
import sqlalchemy.orm as saorm

metadata = sa.MetaData()
book_table = sa.Table('book', metadata,
    sa.Column('title', sa.String, primary_key=True),
    sa.Column('author', sa.String),
    sa.Column('year', sa.Integer))

engine = sa.create_engine('sqlite:///books.db')
metadata.create_all(engine)
Session = saorm.sessionmaker(bind=engine)
session = Session()

rows = session.execute(sa.select(book_table)).fetchall()
print(rows)

for row in rows:
    print(row)

session.close() """

#with engine.connect() as conn:
#    rows = conn.execute(sa.text("SELECT * FROM books"))
#    print(rows.rowcount)




#rows = conn.execute('SELECT * FROM books')
#print(rows.rowcount)
#print("Rows")

#print(rows.rowcount)
    # print('No rows')

#for row in rows:
#    print(row)
#    print("row")

#conn.close()