#CRITERIOS

#Importamos las librerías necesarias.
import auxiliares
import datetime

date = str(datetime.datetime.now())[0:19].replace(" ", "_")
carpetalogs = "logs"

def buscarEnRepo(listaRepositorios, criterio):
    print("Buscando repositorios recursivamente: '" + criterio +"'")
    repos = []
    log = carpetalogs + "/log_buscarEnRepo_" + criterio + "_" + date + ".log"
    f = open(log, "w")

    for repo in listaRepositorios:
        f.write("--> Analizando repositorio: " + repo.full_name.split("/")[1])
        f.write("\n")
        contents = repo.get_contents("")
        while contents:
            content_file = contents.pop(0)
            f.write(str(content_file))
            f.write("\n")
            if criterio in content_file.path.lower():
                f.write("Adding " + content_file.path)
                f.write("\n")
                repos.append(repo)
                break
            else:
                if content_file.type == "dir":
                    contents.extend(repo.get_contents(content_file.path))

    print("Total de repositorios filtrados según el criterio: %d" % len(repos))
    f.close()
    auxiliares.imprimirListaRepositorios(repos)
    return repos

def buscarEnRaiz(listaRepositorios, criterio):
    print("Buscando repositorios: '" + criterio +"' en la raiz")
    repos = []
    log = carpetalogs + "/log_buscarEnRaiz_" + criterio + "_" + date + ".log"
    f = open(log, "w")

    for repo in listaRepositorios:
        f.write("--> Analizando repositorio: " + repo.full_name.split("/")[1])
        f.write("\n")
        contents = repo.get_contents("")
        for content_file in contents:
            f.write(str(content_file))
            f.write("\n")
            if criterio in content_file.path.lower():
                f.write("Adding " + content_file.path)
                f.write("\n")
                repos.append(repo)
                break

    print("Total de repositorios filtrados según el criterio: %d" % len(repos))
    f.close()
    auxiliares.imprimirListaRepositorios(repos)
    return repos

def buscarEnTests(listaRepositorios, criterio):
    print("Buscando repositorios: '" + criterio + "' en carpeta test/tests")
    repos = []
    log = carpetalogs + "/log_buscarEnTests_" + criterio + "_" + date + ".log"
    f = open(log, "w")

    for repo in listaRepositorios:
        f.write("--> Analizando repositorio: " + repo.full_name.split("/")[1])
        f.write("\n")
        contents = repo.get_contents("")
        while contents:
            content_file = contents.pop(0)
            #print(content_file)
            f.write(str(content_file))
            f.write("\n")
            if "test" in content_file.path.lower():
                if content_file.type == "dir":
                    #contents.extend(repo.get_contents(content_file.path))
                    contents = repo.get_contents(content_file.path)
                    while contents:
                        content_file = contents.pop(0)
                        #print(content_file)
                        f.write(str(content_file))
                        f.write("\n")
                        if "test/" + criterio in content_file.path.lower() or "tests/" + criterio in content_file.path.lower():
                            #print("Adding " + content_file.path)
                            f.write("Adding " + content_file.path)
                            f.write("\n")
                            repos.append(repo)
                            break
                break
        f.write("\n")

    print("Total de repositorios filtrados según el criterio: %d" % len(repos))
    f.close()
    auxiliares.imprimirListaRepositorios(repos)
    return repos

def buscarEnSrcTests(listaRepositorios, criterio):
    print("Buscando repositorios: '" + criterio +"' en carpeta src/test")
    repos = []
    log = carpetalogs + "/log_buscarEnSrcTests_" + criterio + "_" + date + ".log"
    f = open(log, "w")

    for repo in listaRepositorios:
        f.write("--> Analizando repositorio: " + repo.full_name.split("/")[1])
        f.write("\n")
        contents = repo.get_contents("")
        while contents:
            content_file = contents.pop(0)
            f.write(str(content_file))
            f.write("\n")
            if content_file.path.lower() == "src":
                if content_file.type == "dir":
                    #contents.extend(repo.get_contents(content_file.path))
                    contents = repo.get_contents(content_file.path)
                    while contents:
                        content_file = contents.pop(0)
                        f.write(str(content_file))
                        f.write("\n")
                        if content_file.path.lower() in ["src/test"]:
                            f.write("Accediendo a carpeta " + content_file.path)
                            f.write("\n")
                            if content_file.type == "dir":
                                #contents.extend(repo.get_contents(content_file.path))
                                contents = repo.get_contents(content_file.path)
                                while contents:
                                    content_file = contents.pop(0)
                                    f.write(str(content_file))
                                    f.write("\n")
                                    if content_file.type == "dir":
                                        if criterio in content_file.path.lower():
                                            f.write("Adding " + content_file.path)
                                            f.write("\n")
                                            repos.append(repo)
                                            break
                                        else:
                                            contents.extend(repo.get_contents(content_file.path))
                            break
        f.write("\n")

    print("Total de repositorios filtrados según el criterio: %d" % len(repos))
    f.close()
    auxiliares.imprimirListaRepositorios(repos)
    return repos

