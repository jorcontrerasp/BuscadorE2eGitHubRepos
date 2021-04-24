#FUNCIONES AUXILIARES

#Importamos las librerías necesarias.
import configuracion as conf
import filtrosQuery as fq
import criterios
import pickle
import pandas as pd
import subprocess
import base64
import os
import shutil
from shutil import rmtree
import logging
from github import GithubException
import repoBD
import executeQuery
import openpyxl

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
                      columns=["GitHub_URL", "Lenguaje", "CommitID"
                               ,criterios.Criterios.criterio1.name
                               #,criterios.Criterios.criterio2.name
                               ,criterios.Criterios.criterio3.name
                               #,criterios.Criterios.criterio4.name
                               ,criterios.Criterios.criterio5.name
                               #,criterios.Criterios.criterio6.name
                               #,criterios.Criterios.criterio7.name
                               #,criterios.Criterios.criterio8.name
                               #,criterios.Criterios.criterio9.name
                               ,criterios.Criterios.criterio10.name
                               #,criterios.Criterios.criterio11.name
                               #,criterios.Criterios.criterio12.name
                               ])
    df.at[repo1.full_name, "GitHub_URL"] = repo1.html_url
    df.at[repo1.full_name, "Lenguaje"] = repo1.language
    df.at[repo1.full_name, criterios.Criterios.criterio1.name] = " "
    #df.at[repo1.full_name, criterios.Criterios.criterio2.name] = " "
    df.at[repo1.full_name, criterios.Criterios.criterio3.name] = " "
    #df.at[repo1.full_name, criterios.Criterios.criterio4.name] = " "
    df.at[repo1.full_name, criterios.Criterios.criterio5.name] = " "
    #df.at[repo1.full_name, criterios.Criterios.criterio6.name] = " "
    #df.at[repo1.full_name, criterios.Criterios.criterio7.name] = " "
    #df.at[repo1.full_name, criterios.Criterios.criterio8.name] = " "
    #df.at[repo1.full_name, criterios.Criterios.criterio9.name] = " "
    df.at[repo1.full_name, criterios.Criterios.criterio10.name] = " "
    #df.at[repo1.full_name, criterios.Criterios.criterio11.name] = " "
    #df.at[repo1.full_name, criterios.Criterios.criterio12.name] = " "

    # Actualizamos la BD
    repo1BBDD = repoBD.createRepoBD()
    repo1BBDD.setNombre(repo1.full_name.split("/")[1])
    repo1BBDD.setOrganizacion(repo1.full_name.split("/")[0])
    repo1BBDD.setLenguaje(repo1.language)
    repo1BBDD.setUrl(repo1.html_url)
    repo1BBDD.setSize(repo1.size)
    repo1BBDD.setBoE2e(0)
    repo1BBDD.setIdBusqueda(conf.config.idBusqueda)
    guardarRepoEnBD(repo1BBDD)

    for repo in listaRepositorios[1:len(listaRepositorios)]:
        df2 = pd.DataFrame([],
                          index=[repo.full_name],
                          columns=["GitHub_URL", "Lenguaje", "CommitID"
                                   ,criterios.Criterios.criterio1.name
                                   #,criterios.Criterios.criterio2.name
                                   ,criterios.Criterios.criterio3.name
                                   #,criterios.Criterios.criterio4.name
                                   ,criterios.Criterios.criterio5.name
                                   #,criterios.Criterios.criterio6.name
                                   #,criterios.Criterios.criterio7.name
                                   #,criterios.Criterios.criterio8.name
                                   #,criterios.Criterios.criterio9.name
                                   ,criterios.Criterios.criterio10.name
                                   #,criterios.Criterios.criterio11.name
                                   #,criterios.Criterios.criterio12.name
                                   ])
        df2.at[repo.full_name, "GitHub_URL"] = repo.html_url
        lenguaje = repo.language
        df2.at[repo.full_name, "Lenguaje"] = repo.language
        df2.at[repo.full_name, criterios.Criterios.criterio1.name] = " "
        # df2.at[repo.full_name, criterios.Criterios.criterio2.name] = " "
        df2.at[repo.full_name, criterios.Criterios.criterio3.name] = " "
        # df2.at[repo.full_name, criterios.Criterios.criterio4.name] = " "
        df2.at[repo.full_name, criterios.Criterios.criterio5.name] = " "
        # df2.at[repo.full_name, criterios.Criterios.criterio6.name] = " "
        # df2.at[repo.full_name, criterios.Criterios.criterio7.name] = " "
        # df2.at[repo.full_name, criterios.Criterios.criterio8.name] = " "
        # df2.at[repo.full_name, criterios.Criterios.criterio9.name] = " "
        df2.at[repo.full_name, criterios.Criterios.criterio10.name] = " "
        # df2.at[repo.full_name, criterios.Criterios.criterio11.name] = " "
        # df2.at[repo.full_name, criterios.Criterios.criterio12.name] = " "
        df = df.append(df2)

        # Actualizamos la BD
        repoBBDD = repoBD.createRepoBD()
        repoBBDD.setNombre(repo.full_name.split("/")[1])
        repoBBDD.setOrganizacion(repo.full_name.split("/")[0])
        repoBBDD.setLenguaje(repo.language)
        repoBBDD.setUrl(repo.html_url)
        repoBBDD.setSize(repo.size)
        repoBBDD.setBoE2e(0)
        repoBBDD.setIdBusqueda(conf.config.idBusqueda)
        guardarRepoEnBD(repoBBDD)

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

    elif criterio == criterios.Criterios.criterio12.value:
        criterio12 = criterios.Criterios.criterio12.name.lower()
        actualizarDataFrameAux(criterio12, nombreRepo, path, df)

    else:
        print("Criterio no definido")

