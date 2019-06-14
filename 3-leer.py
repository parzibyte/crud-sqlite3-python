"""
CRUD de SQLite3 con Python 3
@author parzibyte
Más tutoriales en: parzibyte.me/blog
"""
import sqlite3
try:
	bd = sqlite3.connect("libros.db")
	cursor = bd.cursor()
	sentencia = "SELECT * FROM libros;"
 
	cursor.execute(sentencia)
	
	libros = cursor.fetchall()
	
	print(libros)
except sqlite3.OperationalError as error:
	print("Error al abrir:", error)