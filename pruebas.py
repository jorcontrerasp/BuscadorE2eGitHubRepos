#TFG (estudio CI/CD GitHub) - PRUEBAS
import datetime
import criterios
import auxiliares
import pandas as pd
from github import Github

date = str(datetime.datetime.now())[0:19]
print(date + " - Iniciando prueba")

# Generamos un token para consultar la API de GitHub a través de la librería.
user = "userId"
token = "userToken"
g = Github(user, token)

filtered_repos = []
repo = g.get_repo("AnySoftKeyboard/AnySoftKeyboard")
filtered_repos.append(repo)
auxiliares.imprimirListaRepositorios(filtered_repos)

# Generar csv con pandas de los repositorios que se van a tratar.
df = pd.DataFrame([],
     index=[repo.full_name],
     columns=['criterio1', 'criterio2', 'criterio3', 'criterio4', 'criterio5', 'criterio6', 'criterio7', 'criterio8', 'criterio9', 'criterio10', 'criterio11'])

criterio = "integration"

if criterio == criterios.Criterios.criterio1.value:
     df.at[repo.full_name, criterios.Criterios.criterio1.name] = '[A] '
     print(df)

valor = str(df.at[repo.full_name, criterios.Criterios.criterio1.name])
if valor == "nan":
     df.at[repo.full_name, criterios.Criterios.criterio1.name] = '[B] '
     print(df)
else:
     df.at[repo.full_name, criterios.Criterios.criterio1.name] += '[B] '
     print(df)

# Aplicamos criterios:
#df = auxiliares.generarDataFrame(filtered_repos)
#repos = criterios.buscarC11(filtered_repos, df)

path = "addons/languages/persian/pack/dictionary/prebuilt/PersianPrebuild.xml"
path2 = "addons/Private_Play_Store.txt"

if "/" in path:
     pathArray = path.split("/")
     fActual = pathArray[len(pathArray)-1]

h = auxiliares.getFileContent(repo, path2)
print(h)


date = str(datetime.datetime.now())[0:19]
print(date + " - Prueba finalizada")
