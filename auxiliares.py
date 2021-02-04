#FUNCIONES AUXILIARES

#Importamos las librerías necesarias.
import base64
import os
import datetime
import pickle
from github import GithubException
import criterios
import openpyxl
import pandas as pd

date = str(datetime.datetime.now())[0:19].replace(" ", "_")
carpetalogs = "logs"

def imprimirListaRepositorios(repositorios):
    for project in repositorios:
        project_name = project.full_name.split("/")[1]
        print(project.full_name)

def imprimirRepositorio(project):
    project_name = project.full_name.split("/")[1]
    print(project.full_name)

def listarReposDataFrame(listaRepositorios):
    listaStr = ''
    for repo in listaRepositorios:
        listaStr = listaStr + '\'' + repo.full_name + '\'' + ','
    longitud = len(listaStr)
    return listaStr[0:longitud-1]

def generarDataFrame(listaRepositorios):
    repo1 = listaRepositorios[0]
    df = pd.DataFrame([],
                      index=[repo1.full_name],
                      columns=['criterio1', 'criterio2', 'criterio3', 'criterio4', 'criterio5', 'criterio6',
                               'criterio7', 'criterio8', 'criterio9', 'criterio10', 'criterio11'])

    for repo in listaRepositorios[1:len(listaRepositorios)-1]:
        df2 = pd.DataFrame([],
                           index=[repo.full_name],
                           columns=['criterio1', 'criterio2', 'criterio3', 'criterio4', 'criterio5', 'criterio6',
                                    'criterio7', 'criterio8', 'criterio9', 'criterio10', 'criterio11'])
        df = df.append(df2)

    return df

def actualizarDataFrame(criterio, nombreRepo, path, df):
    if criterio == criterios.Criterios.criterio1.value:
        criterio1 = criterios.Criterios.criterio1.name.lower()
        actualizarDataFrameAux(criterio1, nombreRepo, path, df)

    elif criterio == criterios.Criterios.criterio2.value:
        criterio2 = criterios.Criterios.criterio2.name.lower()
        actualizarDataFrameAux(criterio2, nombreRepo, path, df)

    elif criterio == criterios.Criterios.criterio3.value:
        criterio3 = criterios.Criterios.criterio3.name.lower()
        actualizarDataFrameAux(criterio3, nombreRepo, path, df)

    elif criterio == criterios.Criterios.criterio4.value:
        criterio4 = criterios.Criterios.criterio4.name.lower()
        actualizarDataFrameAux(criterio4, nombreRepo, path, df)

    elif criterio == criterios.Criterios.criterio5.value:
        criterio5 = criterios.Criterios.criterio5.name.lower()
        actualizarDataFrameAux(criterio5, nombreRepo, path, df)

    elif criterio == criterios.Criterios.criterio6.value:
        criterio6 = criterios.Criterios.criterio6.name.lower()
        actualizarDataFrameAux(criterio6, nombreRepo, path, df)

    elif criterio == criterios.Criterios.criterio7.value:
        criterio7 = criterios.Criterios.criterio7.name.lower()
        actualizarDataFrameAux(criterio7, nombreRepo, path, df)

    elif criterio == criterios.Criterios.criterio8.value:
        criterio8 = criterios.Criterios.criterio8.name.lower()
        actualizarDataFrameAux(criterio8, nombreRepo, path, df)

    elif criterio == criterios.Criterios.criterio9.value:
        criterio9 = criterios.Criterios.criterio9.name.lower()
        actualizarDataFrameAux(criterio9, nombreRepo, path, df)

    elif criterio == criterios.Criterios.criterio10.value:
        criterio10 = criterios.Criterios.criterio10.value.lower()
        actualizarDataFrameAux(criterio10, nombreRepo, path, df)

    elif criterio == criterios.Criterios.criterio11.value:
        criterio11 = criterios.Criterios.criterio11.name.lower()
        actualizarDataFrameAux(criterio11, nombreRepo, path, df)

    else:
        print("Criterio no definido")

def actualizarDataFrameAux(criterio, nombreRepo, path, df):
    valor = str(df.at[nombreRepo, criterio])
    if valor == "nan":
        df.at[nombreRepo, criterio] = "[" + path + "] "
    else:
        df.at[nombreRepo, criterio] += "[" + path + "] "

