import configuracion as conf
import pymysql
import pymysql.cursors

def getConexion():
    db = pymysql.connect(host=conf.ConexionesBD.host,
                         user=conf.ConexionesBD.user,
                         password=conf.ConexionesBD.password,
                         database=conf.ConexionesBD.db,
                         cursorclass=conf.ConexionesBD.cursorClass)
    return db

def finalizaConexion(db):
    db.close()

def execute(query):
    try:
        db = getConexion()

        # Preparamos el objeto cursor.
        cursor = db.cursor()

        # Ejecutamos la query.
        cursor.execute(query)

        filas = cursor.fetchall()
        for fila in filas:
            print(fila)

        # Cerramos la conexión con la BBDD.
        db.commit()
        finalizaConexion(db)
        return filas
    except:
        db.rollback()
        finalizaConexion(db)
        return ""

def formatearBD():
    sql = "DELETE * FROM BD_D_REPO WHERE 1=1"
    execute(sql)
