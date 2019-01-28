import sqlite3

prueba = open("novelas.db", "w")
prueba.close()

conexion = sqlite3.connect("novelas.db")

consulta = conexion.cursor()

tabla = "CREATE TABLE tabla(id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,"
tabla += "nombre VARCHAR(30) NOT NULL, autor VARCHAR(40) NOT NULL,"
tabla += "year INTEGER(9) NOT NULL);"

print("tabla creada") if consulta.execute(tabla) else print("tabla no creada")
consulta.close()

conexion.commit()
conexion.close()
