from logger_base import log


class reciboDAO:

    #Definimos las variables.
    _SELECCIONAR = 'SELECT * FROM ordenes ORDER BY id_ordenes'
    _INSERTAR = 'INSERT INTO ordenes(nombre, apellido, email) VALUES (%s, %s, %s)'
    _ACTUALIZAR = 'UPDATE ordenes SET nombre=%s, apellido=%s, email=%s WHERE id_ordenes=%s'
    _ELIMINAR = 'DELETE FROM ordenes WHERE id_ordenes=%s'

    @classmethod
    def seleccionar(cls):
        #realizamos la conexion de no estar echa
        with Conexion.obtenerConexion(): #debemos comentar para que no de error en pruebas incertar
            #Obtenemos el cursor
            with Conexion.obtenerCursor() as cursor:
                #vamos a ejecutar a travez del cursor el query seleccionar
                cursor.execute(cls._SELECCIONAR)
                registros = cursor.fetchall()
                #creamos una lista vacia que le pasaremos a persona
                recibos = []
                #vamos a recorrer los registros con un for each
                for registro in registros:
                    orden = Persona(registro[0], registro[1], registro[2], registro[3])
                    recibos.append(orden)
                return recibos

    @classmethod
    def insertar(cls, orden):
        with Conexion.obtenerConexion():
            with Conexion.obtenerCursor() as cursor:
                valores = (orden.nombre, orden.apellido, orden.email)
                cursor.execute(cls._INSERTAR, valores)
                log.debug(f'Persona Insertada: {orden}')
                return cursor.rowcount

    @classmethod
    def actualizar(cls, orden):
        with Conexion.obtenerConexion():
            with Conexion.obtenerCursor() as cursor:
                valores = (orden.nombre, orden.apellido, orden.email, orden._id_persona)
                cursor.execute(cls._ACTUALIZAR, valores)
                log.debug(f'Persona actualizada: {orden}')
                return cursor.rowcount

    @classmethod
    def eliminar(cls, orden):
        with Conexion.obtenerConexion() as cursor:
            with Conexion.obtenerCursor():
                valores = (orden.id_ordenes)
                cursor.execute =(cls._ELIMINAR, valores)
                log.debug(f'Los objetos eliminados son: {orden}')
                return cursor.rowcount


