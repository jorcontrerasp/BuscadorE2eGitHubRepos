#TFG (estudio CI/CD GitHub) - Programa de validación

#Importamos las librerías necesarias.
import datetime
import criterios
import auxiliares
from github import Github

generarListaRepos = True

date = str(datetime.datetime.now())[0:19]
print(date + " - Iniciando prueba")

# Generamos un token para consultar la API de GitHub a través de la librería.
user = "userId"
token = "userToken"
g = Github(user, token)

filtered_repos = []
repo = g.get_repo("PyGithub/PyGithub")
filtered_repos.append(repo)
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
repos = criterios.buscarEnRepo(filtered_repos, criterio1)

# Clonamos repositorios:
lAux = []
lAux.append(repos)
auxiliares.clonarRepositorios(lAux)

date = str(datetime.datetime.now())[0:19]
print(date + " - Prueba finalizada")
