from enum import Enum
import configuracion as conf
import auxiliares
import os
import repoBD
import time

class Criterios(Enum):
    criterio1 = "integration"
    criterio2 = "system"
    criterio3 = "e2e"
    criterio4 = "itest"
    criterio5 = "acceptance"
    criterio6 = "distributed"
    criterio7 = "end-to-end-test"
    criterio8 = "docker"
    criterio9 = "swagger"
    criterio10 = "criterio10"
    criterio11 = "criterio11"
    criterio12 = "ci-files"

# FUNCIONES DE BÚSQUEDA LOCAL
def obtenerRutaCompletaE(origen, lFicheros):
    content = []
    for c in lFicheros:
        content.append(origen + "/" + c)

    return content

def recorrerRepositoriosLocal(listaRepositorios, df, df2):
    listaEncontrados = []
    for repo in listaRepositorios:

        content = obtenerRutaCompletaE("./" + conf.config.cRepositorios, [repo])

        rutaIni = content[0]
        if os.path.exists(rutaIni):

            # Buscamos C1
            boC1 = buscarTodaCarpetaEnRepoLocal2(repo, content, Criterios.criterio1.value, df)

            # Buscamos C3
            content = obtenerRutaCompletaE("./" + conf.config.cRepositorios, [repo])
            boC3 = buscarTodaCarpetaEnRepoLocal2(repo, content, Criterios.criterio3.value, df)

            # Buscamos C5
            content = obtenerRutaCompletaE("./" + conf.config.cRepositorios, [repo])
            boC5 = buscarTodaCarpetaEnRepoLocal2(repo, content, Criterios.criterio5.value, df)

            # Buscamos C10
            content = obtenerRutaCompletaE("./" + conf.config.cRepositorios, [repo])
            boC10 = buscarC10_Local(repo, content, df)

            # Si lo ha encontrado:
            # - lo añadimos a la listaEncontrados.
            encontrado = False
            if boC1 or boC3 or boC5 or boC10:
                listaEncontrados.append(repo)
                encontrado = True

            # Actualizamos BD
            if conf.config.actualizarBD:
                print("Actualizando base de datos...")
                repoBBDD = repoBD.createRepoBD()
                repoBBDD.setNombre(repo.split("*_*")[1])
                repoBBDD.setOrganizacion(repo.split("*_*")[0])
                repoBBDD.setBoE2e(encontrado)
                auxiliares.guardarRepoEnBD(repoBBDD)

            # Actualizamos contadores
            columna = "n_encontrados"
            if boC1:
                df2.at[Criterios.criterio1.value, columna] += 1
            if boC3:
                df2.at[Criterios.criterio3.value, columna] += 1
            if boC5:
                df2.at[Criterios.criterio5.value, columna] += 1
            if boC10:
                df2.at[Criterios.criterio10.value, columna] += 1

            df2.at["Totales", columna] = auxiliares.contarRepositoriosAlMenos1Criterio(df)
        else:
            print("No se ha encontrado la ruta " + rutaIni)

    return listaEncontrados

# El primer fichero o carpeta que cumpla el criterio será el que devuelva
def buscarPrimeroEnRepoLocal(repo, lFicheros, criterio, df):
    log = conf.config.cLogs + "/log_buscarEnRepoLocal_" + criterio + "_" + conf.config.fechaEjecucion + ".log"
    f = auxiliares.abrirLog(log)
    auxiliares.escribirLog(f, "--> Analizando repositorio: " + repo + ", criterio: " + criterio)
    print("--> Analizando repositorio: " + repo + ", criterio: " + criterio)
    encontrado = True
    minLimit = conf.config.SEARCH_TIME_LIMIT  # minutos
    segLimit = minLimit * 60  # segundos
    tIni = time.perf_counter()
    tFin = tIni + 1
    while len(lFicheros) > 0 and (tFin - tIni) <= segLimit:
        tFin = time.perf_counter()
        e = lFicheros.pop(0)
        f.write(e)
        f.write("\n")
        if os.path.isdir(e):
            #print(e + "[CARPETA]")
            if criterio in e.lower():
                auxiliares.escribirLog(f, "Adding " + e)
                repo = repo.replace("*_*", "/")
                auxiliares.actualizarDataFrame(criterio, repo, e, df)
                encontrado = True
                break
            else:
                contentAux = os.listdir(e)
                content = obtenerRutaCompletaE(e, contentAux)
                for c in content:
                    lFicheros.insert(0, c)
        elif os.path.isfile(e):
            #print(e + "[FICHERO]")
            if criterio in e.lower():
                auxiliares.escribirLog(f, "Adding " + e)
                repo = repo.replace("*_*", "/")
                auxiliares.actualizarDataFrame(criterio, repo, e, df)
                encontrado = True
                break
    auxiliares.cerrarLog(f)
    return encontrado

