import sqlite3

conn = sqlite3.connect('example.db')

c = conn.cursor()


def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS stuffTOPlot(unix REAL, datestamp TEXT, keyword TEXT, value REAL)')


def insert_data():
    c.execute("INSERT INTO stuffTOPlot VALUES(14512332, '31.11.2011', 'Python', 6)")


def show_data():
    for row in c.execute('SELECT * FROM stocks ORDER BY price'):  # the table is an iterable
        print(row)


create_table()
show_data()

# Save (commit) the changes
conn.commit()

# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
c.close()
conn.close()