def actualizarDataFrameCommitID(listaRepos, df):
    for repo in listaRepos:
        commitID = obtenerRepoCommitID(repo.full_name.replace("/", "*_*"))
        df.at[repo.full_name, "CommitID"] = commitID

        # Actualizamos la BD
        repoBBDD = repoBD.createRepoBD()
        repoBBDD.setNombre(repo.full_name.split("/")[1])
        repoBBDD.setOrganizacion(repo.full_name.split("/")[0])
        repoBBDD.setLenguaje(repo.language)
        repoBBDD.setUrl(repo.html_url)
        repoBBDD.setSize(repo.size)
        repoBBDD.setCommitID(commitID)
        repoBBDD.setBoE2e(0)
        repoBBDD.setIdBusqueda(conf.config.idBusqueda)
        guardarRepoEnBD(repoBBDD)

def contarRepositoriosAlMenos1Criterio(df):
    cont = 0
    for index, row in df.iterrows():
        if (len(str(row[criterios.Criterios.criterio1.name])) > 1):
            cont += 1
        #elif (len(str(row[criterios.Criterios.criterio2.name])) > 1):
            #cont += 1
        elif (len(str(row[criterios.Criterios.criterio3.name])) > 1):
            cont += 1
        #elif (len(str(row[criterios.Criterios.criterio4.name])) > 1):
            #cont += 1
        elif (len(str(row[criterios.Criterios.criterio5.name])) > 1):
            cont += 1
        #elif (len(str(row[criterios.Criterios.criterio6.name])) > 1):
            #cont += 1
        #elif (len(str(row[criterios.Criterios.criterio7.name])) > 1):
            #cont += 1
        #elif (len(str(row[criterios.Criterios.criterio8.name])) > 1):
            #cont += 1
        #elif (len(str(row[criterios.Criterios.criterio9.name])) > 1):
            #cont += 1
        elif (len(str(row[criterios.Criterios.criterio10.name])) > 1):
            cont += 1
        #elif (len(row[criterios.Criterios.criterio11.name]) > 1):
            #cont += 1
        #elif (len(row[criterios.Criterios.criterio12.name]) > 1):
            #cont += 1
    return cont