# Busca todas los ficheros/carpetas que coinciden (no que contengan) con el criterio.
def buscarTodaCarpetaEnRepoLocal(repo, lFicheros, criterio, df):
    log = conf.config.cLogs + "/log_buscarEnRepoLocal_" + criterio + "_" + conf.config.fechaEjecucion + ".log"
    f = auxiliares.abrirLog(log)
    auxiliares.escribirLog(f, "--> Analizando repositorio: " + repo + ", criterio: " + criterio)
    print("--> Analizando repositorio: " + repo + ", criterio: " + criterio)
    encontrado = False
    contador = 0
    minLimit = conf.config.SEARCH_TIME_LIMIT  # minutos
    segLimit = minLimit * 60  # segundos
    tIni = time.perf_counter()
    tFin = tIni + 1
    while len(lFicheros) > 0 and (tFin - tIni) <= segLimit:
        tFin = time.perf_counter()
        e = lFicheros.pop(0)
        auxiliares.escribirLog(f, e)
        fActual = auxiliares.obtenerFicheroIt(e)
        if os.path.isdir(e):
            #print(e + "[CARPETA]")
            if criterio == fActual:
                if contador >= conf.config.ITEMS_FOUND_LIMIT:
                    break
                else:
                    auxiliares.escribirLog(f, "Adding " + e)
                    repo = repo.replace("*_*", "/")
                    auxiliares.actualizarDataFrame(criterio, repo, e, df)
                    encontrado = True
                    contador = contador + 1
            else:
                contentAux = os.listdir(e)
                content = obtenerRutaCompletaE(e, contentAux)
                for c in content:
                    lFicheros.insert(0, c)
        elif os.path.isfile(e):
            #print(e + "[FICHERO]")
            if criterio == e.lower():
                if contador >= conf.config.ITEMS_FOUND_LIMIT:
                    break
                else:
                    auxiliares.escribirLog(f, "Adding " + e)
                    repo = repo.replace("*_*", "/")
                    auxiliares.actualizarDataFrame(criterio, repo, e, df)
                    encontrado = True
                    contador = contador + 1
    auxiliares.cerrarLog(f)
    return encontrado

# Busca todas los ficheros/carpetas que contengan en su nombre el value del criterio.
def buscarTodaCarpetaEnRepoLocal2(repo, lFicheros, criterio, df):
    log = conf.config.cLogs + "/log_buscarEnRepoLocal_" + criterio + "_" + conf.config.fechaEjecucion + ".log"
    f = auxiliares.abrirLog(log)
    auxiliares.escribirLog(f, "--> Analizando repositorio: " + repo + ", criterio: " + criterio)
    print("--> Analizando repositorio: " + repo + ", criterio: " + criterio)
    encontrado = False
    contador = 0
    minLimit = conf.config.SEARCH_TIME_LIMIT  # minutos
    segLimit = minLimit * 60  # segundos
    tIni = time.perf_counter()
    tFin = tIni + 1
    while len(lFicheros)>0 and (tFin - tIni) <= segLimit:
        tFin = time.perf_counter()
        e = lFicheros.pop(0)
        auxiliares.escribirLog(f, e)
        fActual = auxiliares.obtenerFicheroIt(e)
        print(e)
        if os.path.isdir(e):
            #print(e + "[CARPETA]")
            if criterio in e.lower():
                if contador >= conf.config.ITEMS_FOUND_LIMIT:
                    lFicheros = []
                    break
                else:
                    auxiliares.escribirLog(f, "Adding " + e)
                    repo = repo.replace("*_*", "/")
                    auxiliares.actualizarDataFrame(criterio, repo, e, df)
                    encontrado = True
                    contador = contador + 1
            else:
                contentAux = os.listdir(e)
                content = obtenerRutaCompletaE(e, contentAux)
                for c in content:
                    lFicheros.insert(0, c)
        elif os.path.isfile(e):
            #print(e + "[FICHERO]")
            if criterio in e.lower():
                if contador >= conf.config.ITEMS_FOUND_LIMIT:
                    break
                else:
                    auxiliares.escribirLog(f, "Adding " + e)
                    repo = repo.replace("*_*", "/")
                    auxiliares.actualizarDataFrame(criterio, repo, e, df)
                    encontrado = True
                    contador = contador + 1
    auxiliares.cerrarLog(f)
    return encontrado

