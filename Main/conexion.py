import mysql.connector
from mysql.connector import Error

class DAO:
    def __init__(self):
        try:
            self.conexion = mysql.connector.connect(
                host='localhost',
                port=3306,
                user='root',
                password='2005',
                db='facturacion'
            )
        except Error as ex:
            print(f"Error al intentar la conexión: {ex}")


    def listarFacturas(self):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                cursor.execute("SELECT * FROM facturacion ORDER BY idfacturacion ASC")
                resultados = cursor.fetchall()
                return resultados
            except Error as ex:
                print(f"Error al intentar la conexion: {0}".format(ex))

    def registrarFactura(self, factura):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sql = "INSERT INTO facturacion (subtotal, impuestos, total) VALUES (%s, %s, %s)"
                cursor.execute(sql, factura)
                self.conexion.commit()
                print("Factura registrada\n")
            except Error as ex:
                print("Error al intentar la conexión: {ex}")