def generarDataFrameContadores():
    df = pd.DataFrame([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                      index=[criterios.Criterios.criterio1.value,
                             criterios.Criterios.criterio2.value,
                             criterios.Criterios.criterio3.value,
                             criterios.Criterios.criterio4.value,
                             criterios.Criterios.criterio5.value,
                             criterios.Criterios.criterio6.value,
                             criterios.Criterios.criterio7.value,
                             criterios.Criterios.criterio8.value,
                             criterios.Criterios.criterio9.value,
                             criterios.Criterios.criterio10.value,
                             criterios.Criterios.criterio11.value],
                      columns=['n_encontrados'])
    return df

def generarEXCEL_CSV(df, nombreFichero, generarExcel, generarCsv):
    if generarExcel:
        df.to_excel(nombreFichero + ".xlsx")

    if generarCsv:
        df.to_csv(nombreFichero + ".csv")

def generarPickle(nombreFichero, listaRepositorios):
    with open(nombreFichero, 'wb') as f:
        pickle.dump(listaRepositorios, f)
    print("Fichero " + nombreFichero + ".pickle generado")

def cargarRepositorios(fichero):
    with open(fichero, 'rb') as f:
        repositories = pickle.load(f)
    return repositories

def getBlobContent(repo, branch, path_name):
    # Obtener referencia del "branch"
    ref = repo.get_git_ref(f'heads/{branch}')
    # Obtener el árbol
    tree = repo.get_git_tree(ref.object.sha, recursive='/' in path_name).tree
    # Buscar ruta en el árbol
    sha = [x.sha for x in tree if x.path == path_name]
    if not sha:
        # SHA no encontrado
        return None
    # SHA encontrado
    return repo.get_git_blob(sha[0])

def getFileContent(repo, filePath):
    try:
        res = repo.get_contents(filePath)
        return str(res.decoded_content)
    except GithubException:
        blob = getBlobContent(repo, "master", filePath)
        b64 = base64.b64decode(blob.content)
        content = b64.decode("utf8")
        return str(content)

def obtenerFicheroIt(path):
    if "/" in path:
        pathArray = path.split("/")
        fActual = pathArray[len(pathArray) - 1]
    else:
        fActual = path
    return fActual

def clonar1ListaRepo(repositorios):
    # Generamos el directorio 'repositories'
    folder_name = 'repositories'
    if not os.path.exists(folder_name):
        print("Folder %s created!" % folder_name)
        os.mkdir("repositories")
    else:
        print("Folder %s already exist" % folder_name)

    # Clonamos los repositorios
    for project in repositorios:
        project_name = project.full_name.split("/")[1]
        project_folder = "%s/%s" % (folder_name, project_name)

        # CHECK IF PROJECT EXISTS
        if os.path.exists(project_folder):
            print(" -> Project %s already exist in local folder!" % project.full_name)
        else:
            print("Clonando " + project.clone_url + " en " + project_folder)
            # get_ipython().system('git clone $project.clone_url $project_folder')
            comando = 'git clone ' + project.clone_url + ' ' + project_folder
            print(comando)
            os.system(comando)
            print(" -> Project %s cloned!" % project_name)

def clonarRepositorios(lRepositorios):
    # Generamos el directorio 'repositories'
    folder_name = 'repositories'
    if not os.path.exists(folder_name):
        print("Folder %s created!" % folder_name)
        os.mkdir("repositories")
    else:
        print("Folder %s already exist" % folder_name)

    # Clonamos los repositorios
    for repositorio in lRepositorios:
        for project in repositorio:
            project_name = project.full_name.split("/")[1]
            project_folder = "%s/%s" % (folder_name, project_name)

            # CHECK IF PROJECT EXISTS
            if os.path.exists(project_folder):
                print(" -> Project %s already exist in local folder!" % project.full_name)
            else:
                print("Clonando " + project.clone_url + " en " + project_folder)
                #get_ipython().system('git clone $project.clone_url $project_folder')
                comando = 'git clone ' + project.clone_url + ' ' + project_folder
                print(comando)
                os.system(comando)
                print(" -> Project %s cloned!" % project_name)