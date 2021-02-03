#TFG (estudio CI/CD GitHub) - Programa de validación

#Importamos las librerías necesarias.
import datetime
import os
import random
import criterios
import auxiliares
import pandas as pd
from github import Github

# Variables de configuración
generarListaRepos = False
randomizarListaRepos = False
lapseExe = True
doExcel = True
doCsv = False
clonarRepositorios = False
N_RANDOM = 200
N_LAPSE_REPOS = 20

date = str(datetime.datetime.now())[0:19]
print(date + " - Iniciando proceso")

fRepos = 'repos.pickle'

df = pd.DataFrame
df2 = pd.DataFrame

try:
    # Generamos un token para consultar la API de GitHub a través de la librería.
    user = "userId"
    token = "userToken"
    g = Github(user, token)

    if generarListaRepos:
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
        generator = g.search_repositories(query=query)

        # Convertimos el generador en una lista de repositorios.
        repositories = list(generator)
        print("Total repos: %d" % len(repositories))

        # Guardamos la información de los repositorios recuperados en un archivo binario de Python.
        fRepos = 'repos_%s.pickle' % date
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

    if lapseExe:
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

        listaAux = filtered_repos[0:N_LAPSE_REPOS-1]
        del filtered_repos[0:N_LAPSE_REPOS-1]
        auxiliares.generarPickle(fRepos, filtered_repos)
    else:
        listaAux = filtered_repos

        # Generamos nuevos DataFrames mediante la librería "pandas".
        df = auxiliares.generarDataFrame(listaAux)
        df2 = auxiliares.generarDataFrameContadores()

        # [PARA PRUEBAS] Generar DataFrames a partir de excels generados con anterioridad.
        #df = pd.read_excel("research.xlsx", index_col=0)
        #df2 = pd.read_excel("contadores.xlsx", index_col=0)

        if randomizarListaRepos:
            # Seleccionamos k repositorios de manera aleatoria:
            listaAux = random.choices(listaAux, k=N_RANDOM)
            print("Random projects: %d" % len(listaAux))

            # Guardamos la información de los repositorios randomizados en un archivo binario de Python.
            fRepos = 'random_repos_%s.pickle' % date
            auxiliares.generarPickle(fRepos, listaAux)
            listaAux = auxiliares.cargarRepositorios(fRepos)

            # Imprimimos la lista de repositorios
            auxiliares.imprimirListaRepositorios(listaAux)

    if len(listaAux) > 0:
        # Aplicamos criterios:
        #repos1_1 = criterios.buscarEnRaiz(listaAux, criterios.Criterios.criterio1.value, df)
        #repos1_2 = criterios.buscarEnTests(listaAux, criterios.Criterios.criterio1.value, df)
        #repos1_3 = criterios.buscarEnSrcTests(listaAux, criterios.Criterios.criterio1.value, df)

        #repos2_1 = criterios.buscarEnRaiz(listaAux, criterios.Criterios.criterio2.value, df)
        #repos2_2 = criterios.buscarEnTests(listaAux, criterios.Criterios.criterio2.value, df)
        #repos2_3 = criterios.buscarEnSrcTests(listaAux, criterios.Criterios.criterio2.value, df)

        #repos3_1 = criterios.buscarEnRaiz(listaAux, criterios.Criterios.criterio3.value, df)
        #repos3_2 = criterios.buscarEnTests(listaAux, criterios.Criterios.criterio3.value, df)
        #repos3_3 = criterios.buscarEnSrcTests(listaAux, criterios.Criterios.criterio3.value, df)

        #repos4_1 = criterios.buscarEnRaiz(listaAux, criterios.Criterios.criterio4.value, df)
        #repos4_2 = criterios.buscarEnTests(listaAux, criterios.Criterios.criterio4.value, df)
        #repos4_3 = criterios.buscarEnSrcTests(listaAux, criterios.Criterios.criterio4.value, df)

        #repos5_1 = criterios.buscarEnRaiz(listaAux, criterios.Criterios.criterio5.value, df)
        #repos5_2 = criterios.buscarEnTests(listaAux, criterios.Criterios.criterio5.value, df)
        #repos5_3 = criterios.buscarEnSrcTests(listaAux, criterios.Criterios.criterio5.value, df)

        #repos6_1 = criterios.buscarEnRaiz(listaAux, criterios.Criterios.criterio6.value, df)
        #repos6_2 = criterios.buscarEnTests(listaAux, criterios.Criterios.criterio6.value, df)
        #repos6_3 = criterios.buscarEnSrcTests(listaAux, criterios.Criterios.criterio6.value, df)

        #repos7_1 = criterios.buscarEnRaiz(listaAux, criterios.Criterios.criterio7.value, df)
        #repos7_2 = criterios.buscarEnTests(listaAux, criterios.Criterios.criterio7.value, df)
        #repos7_3 = criterios.buscarEnSrcTests(listaAux, criterios.Criterios.criterio7.value, df)

        #repos8_1 = criterios.buscarEnRaiz(listaAux, criterios.Criterios.criterio8.value, df)
        #repos8_2 = criterios.buscarEnTests(listaAux, criterios.Criterios.criterio8.value, df)
        #repos8_3 = criterios.buscarEnSrcTests(listaAux, criterios.Criterios.criterio8.value, df)

        #repos9_1 = criterios.buscarEnRaiz(listaAux, criterios.Criterios.criterio9.value, df)
        #repos9_2 = criterios.buscarEnTests(listaAux, criterios.Criterios.criterio9.value, df)
        #repos9_3 = criterios.buscarEnSrcTests(listaAux, criterios.Criterios.criterio9.value, df)

        #repos10 = criterios.buscarC10(listaAux, df)

        repos11 = criterios.buscarC11(listaAux, df)
    else:
        print("No se han obtenido repositorios del fichero " + fRepos)

    # Transformar DataFrame a Excel/CSV
    auxiliares.generarEXCEL_CSV(df, "research", doExcel, doCsv)

    # Generar un DataFrame auxiliar con los contadores de los repositorios encontrados por cada criterio
    columna = "n_encontrados"

    #nC1 = len(repos1_1) #+ len(repos1_2)
    #nC2 = len(repos2_1) + len(repos2_2)
    #nC3 = len(repos3_1) + len(repos3_2)
    #nC4 = len(repos4_1) + len(repos4_2)
    #nC5 = len(repos5_1) + len(repos5_2)
    #nC6 = len(repos6_1) + len(repos6_2)
    #nC7 = len(repos7_1) + len(repos7_2)
    #nC8 = len(repos8_1) + len(repos8_2)
    #nC9 = len(repos9_1) + len(repos9_2)
    #nC10 = len(repos10)
    nC11 = len(repos11)

    #df2.at[criterios.Criterios.criterio1.value, columna] += nC1
    #df2.at[criterios.Criterios.criterio2.value, columna] += nC2
    #df2.at[criterios.Criterios.criterio3.value, columna] += nC3
    #df2.at[criterios.Criterios.criterio4.value, columna] += nC4
    #df2.at[criterios.Criterios.criterio5.value, columna] += nC5
    #df2.at[criterios.Criterios.criterio6.value, columna] += nC6
    #df2.at[criterios.Criterios.criterio7.value, columna] += nC7
    #df2.at[criterios.Criterios.criterio8.value, columna] += nC8
    #df2.at[criterios.Criterios.criterio9.value, columna] += nC9
    #df2.at[criterios.Criterios.criterio10.value, columna] += nC10
    df2.at[criterios.Criterios.criterio11.value, columna] += nC11

    # Transformar DataFrame a Excel/CSV
    auxiliares.generarEXCEL_CSV(df2, "contadores", doExcel, doCsv)

    # Clonamos repositorios:
    if clonarRepositorios:
        lAux = []
        #lAux.append(repos1_1)
        auxiliares.clonarRepositorios(lAux)

    print(str(datetime.datetime.now())[0:19] + " - Proceso finalizado")
except:
    print(str(datetime.datetime.now())[0:19] + " - ERROR INESPERADO")
    raise
    #FIN
