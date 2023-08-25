import os
from os.path import join, getsize
import sqlite3

conn = sqlite3.connect("example.db")
cur = conn.cursor()
cur.execute("SELECT * FROM stocks ORDER BY price")


for root, dirs, files in os.walk("./"):
    print(root, "consumes ")
    print(sum(getsize(join(root, name)) for name in files), end=" ")
    print("bytes in", len(files), "non-directory files")
