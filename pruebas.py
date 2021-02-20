#TFG (estudio CI/CD GitHub) - PRUEBAS
import configuracion as conf
import auxiliares
import criterios
import datetime
import os
from github import Github

print(conf.Configuracion.fechaEjecucion + " - Iniciando prueba")

# Generamos un token para consultar la API de GitHub a través de la librería.
user = conf.Configuracion.user
token = conf.Configuracion.token
g = Github(user, token)

nombreRepo = "apache/karaf"
repo = g.get_repo(nombreRepo)
filtered_repos = [repo]

auxiliares.clonar1ListaRepo(filtered_repos)

reposEnLocal = os.listdir(conf.Configuracion.carpetaRepositorios)

df = auxiliares.generarDataFrame(filtered_repos)
#repos1 = criterios.recorrerRepositoriosLocal(reposEnLocal, criterios.Criterios.criterio8.value, df)

df.at["apache/karaf", "GitHub_URL"] = df.at["apache/karaf", "GitHub_URL"] + "AAA\n"
df.at["apache/karaf", "GitHub_URL"] = df.at["apache/karaf", "GitHub_URL"] + "BBB\n"

auxiliares.generarEXCEL_CSV(df, "research", conf.Configuracion.doExcel, conf.Configuracion.doCsv)


#print(repos1)

date = str(datetime.datetime.now())[0:19]
print(date + " - Prueba finalizada")
