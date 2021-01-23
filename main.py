#TFG (estudio CI/CD GitHub) - Programa de validación

#Importamos las librerías necesarias.
import datetime
import random
import pickle
import criterios
import auxiliares
from github import Github

generarListaRepos = True
date = str(datetime.datetime.now())[0:19]
print(date + " - Iniciando proceso")

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
        with open('repos_%s.pickle' % date, 'wb') as f:
            pickle.dump(repositories, f)
        print("Fichero .pickle generado")
        fRepos = 'repos_%s.pickle' % date
        repositories = auxiliares.cargarRepositorios(fRepos)
    else:
        fRepos = 'repos_2021-01-17 17:44:04.pickle'
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

    # Seleccionamos k repositorios de manera aleatoria:
    #filtered_repos = random.choices(filtered_repos, k=20)
    #print("Random projects: %d" % len(filtered_repos))

    auxiliares.imprimirListaRepositorios(filtered_repos)

    # Aplicamos criterios:
    criterio1 = "integration"
    criterio2 = "system"
    criterio3 = "e2e"
    criterio4_1 = "itest"
    criterio4_2 = "itests"
    criterio5 = "acceptance"
    criterio6 = "distributed"
    criterio7 = "end-to-end-test"
    criterio8 = "docker"
    criterio9 = "swagger"
    repos1 = criterios.buscarEnTests(filtered_repos, criterio1)

    # Clonamos repositorios:
    lAux = []
    lAux.append(repos1)
    auxiliares.clonarRepositorios(lAux)

    print(str(datetime.datetime.now())[0:19] + " - Proceso finalizado")
except:
    print(str(datetime.datetime.now())[0:19] + " - ERROR INESPERADO")
    raise
    #FIN