def buscarC10_Local(repo, lFicheros, df):
    log = conf.config.cLogs + "/log_buscarC10Local_" + conf.config.fechaEjecucion + ".log"
    f = auxiliares.abrirLog(log)
    auxiliares.escribirLog(f, "--> Analizando repositorio: " + repo + ", criterio 10" )
    print("--> Analizando repositorio: " + repo + ", criterio 10")
    encontrado = False
    contador = 0
    minLimit = conf.config.SEARCH_TIME_LIMIT  # minutos
    segLimit = minLimit * 60  # segundos
    tIni = time.perf_counter()
    tFin = tIni + 1
    while len(lFicheros) > 0 and (tFin - tIni) <= segLimit:
        tFin = time.perf_counter()
        e = lFicheros.pop(0)
        auxiliares.escribirLog(f, e)
        fActual = auxiliares.obtenerFicheroIt(e)
        print(e)
        if os.path.isdir(e):
            #print(e + "[CARPETA]")
            contentAux = os.listdir(e)
            content = obtenerRutaCompletaE(e, contentAux)
            for c in content:
                lFicheros.insert(0, c)
        elif os.path.isfile(e):
            #print(e + "[FICHERO]")
            if fActual.endswith("IT.java") \
                    or "e2e" in fActual \
                    or "integration_test" in fActual \
                    or "integrationtest" in fActual:
                if contador >= conf.config.ITEMS_FOUND_LIMIT:
                    break
                else:
                    auxiliares.escribirLog(f, "Adding " + e)
                    repo = repo.replace("*_*", "/")
                    auxiliares.actualizarDataFrame(Criterios.criterio10.value, repo, e, df)
                    encontrado = True
                    contador = contador + 1
                    #break
    auxiliares.cerrarLog(f)
    return encontrado

def buscarC11_Local(repo, lFicheros, df):
    log = conf.config.cLogs + "/log_buscarC11Local_" + conf.config.fechaEjecucion + ".log"
    f = auxiliares.abrirLog(log)
    auxiliares.escribirLog(f, "--> Analizando repositorio: " + repo + ", criterio 11")
    print("--> Analizando repositorio: " + repo + ", criterio 10")
    encontrado = False
    contador = 0
    minLimit = conf.config.SEARCH_TIME_LIMIT  # minutos
    segLimit = minLimit * 60  # segundos
    tIni = time.perf_counter()
    tFin = tIni + 1
    while len(lFicheros) > 0 and (tFin - tIni) <= segLimit:
        tFin = time.perf_counter()
        e = lFicheros.pop(0)
        auxiliares.escribirLog(f, e)
        fActual = auxiliares.obtenerFicheroIt(e.lower())
        if os.path.isdir(e):
            #print(e + "[CARPETA]")
            contentAux = os.listdir(e)
            content = obtenerRutaCompletaE(e, contentAux)
            for c in content:
                lFicheros.insert(0, c)
        elif os.path.isfile(e):
            #print(e + "[FICHERO]")
            if "pom.xml" in fActual or "build.xml" in fActual:
                fXml = open(e, 'r', encoding="ISO-8859-1")
                xmlContent = fXml.read()
                fXml.close()
                if "selenium-java" in xmlContent or "rest-assured" in xmlContent:
                    if contador >= conf.config.ITEMS_FOUND_LIMIT:
                        break
                    else:
                        auxiliares.escribirLog(f, "Adding " + e)
                        repo = repo.replace("*_*", "/")
                        auxiliares.actualizarDataFrame(Criterios.criterio11.value, repo, e, df)
                        encontrado = True
                        contador = contador + 1
                        #break
    auxiliares.cerrarLog(f)
    return encontrado

