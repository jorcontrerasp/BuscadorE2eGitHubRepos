import executeQuery

class RepoBD:
    id = ""
    nombre = ""
    organizacion = ""
    size = 0
    commitID = ""
    url = ""
    boE2e = False

    def __init__(self):
        self.id = ""
        self.nombre = ""
        self.organizacion = ""
        self.size = 0
        self.commitID = ""
        self.url = ""
        self.boE2e = False

    def getInsert(self):

        campos = ""
        values = ""

        if(len(self.id) >0):
            campos += "ID,"
            values += self.id + ","

        if (len(self.nombre) > 0):
            campos += "NOMBRE,"
            values += "'" + self.nombre + "',"

        if (len(self.organizacion) > 0):
            campos += "ORGANIZACION,"
            values += "'" + self.organizacion + "',"

        if (self.size > 0):
            campos += "SIZE,"
            values += str(self.size) + ","

        if (len(self.commitID) > 0):
            campos += "COMMITID,"
            values += "'" + self.commitID + "',"

        if (len(self.url) > 0):
            campos += "URL,"
            values += "'" + self.url + "',"

        if (self.boE2e):
            campos += "BOE2E,"
            values += "1" + ","
        else:
            campos += "BOE2E,"
            values += "0" + ","

        campos = campos[0:len(campos) - 1]
        values = values[0:len(values) - 1]
        insert = "INSERT INTO BD_D_REPO (" + campos + ") VALUES (" + values + ")"

        insert += ";"

        return insert

    def getUpdate(self):
        if(len(self.id) == 0):
            print("El objeto repoBD no tiene ID. No se puede actualizar.")
            return ""

        values = ""
        if (len(self.nombre) > 0):
            values += "NOMBRE='"  + self.nombre + "',"

        if (len(self.organizacion) > 0):
            values += "ORGANIZACION='" + self.organizacion + "',"

        if (self.size > 0):
            values += "SIZE=" + str(self.size) + ","

        if (len(self.commitID) > 0):
            values += "COMMITID='" + self.commitID + "',"

        if (len(self.url) > 0):
            values += "URL='"  + self.url + "',"

        if (self.boE2e):
            values += "BOE2E=1,"
        else:
            values += "BOE2E=0,"

        values = values[0:len(values) - 1]
        update = "UPDATE BD_D_REPO SET " + values + " WHERE ID = " + self.id

        update += ";"

        return update

    def getFiltro(self):
        select = "SELECT * FROM BD_D_REPO WHERE 1=1"

        if (len(self.id) > 0):
            select += " AND ID=" + self.id

        if (len(self.nombre) > 0):
            select += " AND NOMBRE='" + self.nombre + "'"

        if (len(self.organizacion) > 0):
            select += " AND ORGANIZACION='" + self.organizacion + "'"

        if (self.size > 0):
            select += " AND SIZE=" + str(self.size)

        if (len(self.commitID) > 0):
            select += " AND COMITID='" + self.commitID + "'"

        if (len(self.url) > 0):
            select += " AND URL='" + self.url + "'"

        if (self.boE2e):
            select += " AND BOE2E=1"
        else:
            select += " AND BOE2E=0"

        select += ";"

        return select

    def getDelete(self):
        delete = "DELETE BD_D_REPO WHERE 1=1"

        if (len(self.id) > 0):
            delete += " AND ID=" + self.id

        if (len(self.nombre) > 0):
            delete += " AND NOMBRE='" + self.nombre + "'"

        if (len(self.organizacion) > 0):
            delete += " AND ORGANIZACION='" + self.organizacion + "'"

        if (self.size > 0):
            delete += " AND SIZE=" + str(self.size)

        if (len(self.commitID) > 0):
            delete += " AND COMITID='" + self.commitID + "'"

        if (len(self.url) > 0):
            delete += " AND URL='" + self.url + "'"

        if (self.boE2e):
            delete += " AND BOE2E=1"
        else:
            delete += " AND BOE2E=0"

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

def createRepoBD():
    repoBD = RepoBD()
    return repoBD