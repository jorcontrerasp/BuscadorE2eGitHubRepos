#TFG (estudio CI/CD GitHub) - PRUEBAS
import datetime
import os
import auxiliares
import criterios
from github import Github

date = str(datetime.datetime.now())[0:19]
print(date + " - Iniciando prueba")

# Generamos un token para consultar la API de GitHub a través de la librería.
user = "userId"
token = "userToken"
g = Github(user, token)

carpetaRepositorios = "repositories"
nombreRepo = "kubernetes/ingress-nginx"
repo = g.get_repo(nombreRepo)
filtered_repos = [repo]

auxiliares.clonar1ListaRepo(filtered_repos)
reposEnLocal = os.listdir(carpetaRepositorios)

df = auxiliares.generarDataFrame(filtered_repos)
repos1 = criterios.recorrerRepositoriosLocal(reposEnLocal, criterios.Criterios.criterio3.value, df)

print(repos1)

date = str(datetime.datetime.now())[0:19]
print(date + " - Prueba finalizada")
