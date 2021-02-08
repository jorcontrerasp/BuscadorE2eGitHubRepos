import datetime

# CONFIGURACIÓN
class Configuracion():
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
    carpetaRepositorios = "repositories/repositories_" + fechaEjecucion