def buscarFicherosCI_Local(repo, lFicheros, df):
    log = conf.config.cLogs + "/log_buscarC12Local_" + conf.config.fechaEjecucion + ".log"
    f = auxiliares.abrirLog(log)
    auxiliares.escribirLog(f, "--> Analizando repositorio: " + repo + ", criterio 12 (ci-files)")
    print("--> Analizando repositorio: " + repo + ", criterio 12 (ci-files)")
    encontrado = False
    contador = 0
    minLimit = conf.config.SEARCH_TIME_LIMIT  # minutos
    segLimit = minLimit * 60  # segundos
    tIni = time.perf_counter()
    tFin = tIni + 1
    while len(lFicheros) > 0 and (tFin - tIni) <= segLimit:
        tFin = time.perf_counter()
        e = lFicheros.pop(0)
        auxiliares.escribirLog(f, e)
        if os.path.isdir(e):
            #print(e + "[CARPETA]")
            contentAux = os.listdir(e)
            content = obtenerRutaCompletaE(e, contentAux)
            for c in content:
                lFicheros.insert(0, c)
        elif os.path.isfile(e):
            #print(e + "[FICHERO]")
            if "jenkinsfile" in e.lower() \
                    or ".travis-ci.yml" in e.lower() \
                    or ".travis.yml" in e.lower() \
                    or ".circle-ci.yml" in e.lower() \
                    or ".circle.yml" in e.lower() \
                    or ".github/workflows/pipeline.yml" in e.lower() \
                    or ".azure-pipelines/pipelines.yml" in e.lower() \
                    or ".gitlab-ci.yml" in e.lower():
                if contador >= conf.config.ITEMS_FOUND_LIMIT:
                    break
                else:
                    auxiliares.escribirLog(f, "Adding " + e)
                    repo = repo.replace("*_*", "/")
                    auxiliares.actualizarDataFrame(Criterios.criterio12.value, repo, e, df)
                    encontrado = True
                    contador = contador + 1
                    #break
    auxiliares.cerrarLog(f)
    return encontrado

# FUNCIONES DE BÚSQUEDA (API de GitHub)
def busquedaGitHubApiRepos(listaRepositorios, df, df2):
    listaEncontrados = []
    for repo in listaRepositorios:
        boC1 = buscarEnRepo(repo, Criterios.criterio1.value, df)
        #boC3 = buscarEnRepo(repo, Criterios.criterio3.value, df)
        #boC5 = buscarEnRepo(repo, Criterios.criterio5.value, df)
        boC3 = False
        boC5 = False

        # Si lo ha encontrado:
        # - lo añadimos a la listaEncontrados.
        encontrado = False
        if boC1 or boC3 or boC5:
            listaEncontrados.append(repo)
            encontrado = True

        if conf.config.actualizarBD:
            print("Actualizando base de datos...")
            repoBBDD = repoBD.createRepoBD()
            repoBBDD.setNombre(repo.full_name.split("/")[1])
            repoBBDD.setOrganizacion(repo.full_name.split("/")[0])
            repoBBDD.setBoE2e(encontrado)
            auxiliares.guardarRepoEnBD(repoBBDD)

        # Actualizamos contadores
        columna = "n_encontrados"
        if boC1:
            df2.at[Criterios.criterio1.value, columna] += 1
        if boC3:
            df2.at[Criterios.criterio3.value, columna] += 1
        if boC5:
            df2.at[Criterios.criterio5.value, columna] += 1

        df2.at["Totales", columna] = auxiliares.contarRepositoriosAlMenos1Criterio(df)

    return listaEncontrados

def buscarEnRepo(repo, criterio, df):
    print("Buscando repositorios recursivamente: '" + criterio + "' en el repo: " + repo.full_name)
    encontrado = False
    log = conf.config.cLogs + "/log_buscarEnRepo_" + criterio + "_" + conf.config.fechaEjecucion + ".log"
    f = auxiliares.abrirLog(log)
    auxiliares.escribirLog(f, "--> Analizando repositorio: " + repo.full_name.split("/")[1])
    contents = repo.get_contents("")
    while contents:
        content_file = contents.pop(0)
        auxiliares.escribirLog(f, str(content_file))
        if criterio in content_file.path.lower():
            auxiliares.escribirLog(f, "Adding " + content_file.path)
            encontrado = True
            auxiliares.actualizarDataFrame(criterio, repo.full_name, content_file.path, df)
            break
        else:
            if content_file.type == "dir":
                contents.extend(repo.get_contents(content_file.path))
    auxiliares.cerrarLog(f)
    return encontrado

