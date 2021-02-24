import datetime

# CONFIGURACIÓN
class Configuracion():
    user = "jorcontrerasp"
    token = "6dc204e26cd895a66d5ed1ccb478d60c0d15085e"
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
    cResearch = "research/research_" + fechaEjecucion
    cContadores = "contadores/contadores_" + fechaEjecucion

class FiltrosQuery():
    language = "java"
    stars = ">=500"
    forks = ">=300"
    created = "<2015-01-01"
    pushed = ">2020-01-01"
    archived = "false"
    qIs = "public"

    def getQueryIni(self):
        queryIni = ""
        if len(self.language)>0:
            queryIni += "language:" + self.language + "\n"

        if len(self.stars)>0:
            queryIni += "stars:" + self.stars + "\n"

        if len(self.forks)>0:
            queryIni += "forks:" + self.forks + "\n"

        if len(self.created)>0:
            queryIni += "created:" + self.created + "\n"

        if len(self.pushed)>0:
            queryIni += "pushed:" + self.pushed + "\n"

        if len(self.archived)>0:
            queryIni += "archived:" + self.archived + "\n"

        if len(self.qIs)>0:
            queryIni += "is:" + self.qIs + "\n"

        return queryIni