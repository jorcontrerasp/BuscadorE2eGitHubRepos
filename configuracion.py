import datetime

# CONFIGURACIÓN
class Configuracion():
    user = "userId"
    token = "userToken"
    fechaEjecucion = str(datetime.datetime.now())[0:19].replace(" ", "_")
    buscarEnLocal = True
    generarListaRepos = False
    randomizarListaRepos = True
    lapseExe = False
    clonarRepositorios = False
    doExcel = True
    doCsv = False
    N_RANDOM = 30
    N_LAPSE_REPOS = 20
    cRepositorios = "repositories/repositories_" + fechaEjecucion
    cLogs = "logs"

class FiltrosQuery():
    language = "java"
    stars = ">=500"
    forks = ">=300"
    created = "<2015-01-01"
    pushed = ">2020-01-01"
    archived = "false"
    qIs = "public"

    def getQueryIni(self):
        queryIni = "language:" + self.language + "\n" \
                + "stars:" + self.stars + "\n" \
                + "forks:" + self.forks + "\n" \
                + "created:" + self.created + "\n" \
                + "pushed:" + self.pushed + "\n" \
                + "archived:" + self.archived + "\n" \
                + "is:" + self.qIs + "\n"
        return queryIni