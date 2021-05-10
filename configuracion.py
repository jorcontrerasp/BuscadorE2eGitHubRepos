import datetime
import auxiliares

# CONFIGURACIÓN
class Configuracion():
    user = None
    token = None
    fechaEjecucion = str(datetime.datetime.now())[0:19].replace(" ", "_").replace(":", "h", 1).replace(":", "m", 1) + "s"
    actualizarBD = None
    buscarEnLocal = None
    generarListaRepos = None
    randomizarListaRepos = None
    lapseExe = None
    clonarRepositorios = None
    doExcel = None
    doCsv = None
    escribirEnLog = None
    N_RANDOM = -1
    N_LAPSE_REPOS = -1
    REPO_SIZE_LIMIT = -1
    ITEMS_FOUND_LIMIT = -1
    cRepositorios = "repositories/repositories_" + fechaEjecucion
    cLogs = "logs"
    cResearch = "research/research_" + fechaEjecucion
    cContadores = "contadores/contadores_" + fechaEjecucion
    idBusqueda = -1

    def __init__(self):
        self.inicializaConfiguracion()

    def inicializaConfiguracion(self):
        self.user = auxiliares.getConfiguracion("CREDENCIALES", "user")
        self.token = auxiliares.getConfiguracion("CREDENCIALES", "token")
        self.actualizarBD = auxiliares.getConfiguracion("SEARCH_PARAM", "actualizarBD")
        self.buscarEnLocal = auxiliares.getConfiguracion("SEARCH_PARAM", "buscarEnLocal")
        self.generarListaRepos = auxiliares.getConfiguracion("SEARCH_PARAM", "generarListaRepos")
        self.randomizarListaRepos = auxiliares.getConfiguracion("SEARCH_PARAM", "randomizarListaRepos")
        self.lapseExe = auxiliares.getConfiguracion("SEARCH_PARAM", "lapseExe")
        self.clonarRepositorios = auxiliares.getConfiguracion("SEARCH_PARAM", "clonarRepositorios")
        self.doExcel = auxiliares.getConfiguracion("SEARCH_PARAM", "doExcel")
        self.doCsv = auxiliares.getConfiguracion("SEARCH_PARAM", "doCsv")
        self.escribirEnLog = auxiliares.getConfiguracion("SEARCH_PARAM", "escribirEnLog")
        self.N_RANDOM = auxiliares.getConfiguracion("SEARCH_PARAM", "N_RANDOM")
        self.N_LAPSE_REPOS = auxiliares.getConfiguracion("SEARCH_PARAM", "N_LAPSE_REPOS")
        self.REPO_SIZE_LIMIT = auxiliares.getConfiguracion("SEARCH_PARAM", "REPO_SIZE_LIMIT")
        self.ITEMS_FOUND_LIMIT = auxiliares.getConfiguracion("SEARCH_PARAM", "ITEMS_FOUND_LIMIT")

    # GETTER & SETTER
    def getUser(self):
        return self.user

    def getUserSql(self):
        return auxiliares.getConfiguracion("CREDENCIALES", "user")

    def setUser(self, user):
        self.user = user

    def getToken(self):
        return self.token

    def getTokenSql(self):
        return auxiliares.getConfiguracion("CREDENCIALES", "token")

    def setToken(self, token):
        self.token = token

    def getBuscarEnLocal(self):
        return self.buscarEnLocal

    def getBuscarEnLocalSql(self):
        return auxiliares.getConfiguracion("SEARCH_PARAM", "buscarEnLocal")

    def setBuscarEnLocal(self, buscarEnLocal):
        self.buscarEnLocal = buscarEnLocal

    def getGenerarListaRepos(self):
        return self.generarListaRepos

    def getGenerarListaReposSql(self):
        return auxiliares.getConfiguracion("SEARCH_PARAM", "generarListaRepos")

    def setGenerarListaRepos(self, generarListaRepos):
        self.generarListaRepos = generarListaRepos

    def getRandomizarListaRepos(self):
        return self.randomizarListaRepos

    def getRandomizarListaReposSql(self):
        return auxiliares.getConfiguracion("SEARCH_PARAM", "randomizarListaRepos")

    def setRandomizarListaRepos(self, randomizarListaRepos):
        self.randomizarListaRepos = randomizarListaRepos

    def getLapseExe(self):
        return self.lapseExe

    def getLapseExeSql(self):
        return auxiliares.getConfiguracion("SEARCH_PARAM", "lapseExe")

    def setLapseExe(self, lapseExe):
        self.lapseExe = lapseExe

    def getClonarRepositorios(self):
        return self.clonarRepositorios

    def getClonarRepositoriosSql(self):
        return auxiliares.getConfiguracion("SEARCH_PARAM", "clonarRepositorios")

    def setClonarRepositorios(self, clonarRepositorios):
        self.clonarRepositorios = clonarRepositorios

    def getDoExcel(self):
        return self.doExcel

    def getDoExcelSql(self):
        return auxiliares.getConfiguracion("SEARCH_PARAM", "doExcel")

    def setDoExcel(self, doExcel):
        self.doExcel = doExcel

    def getDoCsv(self):
        return self.doCsv

    def getDoCsvSql(self):
        return auxiliares.getConfiguracion("SEARCH_PARAM", "doCsv")

    def setDoCsv(self, doCsv):
        self.doCsv = doCsv

    def getActualizarBD(self):
        return self.actualizarBD

    def getActualizarBDSql(self):
        return auxiliares.getConfiguracion("SEARCH_PARAM", "actualizarBD")

    def setActualizarBD(self, actualizarBD):
        self.actualizarBD = actualizarBD

    def getEscribirEnLog(self):
        return self.escribirEnLog

    def getEscribirEnLogSql(self):
        return auxiliares.getConfiguracion("SEARCH_PARAM", "escribirEnLog")

    def setEscribirEnLog(self, escribirEnLog):
        self.escribirEnLog = escribirEnLog

config = Configuracion()