def actualizarDataFrameAux(criterio, nombreRepo, path, df):
    valor = str(df.at[nombreRepo, criterio])
    if valor == "nan":
        df.at[nombreRepo, criterio] = "[" + path + "]\n"
    else:
        df.at[nombreRepo, criterio] += "[" + path + "]\n"

def generarDataFrameContadores():
    df = pd.DataFrame([0, 0, 0, 0, 0],
                      index=[criterios.Criterios.criterio1.value
                             #,criterios.Criterios.criterio2.value
                             ,criterios.Criterios.criterio3.value
                             #,criterios.Criterios.criterio4.value
                             ,criterios.Criterios.criterio5.value
                             #,criterios.Criterios.criterio6.value
                             #,criterios.Criterios.criterio7.value
                             #,criterios.Criterios.criterio8.value
                             #,criterios.Criterios.criterio9.value
                             ,criterios.Criterios.criterio10.value
                             #,criterios.Criterios.criterio11.value
                             #,criterios.Criterios.criterio12.value
                             ,"Totales"],
                      columns=['n_encontrados'])
    return df

def obtenerRepoCommitID(repo):
    proyectPath = os.getcwd()
    # Inicializamos el commitID a 'NE' (no encontrado).
    commitID = "NE"
    ruta = proyectPath + "/" + conf.config.cRepositorios + "/" + repo
    if os.path.exists(ruta):
        os.chdir(ruta)
        commitIDAux = subprocess.check_output("git log --pretty=format:'%h' -n 1", shell=True)
        commitID = commitIDAux.decode()
        os.chdir(proyectPath)
    else:
        print("No se ha encontrado la ruta " + ruta)
    return commitID

def generarEXCEL_CSV(df, pFichero, generarExcel, generarCsv):
    if generarExcel:
        df.to_excel(pFichero + ".xlsx")

    if generarCsv:
        df.to_csv(pFichero + ".csv")

def generarPickle(nombreFichero, listaRepositorios):
    with open(nombreFichero, 'wb') as f:
        pickle.dump(listaRepositorios, f)
    print("Fichero " + nombreFichero + " generado")

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

def crearCarpetasLocal():
    # CREAR CARPETAS NECESARIAS EN LOCAL
    # Creamos la carpeta donde van los logs (si no existe)
    if not os.path.exists(conf.config.cLogs):
        os.mkdir(conf.config.cLogs)

    # Creamos la carpeta donde van los repositories (si no existe)
    if not os.path.exists(conf.config.cRepositorios.split("/")[0]):
        os.mkdir(conf.config.cRepositorios.split("/")[0])

    # Creamos la carpeta donde van los contadores (si no existe)
    if not os.path.exists(conf.config.cContadores.split("/")[0]):
        os.mkdir(conf.config.cContadores.split("/")[0])

    # Creamos la carpeta donde van los research (si no existe)
    if not os.path.exists(conf.config.cResearch.split("/")[0]):
        os.mkdir(conf.config.cResearch.split("/")[0])
    # FIN CREAR CARPETAS NECESARIAS EN LOCAL

