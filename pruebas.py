#TFG (estudio CI/CD GitHub) - PRUEBAS
import configuracion as conf
import auxiliares
import criterios
import datetime
import os
from github import Github

class RepoPruebas():
    organizacion = ""
    nombre = ""

def ejecutaPrueba():
    print(conf.Configuracion.fechaEjecucion + " - Iniciando prueba")

    # Generamos un token para consultar la API de GitHub a través de la librería.
    user = conf.Configuracion.user
    token = conf.Configuracion.token
    g = Github(user, token)

    repo = g.get_repo(RepoPruebas.nombre)
    filteredRepos = [repo]

    auxiliares.clonar1ListaRepo(filteredRepos)

    reposEnLocal = os.listdir(conf.Configuracion.carpetaRepositorios)

    df = auxiliares.generarDataFrame(filteredRepos)
    rAux = criterios.recorrerRepositoriosLocal(reposEnLocal, criterios.Criterios.criterio8.value, df)

    auxiliares.generarEXCEL_CSV(df, "research", conf.Configuracion.doExcel, conf.Configuracion.doCsv)

    date = str(datetime.datetime.now())[0:19]
    print(date + " - Prueba finalizada")

# LLAMADA AL MÉTODO DE EJECUCIÓN
# ejecutaPrueba()
