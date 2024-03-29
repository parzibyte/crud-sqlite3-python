"""
CRUD de SQLite3 con Python 3
@author parzibyte
Más tutoriales en: parzibyte.me/blog
"""
import sqlite3
try:
 
	#Conectar a la base de datos
	bd = sqlite3.connect("libros.db")
	cursor = bd.cursor()
 
	#Listar los libros
 
	sentencia = "SELECT *,rowid FROM libros;"
 
	cursor.execute(sentencia)
	
	libros = cursor.fetchall()
	print("+{:-<20}+{:-<20}+{:-<10}+{:-<50}+{:-<10}+".format("", "", "", "", ""))
	print("|{:^20}|{:^20}|{:^10}|{:^50}|{:^10}|".format("Autor", "Género", "Precio", "Título", "Rowid"))
	print("+{:-<20}+{:-<20}+{:-<10}+{:-<50}+{:-<10}+".format("", "", "", "", ""))
 
 
	for autor, genero, precio, titulo, rowid in libros:
		print("|{:^20}|{:^20}|{:^10}|{:^50}|{:^10}|".format(autor, genero, precio, titulo, rowid))
	
 
	print("+{:-<20}+{:-<20}+{:-<10}+{:-<50}+{:-<10}+".format("", "", "", "", ""))
 
	#Pedir id del libro a editar
	id_libro = input("\nEscribe el id del libro que quieres editar: ")
	if not id_libro:
		print("No escribiste nada")
		exit()
 
	#Pedir nuevos datos
	autor = input("\nNuevo autor: ")
	genero = input("\nNuevo género: ")
	precio = float(input("\nNuevo precio: "))
	titulo = input("\nNuevo título: ")
 
	#Sentencia para actualizar
	sentencia = "UPDATE libros SET autor = ?, genero = ?, precio = ?, titulo = ? WHERE rowid = ?;"
 
	#Actualizar datos
	cursor.execute(sentencia, [autor, genero, precio, titulo, id_libro])
	bd.commit()
	print("Datos guardados")
 
except sqlite3.OperationalError as error:
	print("Error al abrir:", error)