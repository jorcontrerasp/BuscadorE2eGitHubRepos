#TFG (estudio CI/CD GitHub) - PRUEBAS
from github.GithubException import UnknownObjectException
import configuracion as conf
import auxiliares
import criterios
import datetime
import os
import pandas as pd
from github import Github
import github

class RepoPruebas():
    organizacion = ""
    nombre = ""

def ejecutaPrueba():
    print(conf.config.fechaEjecucion + " - Iniciando proceso")

    continuar = True

    # Generamos un token para consultar la API de GitHub a través de la librería.
    user = conf.config.user
    token = conf.config.token
    g = Github(user, token)

    try:
        repo = g.get_repo(RepoPruebas.organizacion + "/" + RepoPruebas.nombre)
    except UnknownObjectException as e:
        print("El repositorio " + RepoPruebas.organizacion + "/" + RepoPruebas.nombre + " no existe en GitHub: " + str(e))
        continuar = False

    if continuar:
        auxiliares.crearCarpetasLocal()

        filteredRepos = [repo]

        df = auxiliares.generarDataFrame(filteredRepos)
        df2 = auxiliares.generarDataFrameContadores()

        # Clonar
        auxiliares.clonar1ListaRepo(filteredRepos)

        # Actualizar CommitID
        auxiliares.actualizarDataFrameCommitID(filteredRepos, df)

        reposEnLocal = os.listdir(conf.config.cRepositorios)

        # Aplicamos criterios
        print("Nº repos en local: " + str(len(reposEnLocal)))
        lReposEncontrados = criterios.recorrerRepositoriosLocal(reposEnLocal, df, df2)

        auxiliares.generarEXCEL_CSV(df, "research", conf.config.doExcel, conf.config.doCsv)
    else:
        print("No se ha podido continuar con la ejecución de la prueba.")

    date = str(datetime.datetime.now())[0:19]
    print(date + " - Proceso finalizado")

# LLAMADA AL MÉTODO DE EJECUCIÓN
# ejecutaPrueba()
