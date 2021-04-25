import datetime
import executeQuery

# CONFIGURACIÓN
class Configuracion():
    user = None
    token = None
    fechaEjecucion = str(datetime.datetime.now())[0:19].replace(" ", "_").replace(":", "h", 1).replace(":", "m", 1) + "s"
    buscarEnLocal = None
    generarListaRepos = None
    randomizarListaRepos = None
    lapseExe = None
    clonarRepositorios = None
    doExcel = None
    doCsv = None
    actualizarBD = None
    N_RANDOM = -1
    N_LAPSE_REPOS = -1
    REPO_SIZE_LIMIT = -1
    cRepositorios = "repositories/repositories_" + fechaEjecucion
    cLogs = "logs"
    cResearch = "research/research_" + fechaEjecucion
    cContadores = "contadores/contadores_" + fechaEjecucion
    idBusqueda = -1

    def __init__(self):
        self.inicializaConfiguracion()

    def inicializaConfiguracion(self):
        self.user = self.getConfiguracion("CREDENCIALES", "user")
        self.token = self.getConfiguracion("CREDENCIALES", "token")
        self.buscarEnLocal = self.getConfiguracion("SEARCH_PARAM", "buscarEnLocal")
        self.generarListaRepos = self.getConfiguracion("SEARCH_PARAM", "generarListaRepos")
        self.randomizarListaRepos = self.getConfiguracion("SEARCH_PARAM", "randomizarListaRepos")
        self.lapseExe = self.getConfiguracion("SEARCH_PARAM", "lapseExe")
        self.clonarRepositorios = self.getConfiguracion("SEARCH_PARAM", "clonarRepositorios")
        self.doExcel = self.getConfiguracion("SEARCH_PARAM", "doExcel")
        self.doCsv = self.getConfiguracion("SEARCH_PARAM", "doCsv")
        self.actualizarBD = self.getConfiguracion("SEARCH_PARAM", "actualizarBD")
        self.N_RANDOM = self.getConfiguracion("SEARCH_PARAM", "N_RANDOM")
        self.N_LAPSE_REPOS = self.getConfiguracion("SEARCH_PARAM", "N_LAPSE_REPOS")
        self.REPO_SIZE_LIMIT = self.getConfiguracion("SEARCH_PARAM", "REPO_SIZE_LIMIT")

    def getConfiguracion(self, codigo, campo):
        query = "Select valor from BD_D_CONFIGURACION WHERE IDCONFIGURACIONTIPO IN(Select IDCONFIGURACIONTIPO FROM BD_D_CONFIGURACIONTIPO WHERE CODIGO = :codigo) AND campo = :campo;"
        query = query.replace(":codigo", "'" + codigo + "'")
        query = query.replace(":campo", "'" + campo + "'")

        resultado = executeQuery.execute(query)

        r = None
        valor = resultado[0]["valor"]
        if valor == 'True':
            r = True
        elif valor == 'False':
            r = False
        elif valor.isdigit():
            r = int(valor)
        else:
            r = valor

        return r

    # GETTER & SETTER
    def getUser(self):
        return self.user

    def getUserSql(self):
        return self.getConfiguracion("CREDENCIALES", "user")

    def setUser(self, user):
        self.user = user

    def getToken(self):
        return self.token

    def getTokenSql(self):
        return self.getConfiguracion("CREDENCIALES", "token")

    def setToken(self, token):
        self.token = token

    def getBuscarEnLocal(self):
        return self.buscarEnLocal

    def getBuscarEnLocalSql(self):
        return self.getConfiguracion("SEARCH_PARAM", "buscarEnLocal")

    def setBuscarEnLocal(self, buscarEnLocal):
        self.buscarEnLocal = buscarEnLocal

    def getGenerarListaRepos(self):
        return self.generarListaRepos

    def getGenerarListaReposSql(self):
        return self.getConfiguracion("SEARCH_PARAM", "generarListaRepos")

    def setGenerarListaRepos(self, generarListaRepos):
        self.generarListaRepos = generarListaRepos

    def getRandomizarListaRepos(self):
        return self.randomizarListaRepos

    def getRandomizarListaReposSql(self):
        return self.getConfiguracion("SEARCH_PARAM", "randomizarListaRepos")

    def setRandomizarListaRepos(self, randomizarListaRepos):
        self.randomizarListaRepos = randomizarListaRepos

    def getLapseExe(self):
        return self.lapseExe

    def getLapseExeSql(self):
        return self.getConfiguracion("SEARCH_PARAM", "lapseExe")

    def setLapseExe(self, lapseExe):
        self.lapseExe = lapseExe

    def getClonarRepositorios(self):
        return self.clonarRepositorios

    def getClonarRepositoriosSql(self):
        return self.getConfiguracion("SEARCH_PARAM", "clonarRepositorios")

    def setClonarRepositorios(self, clonarRepositorios):
        self.clonarRepositorios = clonarRepositorios

    def getDoExcel(self):
        return self.doExcel

    def getDoExcelSql(self):
        return self.getConfiguracion("SEARCH_PARAM", "doExcel")

    def setDoExcel(self, doExcel):
        self.doExcel = doExcel

    def getDoCsv(self):
        return self.doCsv

    def getDoCsvSql(self):
        return self.getConfiguracion("SEARCH_PARAM", "doCsv")

    def setDoCsv(self, doCsv):
        self.doCsv = doCsv

    def getActualizarBD(self):
        return self.actualizarBD

    def getActualizarBDSql(self):
        return self.getConfiguracion("SEARCH_PARAM", "actualizarBD")

    def setActualizarBD(self, actualizarBD):
        self.actualizarBD = actualizarBD

config = Configuracion()