import executeQuery
import configuracion as conf

class RepoBD:
    id = -1
    nombre = ""
    organizacion = ""
    lenguaje = ""
    size = 0
    commitID = ""
    url = ""
    boE2e = False
    idbusqueda = -1
    tstbd = ""

    def __init__(self):
        self.id = -1
        self.nombre = ""
        self.organizacion = ""
        self.lenguaje = ""
        self.size = 0
        self.commitID = ""
        self.url = ""
        self.boE2e = False
        self.idbusqueda = -1
        self.tstbd = conf.Configuracion.fechaEjecucion

    def getInsert(self):

        campos = ""
        values = ""

        if(self.id >0):
            campos += "IDREPO,"
            values += str(self.id) + ","

        if (len(str(self.nombre)) > 0):
            campos += "NOMBRE,"
            values += "'" + str(self.nombre) + "',"

        if (len(str(self.organizacion)) > 0):
            campos += "ORGANIZACION,"
            values += "'" + str(self.organizacion) + "',"

        if (len(str(self.lenguaje)) > 0):
            campos += "LENGUAJE,"
            values += "'" + str(self.lenguaje) + "',"

        if (self.size > 0):
            campos += "SIZE,"
            values += str(self.size) + ","

        if (len(str(self.commitID)) > 0):
            campos += "COMMITID,"
            values += "'" + str(self.commitID) + "',"

        if (len(str(self.url)) > 0):
            campos += "URL,"
            values += "'" + str(self.url) + "',"

        if (self.boE2e):
            campos += "BOE2E,"
            values += "1" + ","
        else:
            campos += "BOE2E,"
            values += "0" + ","

        if (self.idbusqueda > 0):
            campos += "IDBUSQUEDA,"
            values += str(self.idbusqueda) + ","

        if (len(str(self.tstbd)) > 0):
            campos += "TSTBD,"
            values += "'" + str(self.tstbd) + "',"

        campos = campos[0:len(campos) - 1]
        values = values[0:len(values) - 1]
        insert = "INSERT INTO BD_D_REPO (" + campos + ") VALUES (" + values + ")"

        insert += ";"

        return insert

    def getUpdate(self):
        if(self.id == -1 or self.id == 0):
            print("El objeto repoBD no tiene IDREPO. No se puede actualizar.")
            return ""

        values = ""
        if (len(str(self.nombre)) > 0):
            values += "NOMBRE='"  + str(self.nombre) + "',"

        if (len(str(self.organizacion)) > 0):
            values += "ORGANIZACION='" + str(self.organizacion) + "',"

        if (len(str(self.lenguaje)) > 0):
            values += "LENGUAJE='" + str(self.lenguaje) + "',"

        if (self.size > 0):
            values += "SIZE=" + str(self.size) + ","

        if (len(str(self.commitID)) > 0):
            values += "COMMITID='" + str(self.commitID) + "',"

        if (len(str(self.url)) > 0):
            values += "URL='" + str(self.url) + "',"

        if (self.boE2e):
            values += "BOE2E=1,"
        else:
            values += "BOE2E=0,"

        if (self.idbusqueda > 0):
            values += "IDBUSQUEDA=" + str(self.idbusqueda) + ","

        if (len(str(self.tstbd)) > 0):
            values += "TSTBD='" + str(self.tstbd) + "',"

        values = values[0:len(values) - 1]
        update = "UPDATE BD_D_REPO SET " + values + " WHERE IDREPO = " + str(self.id)

        update += ";"

        return update

    def getFiltro(self):
        select = "SELECT * FROM BD_D_REPO WHERE 1=1"

        if (self.id > 0):
            select += " AND IDREPO=" + str(self.id)

        if (len(str(self.nombre)) > 0):
            select += " AND NOMBRE='" + str(self.nombre) + "'"

        if (len(str(self.organizacion)) > 0):
            select += " AND ORGANIZACION='" + str(self.organizacion) + "'"

        if (len(str(self.lenguaje)) > 0):
            select += " AND LENGUAJE='" + str(self.lenguaje) + "'"

        if (self.size > 0):
            select += " AND SIZE=" + str(self.size)

        if (len(str(self.commitID)) > 0):
            select += " AND COMITID='" + str(self.commitID) + "'"

        if (len(str(self.url)) > 0):
            select += " AND URL='" + str(self.url) + "'"

        if (self.boE2e):
            select += " AND BOE2E=1"
        else:
            select += " AND BOE2E=0"

        if (self.idbusqueda > 0):
            select += " AND IDBUSQUEDA=" + str(self.idbusqueda)

        if (len(str(self.tstbd)) > 0):
            select += " AND TSTBD='" + str(self.tstbd) + "'"

        select += ";"

        return select

    def getDelete(self):
        delete = "DELETE BD_D_REPO WHERE 1=1"

        if (self.id > 0):
            delete += " AND IDREPO=" + str(self.id)

        if (len(str(self.nombre)) > 0):
            delete += " AND NOMBRE='" + str(self.nombre) + "'"

        if (len(str(self.organizacion)) > 0):
            delete += " AND ORGANIZACION='" + str(self.organizacion) + "'"

        if (len(str(self.lenguaje)) > 0):
            delete += " AND LENGUAJE='" + str(self.lenguaje) + "'"

        if (self.size > 0):
            delete += " AND SIZE=" + str(self.size)

        if (len(str(self.commitID)) > 0):
            delete += " AND COMITID='" + str(self.commitID) + "'"

        if (len(str(self.url)) > 0):
            delete += " AND URL='" + str(self.url) + "'"

        if (self.boE2e):
            delete += " AND BOE2E=1"
        else:
            delete += " AND BOE2E=0"

        if (self.idbusqueda > 0):
            delete += " AND IDBUSQUEDA=" + str(self.idbusqueda)

        if (len(str(self.tstbd)) > 0):
            delete += " AND TSTBD='" + str(self.tstbd) + "'"

        delete += ";"

        return delete

    # GETTER & SETTER
    def getId(self):
        return self.id

    def setId(self, id):
        self.id = id

    def getNombre(self):
        return self.nombre

    def setNombre(self, nombre):
        self.nombre = nombre

    def getOrganizacion(self):
        return self.organizacion

    def setOrganizacion(self, organizacion):
        self.organizacion = organizacion

    def getLenguaje(self):
        return self.lenguaje

    def setLenguaje(self, lenguaje):
        self.lenguaje = lenguaje

    def getSize(self):
        return self.size

    def setSize(self, size):
        self.size = size

    def getCommitID(self):
        return self.commitID

    def setCommitID(self, commitID):
        self.commitID = commitID

    def getUrl(self):
        return self.url

    def setUrl(self, url):
        self.url = url

    def getBoE2e(self):
        return self.boE2e

    def setBoE2e(self, boE2e):
        self.boE2e = boE2e

    def getIdBusqueda(self):
        return self.idbusqueda

    def setIdBusqueda(self, idbusqueda):
        self.idbusqueda = idbusqueda

    def getTstbd(self):
        return self.tstbd

    def setTstbd(self, tstbd):
        self.tstbd = tstbd

def createRepoBD():
    repoBD = RepoBD()
    return repoBD