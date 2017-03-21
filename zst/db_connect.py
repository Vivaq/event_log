import sqlite3
import os

db = sqlite3.connect(os.getcwd() + '/db.sqlite3')
c = db.cursor()
c.execute('')
db.commit()
