import sqlite3

connection = sqlite3.connect("novelas.db")


def insertar():
    nombre = input("Escribe el título de la  novela: ")
    autor = input("Escribe el autor de la novela: ")
    year = input("Escribe el año de la novela: ")

    # Hago la consulta
    cursor = connection.cursor()
    consulta = "INSERT INTO tabla(nombre,autor,year)" \
               "VALUES ('" + nombre + "','" + autor + "'," + year + ");"

    print("insertado") if cursor.execute(consulta) else print("no insertado")

    # Cierro la conexion
    cursor.close()
    connection.commit()
    connection.close()


def consultar():
    # Usa el método row_factory par preparar la consulta
    connection.row_factory = sqlite3.Row

    # Hago la consulta
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM tabla;")

    # Capturo todos los registros
    filas = cursor.fetchall()

    # Lleno la lista con los registros de la tabla
    lista = []
    for fila in filas:
        s = {"id": fila["id"], "nombre": fila["nombre"], "autor": fila["autor"], "year": fila["year"]}
        lista.append(s)

    # Cierro la conexion
    cursor.close()
    connection.commit()
    connection.close()

    # Imprimo la lista
    for novela in lista:
        string = "id: " + str(novela["id"])
        string += ", nombre: " + novela["nombre"]
        string += ", autor: " + novela["autor"]
        string += ", año: " + str(novela["year"])
        print(string)


def eliminar():
    id = input("ingrese el id del registro a eliminar: ")

    # Hago la consulta
    cursor = connection.cursor()
    consulta = "DELETE FROM tabla WHERE id=" + id + ";"

    print("eliminado") if cursor.execute(consulta) else print("no eliminado")

    # Cierro la conexion
    cursor.close()
    connection.commit()
    connection.close()


# Main
opc = int(input("¿1-create, 2-update, 3-read, 4-delete?: "))

if opc == 1:
    insertar()
elif opc == 3:
    consultar()
elif opc == 4:
    eliminar()