def clonar1ListaRepo(repositorios):
    # Generamos el directorio 'repositories'
    if not os.path.exists(conf.config.cRepositorios):
        print("Folder %s created!" % conf.config.cRepositorios)
        os.mkdir(conf.config.cRepositorios)
    else:
        print("Folder %s already exist" % conf.config.cRepositorios)

    # Clonamos los repositorios
    for project in repositorios:
        if project.size > conf.config.REPO_SIZE_LIMIT:
            print("Repositorio NO clonado. Ocupa demasiado en disco.")
        else:
            #project_name = project.full_name.split("/")[1]
            project_name = project.full_name.replace("/", "*_*")
            project_folder = "%s/%s" % (conf.config.cRepositorios, project_name)

            # CHECK IF PROJECT EXISTS
            if os.path.exists(project_folder):
                print(" -> Project %s already exist in local folder!" % project.full_name)
            else:
                print("Clonando " + project.clone_url + " en " + project_folder)
                # get_ipython().system('git clone $project.clone_url $project_folder')
                comando = 'git clone ' + project.clone_url + ' ' + project_folder
                print(comando)
                try:
                    p = subprocess.Popen(comando, shell=True)
                    p.wait()
                    #os.system(comando)
                    print(" -> Project %s cloned!" % project_name)
                except:
                    print("***WARN** - Por algún motivo no se ha podido clonar el repositorio: " + project.full_name)


def clonarRepositorios(lRepositorios):
    # Generamos el directorio 'repositories'
    if not os.path.exists(conf.config.cRepositorios):
        print("Folder %s created!" % conf.config.cRepositorios)
        os.mkdir(conf.config.cRepositorios)
    else:
        print("Folder %s already exist" % conf.config.cRepositorios)

    # Clonamos los repositorios
    for repositorio in lRepositorios:
        for project in repositorio:
            if project.size > conf.config.REPO_SIZE_LIMIT:
                print("Repositorio NO clonado. Ocupa demasiado en disco.")
            else:
                project_name = project.full_name.split("/")[1]
                project_folder = "%s/%s" % (conf.config.cRepositorios, project_name)

                # CHECK IF PROJECT EXISTS
                if os.path.exists(project_folder):
                    print(" -> Project %s already exist in local folder!" % project.full_name)
                else:
                    print("Clonando " + project.clone_url + " en " + project_folder)
                    #get_ipython().system('git clone $project.clone_url $project_folder')
                    comando = 'git clone ' + project.clone_url + ' ' + project_folder
                    print(comando)
                    try:
                        p = subprocess.Popen(comando, shell=True)
                        p.wait()
                        #os.system(comando)
                        print(" -> Project %s cloned!" % project_name)
                    except:
                        print("***WARN** - Por algún motivo no se ha podido clonar el repositorio: " + project.full_name)

def generarZipRepos():
    logging.basicConfig(level=logging.DEBUG,
                        format='%(asctime)s : %(levelname)s : %(message)s',
                        filename='logs/repositories_' + conf.config.fechaEjecucion + '.log',
                        filemode='w', )

    archivo_zip = shutil.make_archive("repos_snapshots/repositories_" + conf.config.fechaEjecucion,
                                      "zip",
                                      base_dir=conf.config.cRepositorios,
                                      logger=logging)

    rmtree("./" + conf.config.cRepositorios)

def convertToBinaryData(filename):
    # Convert digital data to binary format
    with open(filename, 'rb') as file:
        binaryData = file.read()
    return binaryData

def guardarRepoEnBD(repoBBDD):
    print("Actualizando base de datos...")
    repoFiltro = repoBD.createRepoBD()
    repoFiltro.setNombre(repoBBDD.getNombre())
    repoFiltro.setOrganizacion(repoBBDD.getOrganizacion())

    query = repoFiltro.getFiltro()

    filas = executeQuery.execute(query)
    if len(filas) > 0:
        fila1 = filas[0]
        id = fila1["idrepo"]
        repoBBDD.setId(id)
        update = repoBBDD.getUpdate()
        rUpdate = executeQuery.execute(update)
    else:
        insert = repoBBDD.getInsert()
        rInsert = executeQuery.execute(insert)

def guardarBusquedaBD(busquedaBD):
    if busquedaBD.getIdBusqueda() > 0:
        update = busquedaBD.getUpdateParam()
        rUpdate = executeQuery.executeWithParams(update)
        return rUpdate
    else:
        insert = busquedaBD.getInsertParam()
        idBusqueda = executeQuery.executeWithParams(insert)
        return idBusqueda