def buscarEnRaiz(repo, criterio, df):
    print("Buscando '" + criterio +"' en la raiz del repo: " + repo.full_name)
    encontrado = False
    log = conf.config.cLogs + "/log_buscarEnRaiz_" + criterio + "_" + conf.config.fechaEjecucion + ".log"
    f = auxiliares.abrirLog(log)
    auxiliares.escribirLog(f, "--> Analizando repositorio: " + repo.full_name.split("/")[1])
    contents = repo.get_contents("")
    for content_file in contents:
        auxiliares.escribirLog(f, str(content_file))
        if criterio in content_file.path.lower():
            auxiliares.escribirLog(f, "Adding " + content_file.path)
            encontrado = True
            auxiliares.actualizarDataFrame(criterio, repo.full_name, content_file.path, df)
            break

    auxiliares.cerrarLog(f)
    return encontrado

def buscarEnTests(repo, criterio, df):
    print("Buscando '" + criterio + "' en carpeta test/tests del repo: " + repo.full_name)
    encontrado = False
    log = conf.config.cLogs + "/log_buscarEnTests_" + criterio + "_" + conf.config.fechaEjecucion + ".log"
    f = auxiliares.abrirLog(log)
    auxiliares.escribirLog(f, "--> Analizando repositorio: " + repo.full_name.split("/")[1])
    contents = repo.get_contents("")
    while contents:
        content_file = contents.pop(0)
        if "test" in content_file.path.lower():
            if content_file.type == "dir":
                #contents.extend(repo.get_contents(content_file.path))
                contents = repo.get_contents(content_file.path)
                while contents:
                    content_file = contents.pop(0)
                    if "test/" + criterio in content_file.path.lower() or "tests/" + criterio in content_file.path.lower():
                        auxiliares.escribirLog(f, "Adding " + content_file.path)
                        encontrado = True
                        auxiliares.actualizarDataFrame(criterio, repo.full_name, content_file.path, df)
                        break
            break
    auxiliares.cerrarLog(f)
    return encontrado

def buscarEnSrcTests(repo, criterio, df):
    print("Buscando '" + criterio +"' en carpeta src/test del repo: " + repo.full_name)
    encontrado = False
    log = conf.config.cLogs + "/log_buscarEnSrcTests_" + criterio + "_" + conf.config.fechaEjecucion + ".log"
    f = auxiliares.abrirLog(log)
    auxiliares.escribirLog(f, "--> Analizando repositorio: " + repo.full_name.split("/")[1])
    contents = repo.get_contents("")
    while contents:
        content_file = contents.pop(0)
        if content_file.path.lower() == "src":
            if content_file.type == "dir":
                contents = repo.get_contents(content_file.path)
                while contents:
                    content_file = contents.pop(0)
                    if content_file.path.lower() in ["src/test"]:
                        auxiliares.escribirLog(f, "Accediendo a carpeta " + content_file.path)
                        if content_file.type == "dir":
                            #contents.extend(repo.get_contents(content_file.path))
                            contents = repo.get_contents(content_file.path)
                            while contents:
                                content_file = contents.pop(0)
                                if content_file.type == "dir":
                                    if criterio in content_file.path.lower():
                                        auxiliares.escribirLog(f, "Adding " + content_file.path)
                                        encontrado = True
                                        auxiliares.actualizarDataFrame(criterio, repo.full_name, content_file.path, df)
                                        break
                                    else:
                                        contents.extend(repo.get_contents(content_file.path))
                        break
    auxiliares.cerrarLog(f)
    return encontrado

