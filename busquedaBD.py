import configuracion as conf
import auxiliares

class BusquedaBD:
    idBusqueda = -1
    lenguaje = ""
    stars = ""
    forks = ""
    created = ""
    pushed = ""
    archived = False
    public = True
    research = None
    contadores = None
    tstbd = ""

    def __init__(self):
        self.idBusqueda = -1
        self.lenguaje = ""
        self.stars = ""
        self.forks = ""
        self.created = ""
        self.pushed = ""
        self.archived = False
        self.public = True
        self.research = None
        self.contadores = None
        self.tstbd = conf.config.fechaEjecucion

    def getInsert(self):

        campos = ""
        values = ""

        if(self.idBusqueda > 0):
            campos += "IDBUSQUEDA,"
            values += str(self.idBusqueda) + ","

        if (len(str(self.lenguaje)) > 0):
            campos += "LENGUAJE,"
            values += "'" + str(self.lenguaje) + "',"

        if (len(str(self.stars)) > 0):
            campos += "STARS,"
            values += "'" + str(self.stars) + "',"

        if (len(str(self.forks)) > 0):
            campos += "FORKS,"
            values += "'" + str(self.forks) + "',"

        if (len(str(self.created)) > 0):
            campos += "CREATED,"
            values += "'" + str(self.created) + "',"

        if (len(str(self.pushed)) > 0):
            campos += "PUSHED,"
            values += "'" + str(self.pushed) + "',"

        if (self.archived):
            campos += "ARCHIVED,"
            values += "1" + ","
        else:
            campos += "ARCHIVED,"
            values += "0" + ","

        if (self.public):
            campos += "PUBLIC,"
            values += "1" + ","
        else:
            campos += "PUBLIC,"
            values += "0" + ","

        if (len(str(self.tstbd)) > 0):
            campos += "TSTBD,"
            values += "'" + str(self.tstbd) + "',"

        campos = campos[0:len(campos) - 1]
        values = values[0:len(values) - 1]
        insert = "INSERT INTO BD_D_BUSQUEDA (" + campos + ") VALUES (" + values + ")"

        insert += ";"

        return insert

    def getInsertParam(self):
        insertSql = "INSERT INTO BD_D_BUSQUEDA (lenguaje, stars, forks, created, pushed, archived, public, research, contadores, tstbd) " \
                 "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"

        try:
            researchBD = auxiliares.convertToBinaryData(self.research)
        except:
            researchBD = None

        try:
            contadoresBD = auxiliares.convertToBinaryData(self.contadores)
        except:
            contadoresBD = None

        if (self.archived):
            archivedBD = 1
        else:
            archivedBD = 0

        if (self.public):
            publicBD = 1
        else:
            publicBD = 0

        insertBlobTuple = (self.lenguaje, self.stars, self.forks, self.created, self.pushed,
                           archivedBD, publicBD, researchBD, contadoresBD, self.tstbd)

        insert = (insertSql, insertBlobTuple)
        return insert

    def getUpdate(self):
        if(self.idBusqueda == -1 or self.idBusqueda == 0):
            print("El objeto busquedaBD no tiene IDBUSQUEDA. No se puede actualizar.")
            return ""

        values = ""
        if (len(str(self.lenguaje)) > 0):
            values += "LENGUAJE='"  + str(self.lenguaje) + "',"

        if (len(str(self.stars)) > 0):
            values += "STARS='" + str(self.stars) + "',"

        if (len(str(self.forks)) > 0):
            values += "FORKS='" + str(self.forks) + "',"

        if (len(str(self.created)) > 0):
            values += "CREATED='" + str(self.created) + "',"

        if (len(str(self.pushed)) > 0):
            values += "PUSHED='" + str(self.pushed) + "',"

        if (self.archived):
            values += "ARCHIVED=1,"
        else:
            values += "ARCHIVED=0,"

        if (self.public):
            values += "PUBLIC=1,"
        else:
            values += "PUBLIC=0,"

        if (len(str(self.tstbd)) > 0):
            values += "TSTBD='" + str(self.tstbd) + "',"

        values = values[0:len(values) - 1]
        update = "UPDATE BD_D_BUSQUEDA SET " + values + " WHERE IDBUSQUEDA = " + str(self.idBusqueda)

        update += ";"

        return update

    def getUpdateParam(self):
        if(self.idBusqueda == -1 or self.idBusqueda == 0):
            print("El objeto busquedaBD no tiene IDBUSQUEDA. No se puede actualizar.")
            return ""

        updateBlobTupleAux = []
        values = ""
        if (len(str(self.lenguaje)) > 0):
            values += "LENGUAJE=%s,"
            updateBlobTupleAux.append(self.lenguaje)

        if (len(str(self.stars)) > 0):
            values += "STARS=%s,"
            updateBlobTupleAux.append(self.stars)

        if (len(str(self.forks)) > 0):
            values += "FORKS=%s,"
            updateBlobTupleAux.append(self.forks)

        if (len(str(self.created)) > 0):
            values += "CREATED=%s,"
            updateBlobTupleAux.append(self.created)

        if (len(str(self.pushed)) > 0):
            values += "PUSHED=%s,"
            updateBlobTupleAux.append(self.pushed)

        if (self.archived):
            values += "ARCHIVED=1,"
        else:
            values += "ARCHIVED=0,"

        if (self.public):
            values += "PUBLIC=1,"
        else:
            values += "PUBLIC=0,"

        try:
            researchBD = auxiliares.convertToBinaryData(self.research)
            values += "RESEARCH=%s,"
            updateBlobTupleAux.append(researchBD)
        except:
            researchBD = None

        try:
            contadoresBD = auxiliares.convertToBinaryData(self.contadores)
            values += "CONTADORES=%s,"
            updateBlobTupleAux.append(contadoresBD)
        except:
            contadoresBD = None

        if (len(str(self.tstbd)) > 0):
            values += "TSTBD=%s,"
            updateBlobTupleAux.append(self.tstbd)


        values = values[0:len(values) - 1]
        update = "UPDATE BD_D_BUSQUEDA SET " + values + " WHERE IDBUSQUEDA = %s"
        updateBlobTupleAux.append(self.idBusqueda)

        updateBlobTuple = tuple(updateBlobTupleAux)

        return (update, updateBlobTuple)

    def getFiltro(self):
        select = "SELECT * FROM BD_D_BUSQUEDA WHERE 1=1"

        if (self.idBusqueda > 0):
            select += " AND IDBUSQUEDA=" + str(self.idBusqueda)

        if (len(str(self.lenguaje)) > 0):
            select += " AND LENGUAJE='" + str(self.lenguaje) + "'"

        if (len(str(self.stars)) > 0):
            select += " AND STARS='" + str(self.stars) + "'"

        if (len(str(self.forks)) > 0):
            select += " AND FORKS='" + str(self.forks) + "'"

        if (len(str(self.created)) > 0):
            select += " AND CREATED='" + str(self.created) + "'"

        if (len(str(self.pushed)) > 0):
            select += " AND PUSHED='" + str(self.pushed) + "'"

        if (self.archived):
            select += " AND ARCHIVED=1"
        else:
            select += " AND ARCHIVED=0"

        if (self.public):
            select += " AND PUBLIC=1"
        else:
            select += " AND PUBLIC=0"

        if (len(str(self.tstbd)) > 0):
            select += " AND TSTBD='" + str(self.tstbd) + "'"

        select += ";"

        return select

    def getDelete(self):
        delete = "DELETE BD_D_BUSQUEDA WHERE 1=1"

        if (self.idBusqueda > 0):
            delete += " AND IDBUSQUEDA=" + str(self.idBusqueda)

        if (len(str(self.lenguaje)) > 0):
            delete += " AND LENGUAJE='" + str(self.lenguaje) + "'"

        if (len(str(self.stars)) > 0):
            delete += " AND STARS='" + str(self.stars) + "'"

        if (len(str(self.forks)) > 0):
            delete += " AND FORKS='" + str(self.forks) + "'"

        if (len(str(self.created)) > 0):
            delete += " AND CREATED='" + str(self.created) + "'"

        if (len(str(self.pushed)) > 0):
            delete += " AND PUSHED='" + str(self.pushed) + "'"

        if (self.archived):
            delete += " AND ARCHIVED=1"
        else:
            delete += " AND ARCHIVED=0"

        if (self.public):
            delete += " AND PUBLIC=1"
        else:
            delete += " AND PUBLIC=0"

        if (len(str(self.tstbd)) > 0):
            delete += " AND TSTBD='" + str(self.tstbd) + "'"

        delete += ";"

        return delete

    # GETTER & SETTER
    def getIdBusqueda(self):
        return self.idBusqueda

    def setIdBusqueda(self, idBusqueda):
        self.idBusqueda = idBusqueda

    def getLenguaje(self):
        return self.lenguaje

    def setLenguaje(self, lenguaje):
        self.lenguaje = lenguaje

    def getStars(self):
        return self.stars

    def setStars(self, stars):
        self.stars = stars

    def getForks(self):
        return self.forks

    def setForks(self, forks):
        self.forks = forks

    def getCreated(self):
        return self.created

    def setCreated(self, created):
        self.created = created

    def getPushed(self):
        return self.pushed

    def setPushed(self, pushed):
        self.pushed = pushed

    def getArchived(self):
        return self.archived

    def setArchived(self, archived):
        self.archived = archived

    def getPublic(self):
        return self.public

    def setPublic(self, public):
        self.public = public

    def getResearch(self):
        return self.research

    def setResearch(self, research):
        self.research = research

    def getContadores(self):
        return self.contadores

    def setContadores(self, contadores):
        self.contadores = contadores

    def getTstbd(self):
        return self.tstbd

    def setTstbd(self, tstbd):
        self.tstbd = tstbd

def createBusquedaBD():
    busquedaBD = BusquedaBD()
    return busquedaBD