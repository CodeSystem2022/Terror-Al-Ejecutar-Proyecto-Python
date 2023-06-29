import mysql.connector
from mysql.connector import Error

class DAO:
    def __init__(self):
        try:
            self.conexion = mysql.connector.connect(
                host='localhost',
                port=3306,
                user='root',
                password='',
                database='facturacion'
            )
            print('Se estableció la conexión')
        except Error as ex:
            print(f"Error al intentar la conexión: {ex}")

    def listarFacturas(self):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                cursor.execute("SELECT * FROM facturas ORDER BY idfacturacion ASC")
                resultados = cursor.fetchall()
                return resultados
            except Error as ex:
                print(f"Error al intentar la conexión: {ex}")

    def registrar_factura(self, subtotal, total, impuesto):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sql = "INSERT INTO facturas (subtotal, total, impuesto) VALUES (%s, %s, %s)"
                valores = (subtotal, total, impuesto)
                cursor.execute(sql, valores)
                self.conexion.commit()
                print("Factura registrada\n")
            except Error as ex:
                print(f"Error al intentar la conexión: {ex}")
            finally:
                if cursor is not None:
                    cursor.close()

