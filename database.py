import sqlite3
db = sqlite3.connect('db.sqlite')

db.execute('DROP TABLE IF EXISTS feedbacks')

db.execute('''CREATE TABLE feedbacks(
	id integer PRIMARY KEY,
	email text NOT NULL,
	message text NOT NULL
)''')

cursor = db.cursor()

cursor.execute('''
	INSERT INTO feedbacks(email, message)
	VALUES('jackson@gmail.com','nice app')
''')

cursor.execute('''
	INSERT INTO feedbacks(email, message)
	VALUES('edward@gmail.com','not bad')
''')

db.commit()
db.close()
