import datetime
import pymysql
import pymysql.cursors
import executeQuery

# CONFIGURACIÓN
class Configuracion():
    user = "userId"
    token = "userToken"
    fechaEjecucion = str(datetime.datetime.now())[0:19].replace(" ", "_").replace(":", "h", 1).replace(":", "m", 1) + "s"
    buscarEnLocal = True
    generarListaRepos = True
    randomizarListaRepos = True
    lapseExe = False
    clonarRepositorios = False
    doExcel = True
    doCsv = False
    actualizarBD = True
    N_RANDOM = 30
    N_LAPSE_REPOS = 20
    REPO_SIZE_LIMIT = 10000000
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
    def getUserBD(self):
        return self.getConfiguracion("CREDENCIALES", "user")

config = Configuracion()