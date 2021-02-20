#TFG (estudio CI/CD GitHub) - Programa de validación

#Importamos las librerías necesarias.
from github import Github
import configuracion as conf
import criterios
import auxiliares
import pandas as pd
import datetime
import random
import os

def exe():
    fRepos = 'repos.pickle'

    df = pd.DataFrame
    df2 = pd.DataFrame

    print(conf.Configuracion.fechaEjecucion + " - Iniciando proceso")

    try:
        # Generamos un token para consultar la API de GitHub a través de la librería.
        user = conf.Configuracion.user
        token = conf.Configuracion.token
        g = Github(user, token)

        if conf.Configuracion.generarListaRepos:
            print("Generando nueva lista de repositorios")
            # Obtenemos un objeto generador, encargado de realizar las búsquedas al iterar sobre él.

            query = """
                language:java 
                stars:>=500 
                forks:>=300 
                created:<2015-01-01 
                pushed:>2020-01-01
                archived:false
                is:public
            """

            print(conf.FiltrosQuery.query)
            generator = g.search_repositories(query=conf.FiltrosQuery.query)

            # Convertimos el generador en una lista de repositorios.
            repositories = list(generator)
            print("Total repos: %d" % len(repositories))

            # Guardamos la información de los repositorios recuperados en un archivo binario de Python.
            fRepos = 'repos_%s.pickle' % conf.Configuracion.fechaEjecucion
            auxiliares.generarPickle(fRepos, repositories)
            repositories = auxiliares.cargarRepositorios(fRepos)
        else:
            print("Utilizando el fichero " + fRepos + " para generar los repositorios")
            repositories = auxiliares.cargarRepositorios(fRepos)

        # Filtramos por el número de COMMITS.
        filtrar_commits = False

        MAX_COMMITS = 10000
        MIN_COMMITS = 1000
        filtered_repos = []

        if filtrar_commits:
            for repo in repositories:
                commits = repo.get_commits().totalCount
                if commits >= MIN_COMMITS and commits <= MAX_COMMITS:
                    filtered_repos.append(repo)
        else:
            for repo in repositories:
                filtered_repos.append(repo)

        print("Total projects: %d" % len(filtered_repos))

        # Imprimimos la lista de repositorios.
        auxiliares.imprimirListaRepositorios(filtered_repos)

        if conf.Configuracion.lapseExe:
            # EXCEL RESEARCH
            if os.path.exists("research.xlsx"):
                df = pd.read_excel("research.xlsx", index_col=0)
            else:
                # Generamos un nuevo DataFrame mediante la librería "pandas".
                df = auxiliares.generarDataFrame(filtered_repos)
            # EXCEL CONTADORES
            if os.path.exists("contadores.xlsx"):
                df2 = pd.read_excel("contadores.xlsx", index_col=0)
            else:
                # Generamos un nuevo DataFrame mediante la librería "pandas".
                df2 = auxiliares.generarDataFrameContadores()

            listaAux = filtered_repos[0:conf.Configuracion.N_LAPSE_REPOS-1]
            del filtered_repos[0:conf.Configuracion.N_LAPSE_REPOS-1]
            auxiliares.generarPickle(fRepos, filtered_repos)
        else:
            listaAux = []
            for r in filtered_repos:
                if r not in listaAux:
                    listaAux.append(r)

            if conf.Configuracion.randomizarListaRepos:
                # Seleccionamos N repositorios de manera aleatoria:
                lRandom = []
                while len(lRandom) < conf.Configuracion.N_RANDOM:
                    item = random.choice(listaAux)
                    if item not in lRandom:
                        lRandom.append(item)
                listaAux = lRandom
                print("Random projects: %d" % len(listaAux))

                # Guardamos la información de los repositorios randomizados en un archivo binario de Python.
                fRepos = 'random_repos_%s.pickle' % conf.Configuracion.fechaEjecucion
                auxiliares.generarPickle(fRepos, listaAux)
                listaAux = auxiliares.cargarRepositorios(fRepos)

                # Imprimimos la lista de repositorios
                auxiliares.imprimirListaRepositorios(listaAux)

            # Generamos nuevos DataFrames mediante la librería "pandas".
            df = auxiliares.generarDataFrame(listaAux)
            df2 = auxiliares.generarDataFrameContadores()

        if len(listaAux) > 0:
            if conf.Configuracion.buscarEnLocal:

                print("Nº repos que se van a clonar: " + str(len(listaAux)))
                # Clonamos en local los repositorios obtenidos:
                auxiliares.clonar1ListaRepo(listaAux)

                # Rellenamos la columna CommitID del DataFrame con los repositorios ya clonados
                auxiliares.actualizarDataFrameCommitID(listaAux, df)

                # Listamos los repositorios clonados
                reposEnLocal = os.listdir(conf.Configuracion.cRepositorios)

                # Aplicamos criterios
                print("Nº repos en local: " + str(len(reposEnLocal)))
                repos1 = criterios.recorrerRepositoriosLocal(reposEnLocal, criterios.Criterios.criterio1.value, df)
                repos2 = criterios.recorrerRepositoriosLocal(reposEnLocal, criterios.Criterios.criterio2.value, df)
                repos3 = criterios.recorrerRepositoriosLocal(reposEnLocal, criterios.Criterios.criterio3.value, df)
                repos4 = criterios.recorrerRepositoriosLocal(reposEnLocal, criterios.Criterios.criterio4.value, df)
                repos5 = criterios.recorrerRepositoriosLocal(reposEnLocal, criterios.Criterios.criterio5.value, df)
                repos6 = criterios.recorrerRepositoriosLocal(reposEnLocal, criterios.Criterios.criterio6.value, df)
                repos7 = criterios.recorrerRepositoriosLocal(reposEnLocal, criterios.Criterios.criterio7.value, df)
                repos8 = criterios.recorrerRepositoriosLocal(reposEnLocal, criterios.Criterios.criterio8.value, df)
                repos9 = criterios.recorrerRepositoriosLocal(reposEnLocal, criterios.Criterios.criterio9.value, df)
                repos10 = criterios.recorrerRepositoriosLocal(reposEnLocal, criterios.Criterios.criterio10.value, df)
                repos11 = criterios.recorrerRepositoriosLocal(reposEnLocal, criterios.Criterios.criterio11.value, df)
                repos12 = criterios.recorrerRepositoriosLocal(reposEnLocal, criterios.Criterios.criterio12.value, df)

                # Generar Zip de los repositorios
                auxiliares.generarZipRepos()

            else:
                # Aplicamos criterios:
                repos1_1 = criterios.buscarEnRaiz(listaAux, criterios.Criterios.criterio1.value, df)
                repos1_2 = criterios.buscarEnTests(listaAux, criterios.Criterios.criterio1.value, df)
                repos1_3 = criterios.buscarEnSrcTests(listaAux, criterios.Criterios.criterio1.value, df)
        else:
            print("No se han obtenido repositorios del fichero " + fRepos)

        # Transformar DataFrame a Excel/CSV
        auxiliares.generarEXCEL_CSV(df, "research", conf.Configuracion.doExcel, conf.Configuracion.doCsv)

        # Generar un DataFrame auxiliar con los contadores de los repositorios encontrados por cada criterio
        columna = "n_encontrados"

        # Inicializamos contadores
        nC1 = 0
        nC2 = 0
        nC3 = 0
        nC4 = 0
        nC5 = 0
        nC6 = 0
        nC7 = 0
        nC8 = 0
        nC9 = 0
        nC10 = 0
        nC11 = 0
        nC12 = 0

        if conf.Configuracion.buscarEnLocal:
            nC1 = len(repos1)
            nC2 = len(repos2)
            nC3 = len(repos3)
            nC4 = len(repos4)
            nC5 = len(repos5)
            nC6 = len(repos6)
            nC7 = len(repos7)
            nC8 = len(repos8)
            nC9 = len(repos9)
            nC10 = len(repos10)
            nC11 = len(repos11)
            nC12 = len(repos12)
        else:
            nC1 = len(repos1_1) + len(repos1_2) + len(repos1_3)

        # Actualizamos DataFrame de contadores
        df2.at[criterios.Criterios.criterio1.value, columna] += nC1
        df2.at[criterios.Criterios.criterio2.value, columna] += nC2
        df2.at[criterios.Criterios.criterio3.value, columna] += nC3
        df2.at[criterios.Criterios.criterio4.value, columna] += nC4
        df2.at[criterios.Criterios.criterio5.value, columna] += nC5
        df2.at[criterios.Criterios.criterio6.value, columna] += nC6
        df2.at[criterios.Criterios.criterio7.value, columna] += nC7
        df2.at[criterios.Criterios.criterio8.value, columna] += nC8
        df2.at[criterios.Criterios.criterio9.value, columna] += nC9
        df2.at[criterios.Criterios.criterio10.value, columna] += nC10
        df2.at[criterios.Criterios.criterio11.value, columna] += nC11
        df2.at[criterios.Criterios.criterio12.value, columna] += nC12
        df2.at["Totales", columna] += auxiliares.contarRepositoriosAlMenos1Criterio(df)

        # Transformar DataFrame a Excel/CSV
        auxiliares.generarEXCEL_CSV(df2, "contadores", conf.Configuracion.doExcel, conf.Configuracion.doCsv)

        # Clonamos repositorios:
        if conf.Configuracion.clonarRepositorios:
            lAux = []
            #lAux.append(repos1_1)
            auxiliares.clonarRepositorios(lAux)

        print(str(datetime.datetime.now())[0:19] + " - Proceso finalizado")
    except:
        print(str(datetime.datetime.now())[0:19] + " - ERROR INESPERADO")
        raise
        #FIN

# LLAMADA AL MÉTODO DE EJECUCIÓN
# exe()