# Criterio 9:
def buscarC9(listaRepositorios):
    print("Iniciando criterio de búsqueda nº 9...")
    repos = []
    log = carpetalogs + "/log_buscarC9_" + date + ".log"
    f = open(log, "w")

    for repo in listaRepositorios:
        f.write("--> Analizando repositorio: " + repo.full_name.split("/")[1])
        f.write("\n")
        contents = repo.get_contents("")
        while contents:
            content_file = contents.pop(0)
            f.write(str(content_file))
            f.write("\n")
            if "swagger" in content_file.path.lower():
                f.write("Adding " + content_file.path)
                f.write("\n")
                repos.append(repo)
                break
            else:
                if content_file.type == "dir":
                    contents.extend(repo.get_contents(content_file.path))

    print("Total repositories (criterio 9): %d" % len(repos))
    auxiliares.imprimirListaRepositorios(repos)
    return repos

# Criterio 10:
def buscarC10(listaRepositorios):
    print("Iniciando criterio de búsqueda nº 10...")
    repos = []
    log = carpetalogs + "/log_buscarC10_" + date + ".log"
    f = open(log, "w")

    for repo in listaRepositorios:
        f.write("--> Analizando repositorio: " + repo.full_name.split("/")[1])
        f.write("\n")
        contents = repo.get_contents("")
        while contents:
            content_file = contents.pop(0)
            f.write(str(content_file))
            f.write("\n")
            if "test" in content_file.path.lower() or "tests" in content_file.path.lower():
                if content_file.type == "dir":
                    f.write("Accediendo a carpeta " + content_file.path)
                    f.write("\n")
                    contents.extend(repo.get_contents(content_file.path))
                    while contents:
                        content_file = contents.pop(0)
                        f.write(str(content_file))
                        f.write("\n")
                        if "it" in content_file.path.lower() \
                                or "e2e" in content_file.path.lower() \
                                or "system" in content_file.path.lower() \
                                or "itest" in content_file.path.lower():
                            f.write("Adding " + content_file.path)
                            f.write("\n")
                            repos.append(repo)
                            break
                break

    print("Total repositories (criterio 10): %d" % len(repos))
    auxiliares.imprimirListaRepositorios(repos)
    return repos

# Criterio 11:
def buscarC11(listaRepositorios):
    print("Iniciando criterio de búsqueda nº 11...")
    repos = []
    log = carpetalogs + "/log_buscarC11_" + date + ".log"
    f = open(log, "w")

    for repo in listaRepositorios:
        f.write("--> Analizando repositorio: " + repo.full_name.split("/")[1])
        f.write("\n")
        contents = repo.get_contents("")
        while contents:
            content_file = contents.pop(0)
            f.write(str(content_file))
            f.write("\n")
            if "pom.xml" in content_file.path.lower():
                isSelenium = 'selenium' in str(repo.get_contents("pom.xml").decoded_content)
                isRestassured = 'restassured' in str(repo.get_contents("pom.xml").decoded_content)
                if isSelenium or isRestassured:
                    f.write("Adding " + content_file.path)
                    f.write("\n")
                    repos.append(repo)
                    break
            elif "build.xml" in content_file.path.lower():
                isSelenium = 'selenium' in str(repo.get_contents("build.xml").decoded_content)
                isRestassured = 'restassured' in str(repo.get_contents("build.xml").decoded_content)
                if isSelenium or isRestassured:
                    f.write("Adding " + content_file.path)
                    f.write("\n")
                    repos.append(repo)
                    break
            else:
                if content_file.type == "dir":
                    contents.extend(repo.get_contents(content_file.path))

    print("Total repositories (criterio 11): %d" % len(repos))
    auxiliares.imprimirListaRepositorios(repos)
    return repos