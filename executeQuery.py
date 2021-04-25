import conexionesBD as cBD
import pymysql
import pymysql.cursors

def getConexion():
    try:
        db = pymysql.connect(host=cBD.ConexionesBD.host,
                             user=cBD.ConexionesBD.user,
                             password=cBD.ConexionesBD.password,
                             database=cBD.ConexionesBD.db,
                             cursorclass=cBD.ConexionesBD.cursorClass)
        return db
    except:
        print("Error al obtener la conexión a la base de datos.")

def finalizaConexion(db):
    db.close()

def execute(query):
    db = getConexion()
    try:
        # Preparamos el objeto cursor.
        cursor = db.cursor()

        # Ejecutamos la query.
        #print(query)
        cursor.execute(query)

        filas = cursor.fetchall()

        # Cerramos la conexión con la BBDD.
        db.commit()
        finalizaConexion(db)
        return filas
    except:
        print("Error al ejecutar la sentencia: " + query)
        db.rollback()
        finalizaConexion(db)
        return ""

def executeWithParams(query_params):
    resultado = None
    db = getConexion()
    try:
        # Preparamos el objeto cursor.
        cursor = db.cursor()

        # Ejecutamos la query.
        #print(query_params)
        sql = query_params[0]
        params = query_params[1]

        boInsert = "INSERT" in sql
        boUpdate = "UPDATE" in sql
        boSelect = "SELECT" in sql

        cursor.execute(sql, params)

        if boInsert:
            cursor = db.cursor()
            tabla = sql[12:len(sql)].split(" ")[0]
            query = "SELECT id" + tabla.split("_")[2].lower() + " FROM " + tabla + " ORDER BY id" + tabla.split("_")[2].lower() + " DESC"
            cursor.execute(query)
            identificador = cursor.fetchone()
            resultado = identificador["id" + tabla.split("_")[2].lower()]

        if boSelect:
            resultado = cursor.fetchall()

        # Cerramos la conexión con la BBDD.
        db.commit()
        finalizaConexion(db)
        return resultado
    except:
        print("Error al ejecutar la sentencia: " + query_params)
        db.rollback()
        finalizaConexion(db)
        return ""

def formatearBD():
    sql = "DELETE * FROM BD_D_REPO WHERE 1=1"
    sql2 = "DELETE * FROM BD_D_BUSQUEDA WHERE 1=1"
    execute(sql)
    execute(sql2)
