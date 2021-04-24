#TFG (estudio CI/CD GitHub) - Programa de validación

#Importamos las librerías necesarias.
import github
from github import Github
import configuracion as conf
import criterios
import auxiliares
import pandas as pd
import datetime
import random
import os
import busquedaBD

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

            queryConf = conf.FiltrosQuery.getQueryIni(self=conf.FiltrosQuery)
            fQueryInicial = "query-inicial_" + conf.Configuracion.fechaEjecucion + ".txt"
            f = open(fQueryInicial, "w")
            f.write("QUERY INICIAL:")
            f.write("\n")
            f.write(queryConf)
            generator = g.search_repositories(query=queryConf)

            # Convertimos el generador en una lista de repositorios.
            repositories = list(generator)
            print("Total repos: %d" % len(repositories))

            # Guardamos la información de los repositorios recuperados en un archivo binario de Python.
            fRepos = 'repos_%s.pickle' % conf.Configuracion.fechaEjecucion
            auxiliares.generarPickle(fRepos, repositories)
            repositories = auxiliares.cargarRepositorios(fRepos)

            busqueda = busquedaBD.createBusquedaBD()
            busqueda.setLenguaje(conf.FiltrosQuery.language)
            busqueda.setStars(conf.FiltrosQuery.stars)
            busqueda.setForks(conf.FiltrosQuery.forks)
            busqueda.setCreated(conf.FiltrosQuery.created)
            busqueda.setPushed(conf.FiltrosQuery.pushed)
            busqueda.setArchived(conf.FiltrosQuery.archived)
            busqueda.setPublic(conf.FiltrosQuery.qIs)
            idBusqueda = auxiliares.guardarBusquedaBD(busqueda)
            conf.Configuracion.idBusqueda = idBusqueda

        else:
            print("Utilizando el fichero " + fRepos + " para generar los repositorios")
            if os.path.exists(fRepos):
                repositories = auxiliares.cargarRepositorios(fRepos)
            else:
                raise Exception("No se ha encontrado el fichero pickle en la raíz del proyecto.")

        # Filtramos por el número de COMMITS.
        filtrar_commits = False

        MAX_COMMITS = 10000
        MIN_COMMITS = 1000
        filteredRepos = []

        if filtrar_commits:
            for repo in repositories:
                commits = repo.get_commits().totalCount
                if commits >= MIN_COMMITS and commits <= MAX_COMMITS:
                    filteredRepos.append(repo)
        else:
            for repo in repositories:
                filteredRepos.append(repo)

        tProjects = len(filteredRepos)
        print("Total projects: %d" % tProjects)

        if tProjects == 0 \
                and not os.path.exists("tmp-research.xlsx") \
                and not os.path.exists("tmp-contadores.xlsx"):
            raise Exception("El total de proyectos a analizar no puede ser 0. Revise el fichero pickle o genere uno nuevo.")

        # Imprimimos la lista de repositorios.
        auxiliares.imprimirListaRepositorios(filteredRepos)

        auxiliares.crearCarpetasLocal()

        if conf.Configuracion.lapseExe:
            # EXCEL RESEARCH
            if os.path.exists("tmp-research.xlsx"):
                df = pd.read_excel("tmp-research.xlsx", index_col=0)
            else:
                # Generamos un nuevo DataFrame mediante la librería "pandas".
                df = auxiliares.generarDataFrame(filteredRepos)
            # EXCEL CONTADORES
            if os.path.exists("tmp-contadores.xlsx"):
                df2 = pd.read_excel("tmp-contadores.xlsx", index_col=0)
            else:
                # Generamos un nuevo DataFrame mediante la librería "pandas".
                df2 = auxiliares.generarDataFrameContadores()

            listaAux = filteredRepos[0:conf.Configuracion.N_LAPSE_REPOS]
            del filteredRepos[0:conf.Configuracion.N_LAPSE_REPOS]
            auxiliares.generarPickle(fRepos, filteredRepos)
        else:
            listaAux = []
            for r in filteredRepos:
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

        continuar = True
        lReposEncontrados = []
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
                lReposEncontrados = criterios.recorrerRepositoriosLocal(reposEnLocal, df, df2)

                # Generar Zip de los repositorios
                auxiliares.generarZipRepos()

            else:
                # Aplicamos criterios:
                lReposEncontrados = criterios.busquedaGitHubApiRepos(listaAux, df, df2)

            print("Nº de repos encontrados: " + str(len(lReposEncontrados)))
        else:
            print("No se han obtenido repositorios del fichero " + fRepos)
            auxiliares.generarEXCEL_CSV(df, conf.Configuracion.cResearch,
                                        conf.Configuracion.doExcel,conf.Configuracion.doCsv)
            auxiliares.generarEXCEL_CSV(df2, conf.Configuracion.cContadores,
                                        conf.Configuracion.doExcel, conf.Configuracion.doCsv)
            os.remove("tmp-research.xlsx")
            print("Fichero tmp-research.xlsx eliminado")
            os.remove("tmp-contadores.xlsx")
            print("Fichero tmp-contadores.xlsx eliminado")

            # Guardamos los ficheros excel en BD.
            if conf.Configuracion.actualizarBD:
                busqueda = busquedaBD.createBusquedaBD()
                busqueda.setIdBusqueda(conf.Configuracion.idBusqueda)
                busqueda.setResearch(conf.Configuracion.cResearch + ".xlsx")
                busqueda.setContadores(conf.Configuracion.cContadores + ".xlsx")
                if conf.Configuracion.randomizarListaRepos:
                    busqueda.setFRepos('random_repos_%s.pickle' % conf.Configuracion.fechaEjecucion)
                else:
                    busqueda.setFRepos('repos_%s.pickle' % conf.Configuracion.fechaEjecucion)
                auxiliares.guardarBusquedaBD(busqueda)

            continuar = False

        if continuar:
            # Transformar DataFrame a Excel/CSV
            if conf.Configuracion.lapseExe:
                auxiliares.generarEXCEL_CSV(df, "tmp-research", conf.Configuracion.doExcel, conf.Configuracion.doCsv)
                auxiliares.generarEXCEL_CSV(df2, "tmp-contadores", conf.Configuracion.doExcel, conf.Configuracion.doCsv)
            else:
                auxiliares.generarEXCEL_CSV(df, conf.Configuracion.cResearch, conf.Configuracion.doExcel, conf.Configuracion.doCsv)
                auxiliares.generarEXCEL_CSV(df2, conf.Configuracion.cContadores, conf.Configuracion.doExcel,
                                            conf.Configuracion.doCsv)

                # Guardamos los ficheros excel en BD.
                if conf.Configuracion.actualizarBD:
                    busqueda = busquedaBD.createBusquedaBD()
                    busqueda.setIdBusqueda(conf.Configuracion.idBusqueda)
                    busqueda.setResearch(conf.Configuracion.cResearch + ".xlsx")
                    busqueda.setContadores(conf.Configuracion.cContadores + ".xlsx")
                    if conf.Configuracion.randomizarListaRepos:
                        busqueda.setFRepos('random_repos_%s.pickle' % conf.Configuracion.fechaEjecucion)
                    else:
                        busqueda.setFRepos('repos_%s.pickle' % conf.Configuracion.fechaEjecucion)
                    auxiliares.guardarBusquedaBD(busqueda)

            # Clonamos repositorios:
            if conf.Configuracion.clonarRepositorios:
                lAux = []
                lAux.append(lReposEncontrados)
                auxiliares.clonarRepositorios(lAux)

        print(str(datetime.datetime.now())[0:19] + " - Proceso finalizado")
    except:
        print(str(datetime.datetime.now())[0:19] + " - ERROR INESPERADO")
        raise
        #FIN

# LLAMADA AL MÉTODO DE EJECUCIÓN
# exe()
