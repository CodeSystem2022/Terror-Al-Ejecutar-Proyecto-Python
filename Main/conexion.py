import mysql.connector
from mysql.connector import Error

class DAO():

    def __init__(self):
        try:
            self.conexion = mysql.connector.connect(
                host='localhost',
                port=3306,
                user='root',
                pasword='admin',
                db='facturacion'
            )
        except Error as ex:
            print(f"Error al intentar laa conexion: {0}".format(ex))


        def listarFacturas(self):
            if self.conexion.is_connected():
                try:
                    cursor = self.conexion.cursor()
                    cursor.execute("SELECT * FROM facturacion ORDER BY idfacturacion ASC")
                    resultados = cursor.fetchall()
                    return resultados
                except Error as e:
                    print(f"Error al intentar la conexion: {0}".format(ex))
                    
                    
        def registrarFactura(self, factura):
            if self.conexion.is_Connected():
                try:
                    cursor = self.conexion.cursor()
                    sql = "INSERT INTO facturacion (subtotal, impuestos, total) VALUES ('{0}', '{1}', '{2}')"
                    cursor.execute(sql.format(factura[0], factura[1], factura[2], factura[3]))
                    self.connection.commit()
                    print("Factura registrada\n")
                except Error as ex:
                    print("Error al intentar la conexion: {0}".format(ex))