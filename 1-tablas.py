"""
CRUD de SQLite3 con Python 3
@author parzibyte
Más tutoriales en: parzibyte.me/blog
"""
import sqlite3
try:
	bd = sqlite3.connect("libros.db")
	cursor = bd.cursor()
	tablas = [
		"""
			CREATE TABLE IF NOT EXISTS libros(
				autor TEXT NOT NULL,
				genero TEXT NOT NULL,
				precio REAL NOT NULL,
				titulo REAL NOT NULL
			);
		"""
	]
	for tabla in tablas:
		cursor.execute(tabla);
	print("Tablas creadas correctamente")
except sqlite3.OperationalError as error:
	print("Error al abrir:", error)