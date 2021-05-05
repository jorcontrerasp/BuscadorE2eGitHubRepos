#TFG (estudio CI/CD GitHub) - Programa de validación

#Importamos las librerías necesarias.
from github import Github
import configuracion as conf
import filtrosQuery as fq
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

    print(conf.config.fechaEjecucion + " - Iniciando proceso.")

    try:
        # Generamos un token para consultar la API de GitHub a través de la librería.
        user = conf.config.user
        token = conf.config.token
        g = Github(user, token)

        if conf.config.generarListaRepos:
            print("Generando nueva lista de repositorios.")
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

            queryConf = fq.filtrosQuery.getQueryIni()
            fQueryInicial = "query-inicial_" + conf.config.fechaEjecucion + ".txt"
            f = open(fQueryInicial, "w")
            f.write("QUERY INICIAL:")
            f.write("\n")
            f.write(queryConf)
            generator = g.search_repositories(query=queryConf)

            # Convertimos el generador en una lista de repositorios.
            repositories = list(generator)
            print("Total repos: %d" % len(repositories))

            # Guardamos la información de los repositorios recuperados en un archivo binario de Python.
            fRepos = 'repos_%s.pickle' % conf.config.fechaEjecucion
            auxiliares.generarPickle(fRepos, repositories)
            repositories = auxiliares.cargarRepositorios(fRepos)

            # Almacenamos un registro de búsqueda en base de datos.
            if conf.config.actualizarBD:
                busqueda = busquedaBD.createBusquedaBD()
                busqueda.setLenguaje(fq.filtrosQuery.language)
                busqueda.setStars(fq.filtrosQuery.stars)
                busqueda.setForks(fq.filtrosQuery.forks)
                busqueda.setCreated(fq.filtrosQuery.created)
                busqueda.setPushed(fq.filtrosQuery.pushed)
                busqueda.setArchived(fq.filtrosQuery.archived)
                busqueda.setPublic(fq.filtrosQuery.qIs)
                idBusqueda = auxiliares.guardarBusquedaBD(busqueda)
                conf.config.idBusqueda = idBusqueda

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

        # Si hemos generado un nuevo pickle imprimimos la lista de repositorios.
        if conf.config.generarListaRepos:
            auxiliares.imprimirListaRepositorios(filteredRepos)

        auxiliares.crearCarpetasLocal()

        if conf.config.lapseExe:
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

            listaAux = filteredRepos[0:conf.config.N_LAPSE_REPOS]
            del filteredRepos[0:conf.config.N_LAPSE_REPOS]
            auxiliares.generarPickle(fRepos, filteredRepos)
        else:
            listaAux = []
            for r in filteredRepos:
                if r not in listaAux:
                    listaAux.append(r)

            if conf.config.randomizarListaRepos:
                # Seleccionamos N repositorios de manera aleatoria:
                lRandom = []
                while len(lRandom) < conf.config.N_RANDOM:
                    item = random.choice(listaAux)
                    if item not in lRandom:
                        lRandom.append(item)
                listaAux = lRandom
                print("Random projects: %d" % len(listaAux))

                # Guardamos la información de los repositorios randomizados en un archivo binario de Python.
                fRepos = 'random_repos_%s.pickle' % conf.config.fechaEjecucion
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
            if conf.config.buscarEnLocal:

                print("Nº repos que se van a clonar: " + str(len(listaAux)))
                # Clonamos en local los repositorios obtenidos:
                auxiliares.clonar1ListaRepo(listaAux)

                # Rellenamos la columna CommitID del DataFrame con los repositorios ya clonados
                auxiliares.actualizarDataFrameCommitID(listaAux, df)

                # Listamos los repositorios clonados
                reposEnLocal = os.listdir(conf.config.cRepositorios)

                # Aplicamos criterios
                print("Nº repos en local: " + str(len(reposEnLocal)))
                print("Aplicando criterios...")
                lReposEncontrados = criterios.recorrerRepositoriosLocal(reposEnLocal, df, df2)

                # Generar Zip de los repositorios
                auxiliares.generarZipRepos()

            else:
                # Aplicamos criterios:
                print("Aplicando criterios...")
                lReposEncontrados = criterios.busquedaGitHubApiRepos(listaAux, df, df2)

            print("Nº de repos encontrados: " + str(len(lReposEncontrados)))
        else:
            print("No se han obtenido repositorios del fichero " + fRepos)
            auxiliares.generarEXCEL_CSV(df, conf.config.cResearch,
                                        conf.config.doExcel,conf.config.doCsv)
            auxiliares.generarEXCEL_CSV(df2, conf.config.cContadores,
                                        conf.config.doExcel, conf.config.doCsv)

            if os.path.exists("tmp-research.xlsx"):
                os.remove("tmp-research.xlsx")
                print("Fichero tmp-research.xlsx eliminado")
            if os.path.exists("tmp-contadores.xlsx"):
                os.remove("tmp-contadores.xlsx")
                print("Fichero tmp-contadores.xlsx eliminado")

            # Guardamos la búsqueda junto con los ficheros excel en BD.
            if conf.config.actualizarBD:
                busqueda = busquedaBD.createBusquedaBD()
                busqueda.setLenguaje(fq.filtrosQuery.language)
                busqueda.setStars(fq.filtrosQuery.stars)
                busqueda.setForks(fq.filtrosQuery.forks)
                busqueda.setCreated(fq.filtrosQuery.created)
                busqueda.setPushed(fq.filtrosQuery.pushed)
                busqueda.setArchived(fq.filtrosQuery.archived)
                busqueda.setPublic(fq.filtrosQuery.qIs)
                busqueda.setResearch(conf.config.cResearch + ".xlsx")
                busqueda.setContadores(conf.config.cContadores + ".xlsx")
                idBusqueda = auxiliares.guardarBusquedaBD(busqueda)
                conf.config.idBusqueda = idBusqueda

            continuar = False

        if continuar:
            # Transformar DataFrame a Excel/CSV
            if conf.config.lapseExe:
                auxiliares.generarEXCEL_CSV(df, "tmp-research", conf.config.doExcel, conf.config.doCsv)
                auxiliares.generarEXCEL_CSV(df2, "tmp-contadores", conf.config.doExcel, conf.config.doCsv)
            else:
                auxiliares.generarEXCEL_CSV(df, conf.config.cResearch, conf.config.doExcel, conf.config.doCsv)
                auxiliares.generarEXCEL_CSV(df2, conf.config.cContadores, conf.config.doExcel,
                                            conf.config.doCsv)

                # Guardamos los ficheros excel en BD.
                if conf.config.actualizarBD:
                    busqueda = busquedaBD.createBusquedaBD()
                    busqueda.setIdBusqueda(conf.config.idBusqueda)
                    busqueda.setResearch(conf.config.cResearch + ".xlsx")
                    busqueda.setContadores(conf.config.cContadores + ".xlsx")
                    auxiliares.guardarBusquedaBD(busqueda)

            # Clonamos repositorios:
            if conf.config.clonarRepositorios:
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
