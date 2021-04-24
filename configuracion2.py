import datetime
import pymysql
import pymysql.cursors
import executeQuery

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

user = getConfiguracion("CREDENCIALES", "user")
token = getConfiguracion("CREDENCIALES", "token")
fechaEjecucion = str(datetime.datetime.now())[0:19].replace(" ", "_").replace(":", "h", 1).replace(":", "m", 1) + "s"
buscarEnLocal = getConfiguracion("SEARCH_PARAM", "buscarEnLocal")
generarListaRepos = getConfiguracion("SEARCH_PARAM", "generarListaRepos")
randomizarListaRepos = getConfiguracion("SEARCH_PARAM", "randomizarListaRepos")
lapseExe = getConfiguracion("SEARCH_PARAM", "lapseExe")
clonarRepositorios = getConfiguracion("SEARCH_PARAM", "clonarRepositorios")
doExcel = getConfiguracion("SEARCH_PARAM", "doExcel")
doCsv = getConfiguracion("SEARCH_PARAM", "doCsv")
actualizarBD = getConfiguracion("SEARCH_PARAM", "actualizarBD")
N_RANDOM = getConfiguracion("SEARCH_PARAM", "N_RANDOM")
N_LAPSE_REPOS = getConfiguracion("SEARCH_PARAM", "N_LAPSE_REPOS")
REPO_SIZE_LIMIT = getConfiguracion("SEARCH_PARAM", "REPO_SIZE_LIMIT")
cRepositorios = "repositories/repositories_" + fechaEjecucion
cLogs = "logs"
cResearch = "research/research_" + fechaEjecucion
cContadores = "contadores/contadores_" + fechaEjecucion
idBusqueda = -1