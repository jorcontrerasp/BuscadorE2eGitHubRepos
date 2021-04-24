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
    print(conf.config.fechaEjecucion + " - Iniciando prueba")

    # Generamos un token para consultar la API de GitHub a través de la librería.
    user = conf.config.user
    token = conf.config.token
    g = Github(user, token)

    auxiliares.crearCarpetasLocal()

    repo = g.get_repo(RepoPruebas.organizacion + "/" + RepoPruebas.nombre)
    filteredRepos = [repo]

    auxiliares.clonar1ListaRepo(filteredRepos)

    reposEnLocal = os.listdir(conf.config.cRepositorios)

    df = auxiliares.generarDataFrame(filteredRepos)

    # Aplicamos criterios
    print("Nº repos en local: " + str(len(reposEnLocal)))
    repos1 = criterios.recorrerRepositoriosLocal(reposEnLocal, criterios.Criterios.criterio1.value, df)
    repos3 = criterios.recorrerRepositoriosLocal(reposEnLocal, criterios.Criterios.criterio3.value, df)
    repos5 = criterios.recorrerRepositoriosLocal(reposEnLocal, criterios.Criterios.criterio5.value, df)
    repos10 = criterios.recorrerRepositoriosLocal(reposEnLocal, criterios.Criterios.criterio10.value, df)

    auxiliares.generarEXCEL_CSV(df, "research", conf.config.doExcel, conf.config.doCsv)

    date = str(datetime.datetime.now())[0:19]
    print(date + " - Prueba finalizada")

# LLAMADA AL MÉTODO DE EJECUCIÓN
# ejecutaPrueba()
