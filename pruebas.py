#TFG (estudio CI/CD GitHub) - PRUEBAS
import datetime
import criterios
import auxiliares
from github import Github

date = str(datetime.datetime.now())[0:19]
print(date + " - Iniciando prueba")

# Generamos un token para consultar la API de GitHub a través de la librería.
user = "userId"
token = "userToken"
g = Github(user, token)

nombreRepo = "kubernetes/ingress-nginx"
filtered_repos = [g.get_repo(nombreRepo)]
auxiliares.imprimirListaRepositorios(filtered_repos)

# Aplicamos criterios:
df = auxiliares.generarDataFrame(filtered_repos)
repos = criterios.buscarEnTests(filtered_repos, criterios.Criterios.criterio3.value, df)

date = str(datetime.datetime.now())[0:19]
print(date + " - Prueba finalizada")