# Criterio 10:
def buscarC10(repo, df):
    print("Iniciando criterio de búsqueda nº 10 en el repo: " + repo.full_name)
    encontrado = False
    log = conf.config.cLogs + "/log_buscarC10_" + conf.config.fechaEjecucion + ".log"
    f = auxiliares.abrirLog(log)
    auxiliares.escribirLog(f, "--> Analizando repositorio: " + repo.full_name.split("/")[1])
    contents = repo.get_contents("")
    while contents:
        content_file = contents.pop(0)
        auxiliares.escribirLog(f, str(content_file))
        if "test" in content_file.path.lower() or "tests" in content_file.path.lower():
            if content_file.type == "dir":
                auxiliares.escribirLog(f, "Accediendo a carpeta " + content_file.path)
                contents2 = repo.get_contents(content_file.path)
                while contents2:
                    content_file = contents2.pop(0)
                    auxiliares.escribirLog(f, str(content_file))

                    # Obtenemos el fichero en el que nos encontramos, no la ruta completa.
                    fActual = auxiliares.obtenerFicheroIt(content_file.path.lower())

                    if fActual.endswith("it") \
                            or fActual.startswith("it") \
                            or "e2e" in fActual \
                            or "system" in fActual \
                            or "itest" in fActual:
                        auxiliares.escribirLog(f, "Adding " + content_file.path)
                        encontrado = True
                        auxiliares.actualizarDataFrame(Criterios.criterio10.value, repo.full_name, content_file.path, df)
                        break
            break

    auxiliares.cerrarLog(f)
    return encontrado

# Criterio 11:
def buscarC11(repo, df):
    print("Iniciando criterio de búsqueda nº 11 en el repo: " + repo.full_name)
    encontrado = False
    log = conf.config.cLogs + "/log_buscarC11_" + conf.config.fechaEjecucion + ".log"
    f = auxiliares.abrirLog(log)
    auxiliares.escribirLog(f, "--> Analizando repositorio: " + repo.full_name.split("/")[1])
    contents = repo.get_contents("")
    while contents:
        content_file = contents.pop(0)

        # Con esto se consigue que busque el fichero "pom.xml" y "build.xml" y no que contenga dichos literales.
        # Por ejemplo: HolaQueTal_pom.xml no lo tendría en cuenta. ¿Debería tenerlos en cuenta?
        # Obtenemos el fichero en el que nos encontramos, no la ruta completa.
        fActual = auxiliares.obtenerFicheroIt(content_file.path.lower())

        if "pom.xml" in fActual:
            try:
                decoded = auxiliares.getFileContent(repo, content_file.path)
                isSelenium = 'selenium' in str(decoded)
                isRestassured = 'rest-assured' in str(decoded)
                if isSelenium or isRestassured:
                    auxiliares.escribirLog(f, "Adding " + content_file.path)
                    encontrado = True
                    auxiliares.actualizarDataFrame(Criterios.criterio11.value, repo.full_name, content_file.path, df)
                    break
                else:
                    auxiliares.escribirLog(f, "Literales 'selenium' y 'rest-assured' no encontrados")
                    #Con el siguiente break el programa solamente comprobaría el primer 'pom.xml' que encuentre.
                    #Quitándolo, si el primer 'pom.xml' que encuentre no es ni selenium ni restassured, seguiría buscando algún 'pom.xml' que cumpla la condición.
                    break
            except:
                auxiliares.escribirLog(f, "Error obteniendo el contenido del pom.xml")
                raise
        elif "build.xml" in fActual:
            try:
                decoded = auxiliares.getFileContent(repo, content_file.path)
                isSelenium = 'selenium' in str(decoded)
                isRestassured = 'restassured' in str(decoded)
                if isSelenium or isRestassured:
                    auxiliares.escribirLog(f, "Adding " + content_file.path)
                    encontrado = True
                    auxiliares.actualizarDataFrame(Criterios.criterio11.value, repo.full_name, content_file.path, df)
                    break
                else:
                    auxiliares.escribirLog(f, "Literales 'selenium' y 'rest-assured' no encontrados")
                    # Con el siguiente break el programa solamente comprobaría el primer 'build.xml' que encuentre.
                    # Quitándolo, si el primer 'build.xml' que encuentre no es ni selenium ni restassured, seguiría buscando algún 'build.xml' que cumpla la condición.
                    break
            except:
                auxiliares.escribirLog(f, "Error obteniendo el contenido del build.xml")
                raise
        else:
            if content_file.type == "dir":
                contents.extend(repo.get_contents(content_file.path))

    auxiliares.cerrarLog(f)
    return encontrado