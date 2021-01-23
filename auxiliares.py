#FUNCIONES AUXILIARES

#Importamos las librerías necesarias.
import os
import pickle

def imprimirListaRepositorios(repositorios):
    for project in repositorios:
        project_name = project.full_name.split("/")[1]
        print(project.full_name)

def imprimirRepositorio(project):
    project_name = project.full_name.split("/")[1]
    print(project.full_name)

def cargarRepositorios(fichero):
    with open(fichero, 'rb') as f:
        repositories = pickle.load(f)
    return repositories

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