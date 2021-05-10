import main
import configuracion as conf
import filtrosQuery as fq
import tkinter as tk
from tkinter import ttk
from tkinter import font
from tkinter import messagebox
from PIL import Image
from PIL import ImageTk
import pruebas
import repoBD
import executeQuery
import datetime

app = tk.Tk()
app.title("BuscadorGitHubRepos")
width = '650'
height = '700'
app.geometry(width + 'x' + height)
app.resizable(False, False)

nb = ttk.Notebook(app)
nb.pack(fill='both', expand='yes')

backgroudLblColor = "gray92"

p1 = ttk.Frame(nb)
p2 = ttk.Frame(nb)
p3 = ttk.Frame(nb)

# STATE (Credenciales)
user_state = tk.StringVar()
token_state = tk.StringVar()

# STATE (Filtros Query)
lenguaje_state = tk.StringVar()
stars_state = tk.StringVar()
forks_state = tk.StringVar()
created_state = tk.StringVar()
pushed_state = tk.StringVar()
archivedCheck_state = tk.BooleanVar()
publicCheck_state = tk.BooleanVar()
sizeLimit_state = tk.IntVar()

# STATE (Variables de configuración)
nRandomRepos_state = tk.IntVar()
nLapseRepos_state = tk.IntVar()
actualizarBDCheck_state = tk.BooleanVar()
buscarEnLocalCheck_state = tk.BooleanVar()
generarListaReposCheck_state = tk.BooleanVar()
randomizarReposCheck_state = tk.BooleanVar()
clonarReposCheck_state = tk.BooleanVar()
doExcelCheck_state = tk.BooleanVar()
doCsvCheck_state = tk.BooleanVar()
escribirEnLogCheck_state = tk.BooleanVar()
scriptLapseExeCheck_state = tk.BooleanVar()

# STATE (Base de datos)
nombreRepoBD_state = tk.StringVar()
organizacionBD_state = tk.StringVar()
lenguajeBD_state = tk.StringVar()
commitIdBD_state = tk.StringVar()
sizeBD_state = tk.IntVar()
boE2eCheck_state = tk.BooleanVar()

# STATE (Pruebas)
organizacion_state = tk.StringVar()
nombreRepo_state = tk.StringVar()

def exe():
    print("Ejecutando proceso desde buscador-UI")
    # Filtros Query:
    fq.filtrosQuery.language = lenguaje_state.get().lower()
    fq.filtrosQuery.stars = stars_state.get()
    fq.filtrosQuery.forks = forks_state.get()
    fq.filtrosQuery.created = created_state.get()
    fq.filtrosQuery.pushed = pushed_state.get()

    if archivedCheck_state.get():
        fq.filtrosQuery.qIs = "true"
    else:
        fq.filtrosQuery.qIs = "false"

    if publicCheck_state.get():
        fq.filtrosQuery.qIs = "public"
    else:
        fq.filtrosQuery.qIs = "private"

    # Configuración
    conf.config.fechaEjecucion = str(datetime.datetime.now())[0:19].replace(" ", "_").replace(":", "h", 1).replace(":", "m", 1) + "s"
    conf.config.actualizarBD = actualizarBDCheck_state.get()
    conf.config.buscarEnLocal = buscarEnLocalCheck_state.get()
    conf.config.generarListaRepos = generarListaReposCheck_state.get()
    conf.config.randomizarListaRepos = randomizarReposCheck_state.get()
    conf.config.lapseExe = conf.config.lapseExe
    conf.config.clonarRepositorios = clonarReposCheck_state.get()
    conf.config.doExcel = doExcelCheck_state.get()
    conf.config.doCsv = doCsvCheck_state.get()
    conf.config.escribirEnLog = escribirEnLogCheck_state.get()
    conf.config.N_RANDOM = nRandomRepos_state.get()
    conf.config.N_LAPSE_REPOS = conf.config.N_LAPSE_REPOS
    conf.config.REPO_SIZE_LIMIT = sizeLimit_state.get()
    main.exe()
    messagebox.showinfo(message="Proceso finalizado", title="Aviso")

def ejecutaPrueba():
    pruebas.RepoPruebas.organizacion = organizacion_state.get()
    pruebas.RepoPruebas.nombre = nombreRepo_state.get()
    pruebas.ejecutaPrueba()
    messagebox.showinfo(message="Prueba finalizada", title="Aviso")

def consultarBD():
    print("Consultando base de datos...")
    repo = repoBD.createRepoBD()
    repo.setNombre(nombreRepoBD_state.get())
    repo.setOrganizacion(organizacionBD_state.get())
    repo.setLenguaje(lenguajeBD_state.get())
    repo.setSize(sizeBD_state.get())
    repo.setCommitID(commitIdBD_state.get())
    repo.setBoE2e(boE2eCheck_state.get())
    repo.setTstbd("")

    query = repo.getFiltro()

    print(query)

    filas = executeQuery.execute(query)

    for fila in filas:
        id = fila["idrepo"]
        nombre = fila["nombre"]
        organizacion = fila["organizacion"]
        url = fila["url"]
        listadoBD.insert(0, "[" + str(id) + "]" +organizacion + "/" + nombre + ": " + "'" + url + "'")

def randomizarReposCheck_clicked():
    if randomizarReposCheck_state.get():
        nRandomRepos_state.set(conf.config.N_RANDOM)
        nRandomRepos.config(state=tk.NORMAL)
    else:
        nRandomRepos_state.set(0)
        nRandomRepos.config(state=tk.DISABLED)

def limpiarResultados():
    print("Limpiando base de datos...")
    listadoBD.delete(0, tk.END)

# PESTAÑA 1

row = 0

# LOGO URJC
logoUrjcWidth = 120
logoUrjcHeight = 60
img = Image.open("imgs/logo_urjc2.png")
img = img.resize((logoUrjcWidth,logoUrjcHeight), Image.ANTIALIAS)
photoImg = ImageTk.PhotoImage(img)
widget = tk.Label(p1, image=photoImg, bg=backgroudLblColor)
widget.grid(column=0, row=row)
titleAppLbl = tk.Label(p1, text="BuscadorGitHubRepos", font=('Helvetica', 18, 'bold'), bg=backgroudLblColor)
titleAppLbl.grid(column=1, row=row)
f = font.Font(titleAppLbl, titleAppLbl.cget("font"))
f.configure(underline=True)
titleAppLbl.configure(font=f)
row+=1

# CREDENCIALES
credencialesLbl = tk.Label(p1, text="CREDENCIALES", bg=backgroudLblColor)
credencialesLbl.grid(column=0, row=row)
f = font.Font(credencialesLbl, credencialesLbl.cget("font"))
f.configure(underline=True)
credencialesLbl.configure(font=f)
row+=1

userLbl = tk.Label(p1, text="Usuario: ", bg=backgroudLblColor)
userLbl.grid(column=0, row=row)
user_state.set(conf.config.user)
user = tk.Entry(p1,width=15, textvariable=user_state)
user.grid(column=1, row=row)
row+=1

tokenLbl = tk.Label(p1, text="Token: ", bg=backgroudLblColor)
tokenLbl.grid(column=0, row=row)
token_state.set(conf.config.token)
token = tk.Entry(p1,width=34, textvariable=token_state)
token.grid(column=1, row=row)
row+=1

# FILTROS QUERY
filtrosQueryLbl = tk.Label(p1, text="FILTROS QUERY", bg=backgroudLblColor)
filtrosQueryLbl.grid(column=0, row=row)
f = font.Font(filtrosQueryLbl, filtrosQueryLbl.cget("font"))
f.configure(underline=True)
filtrosQueryLbl.configure(font=f)
row+=1

# LENGUAJE
lenguajeLbl = tk.Label(p1, text="Lenguaje: ", bg=backgroudLblColor)
lenguajeLbl.grid(column=0, row=row)
lenguaje_state.set(fq.filtrosQuery.language)
lenguaje = tk.Entry(p1, width=15, textvariable=lenguaje_state)
lenguaje.grid(column=1, row=row)
row+=1

# STARS
starsLbl = tk.Label(p1, text="Stars: ", bg=backgroudLblColor)
starsLbl.grid(column=0, row=row)
stars_state.set(fq.filtrosQuery.stars)
stars = tk.Entry(p1, width=15, textvariable=stars_state)
stars.grid(column=1, row=row)
row+=1

# FORKS
forksLbl = tk.Label(p1, text="Forks: ", bg=backgroudLblColor)
forksLbl.grid(column=0, row=row)
forks_state.set(fq.filtrosQuery.forks)
forks = tk.Entry(p1, width=15, textvariable=forks_state)
forks.grid(column=1, row=row)
row+=1

# CREATED
createdLbl = tk.Label(p1, text="Created: ", bg=backgroudLblColor)
createdLbl.grid(column=0, row=row)
created_state.set(fq.filtrosQuery.created)
created = tk.Entry(p1, width=15, textvariable=created_state)
created.grid(column=1, row=row)
row+=1

# PUSHED
pushedLbl = tk.Label(p1, text="Pushed: ", bg=backgroudLblColor)
pushedLbl.grid(column=0, row=row)
pushed_state.set(fq.filtrosQuery.pushed)
pushed = tk.Entry(p1, width=15, textvariable=pushed_state)
pushed.grid(column=1, row=row)
row+=1

# ARCHIVED
archivedLbl = tk.Label(p1, text="Archived", bg=backgroudLblColor)
archivedLbl.grid(column=0, row=row)
archivedCheck_state.set(False)
archivedCheck = tk.Checkbutton(p1, var=archivedCheck_state, bg=backgroudLblColor)
archivedCheck.grid(column=1, row=row)
archivedCheck.config(state=tk.DISABLED)
row+=1

# PUBLIC
publicLbl = tk.Label(p1, text="Public", bg=backgroudLblColor)
publicLbl.grid(column=0, row=row)
publicCheck_state.set(True)
publicCheck = tk.Checkbutton(p1, var=publicCheck_state, bg=backgroudLblColor)
publicCheck.grid(column=1, row=row)
publicCheck.config(state=tk.DISABLED)
row+=1

# SIZE LIMIT
sizeLimitLbl = tk.Label(p1, text="Size Limit (kilobytes): ", bg=backgroudLblColor)
sizeLimitLbl.grid(column=0, row=row)
sizeLimit_state.set(conf.config.REPO_SIZE_LIMIT)
sizeLimit = tk.Entry(p1, width=7, textvariable=sizeLimit_state)
sizeLimit.grid(column=1, row=row)
sizeLimit.config(state=tk.DISABLED)
row+=1

# VARIABLES DE CONFIGURACIÓN
configuracionLbl = tk.Label(p1, text="VARIABLES DE CONFIGURACIÓN", bg=backgroudLblColor)
configuracionLbl.grid(column=0, row=row)
f = font.Font(configuracionLbl, configuracionLbl.cget("font"))
f.configure(underline=True)
configuracionLbl.configure(font=f)
row+=1

# ACTUALIZAR BD
actualizarBDLbl = tk.Label(p1, text="Actualizar BD", bg=backgroudLblColor)
actualizarBDLbl.grid(column=0, row=row)
actualizarBDCheck_state.set(conf.config.actualizarBD)
actualizarBDCheck = tk.Checkbutton(p1, var=actualizarBDCheck_state, bg=backgroudLblColor)
actualizarBDCheck.grid(column=1, row=row)
row+=1

# BUSCAR REPOS EN LOCAL
buscarEnLocalReposLbl = tk.Label(p1, text="Buscar repos en LOCAL", bg=backgroudLblColor)
buscarEnLocalReposLbl.grid(column=0, row=row)
buscarEnLocalCheck_state.set(conf.config.buscarEnLocal)
buscarEnLocalCheck = tk.Checkbutton(p1, var=buscarEnLocalCheck_state, bg=backgroudLblColor)
buscarEnLocalCheck.grid(column=1, row=row)
row+=1

# GENERAR LISTA REPOS
generarListaReposLbl = tk.Label(p1, text="Generar lista repos ('.pickle')", bg=backgroudLblColor)
generarListaReposLbl.grid(column=0, row=row)
generarListaReposCheck_state.set(conf.config.generarListaRepos)
generarListaReposCheck = tk.Checkbutton(p1, var=generarListaReposCheck_state, bg=backgroudLblColor)
generarListaReposCheck.grid(column=1, row=row)
row+=1

# ScriptLapseExe
scriptLapseExeLbl = tk.Label(p1, text="Ejecutar mediante 'ScriptLapseExe'", bg=backgroudLblColor)
scriptLapseExeCheck_state.set(conf.config.lapseExe)
scriptLapseExeCheck = tk.Checkbutton(p1, var=scriptLapseExeCheck_state, bg=backgroudLblColor)

# Nº LAPSE REPOS
nLapseRepos_state.set(conf.config.N_LAPSE_REPOS)
nLapseRepos = tk.Entry(p1, width=5, textvariable=nLapseRepos_state)
row+=1

# RANDOMIZAR REPOSITORIOS
randomizarReposLbl = tk.Label(p1, text="Randomizar repositorios", bg=backgroudLblColor)
randomizarReposLbl.grid(column=0, row=row)
randomizarReposCheck_state.set(conf.config.randomizarListaRepos)
randomizarReposCheck = tk.Checkbutton(p1, var=randomizarReposCheck_state, command=randomizarReposCheck_clicked, bg=backgroudLblColor)
randomizarReposCheck.grid(column=1, row=row)

# Nº REPOS RANDOM
nRandomRepos_state.set(conf.config.N_RANDOM)
nRandomRepos = tk.Entry(p1, width=5, textvariable=nRandomRepos_state)
nRandomRepos.grid(column=2, row=row)
row+=1

# CLONAR REPOSITORIOS
clonarReposLbl = tk.Label(p1, text="Clonar repositorios resultantes", bg=backgroudLblColor)
clonarReposLbl.grid(column=0, row=row)
clonarReposCheck_state.set(conf.config.clonarRepositorios)
clonarReposCheck = tk.Checkbutton(p1, var=clonarReposCheck_state, bg=backgroudLblColor)
clonarReposCheck.grid(column=1, row=row)
row+=1

# DO EXCEL
doExcelLbl = tk.Label(p1, text="Generar Excel", bg=backgroudLblColor)
doExcelLbl.grid(column=0, row=row)
doExcelCheck_state.set(conf.config.doExcel)
doExcelCheck = tk.Checkbutton(p1, var=doExcelCheck_state, bg=backgroudLblColor)
doExcelCheck.grid(column=1, row=row)
row+=1

# DO CSV
doCsvLbl = tk.Label(p1, text="Generar Csv", bg=backgroudLblColor)
doCsvLbl.grid(column=0, row=row)
doCsvCheck_state.set(conf.config.doCsv)
doCsvCheck = tk.Checkbutton(p1, var=doCsvCheck_state, bg=backgroudLblColor)
doCsvCheck.grid(column=1, row=row)
row+=1

# ESCRIBIR EN LOG
escribirEnLogLbl = tk.Label(p1, text="Escribir en LOG", bg=backgroudLblColor)
escribirEnLogLbl.grid(column=0, row=row)
escribirEnLogCheck_state.set(conf.config.escribirEnLog)
escribirEnLogCheck = tk.Checkbutton(p1, var=escribirEnLogCheck_state, bg=backgroudLblColor)
escribirEnLogCheck.grid(column=1, row=row)
row+=1

# BOTÓN EJECUTAR
exeButton = tk.Button(p1, text="EJECUTAR", fg="green",  command=exe, bg=backgroudLblColor)
exeButton.grid(column=1, row=row)
row+=1

# PESTAÑA 2

row = 0

# CONSULTAR BD
consultarBdLbl = tk.Label(p2, text="CONSULTAR BD", font=('Helvetica', 18, 'bold'), bg=backgroudLblColor)
consultarBdLbl.grid(column=0, row=row)
f = font.Font(consultarBdLbl, consultarBdLbl.cget("font"))
f.configure(underline=True)
consultarBdLbl.configure(font=f)
row+=1

# NOMBRE REPO BD
nombreRepoBDLbl = tk.Label(p2, text="Nombre repositorio: ", bg=backgroudLblColor)
nombreRepoBDLbl.grid(column=0, row=row)
nombreRepoBD_state.set("")
nombreRepoBD = tk.Entry(p2, width=15, textvariable=nombreRepoBD_state)
nombreRepoBD.grid(column=1, row=row)
row+=1

# ORGANIZACION BD
organizacionBDLbl = tk.Label(p2, text="Organizacion: ", bg=backgroudLblColor)
organizacionBDLbl.grid(column=0, row=row)
organizacionBD_state.set("")
organizacionBD = tk.Entry(p2, width=15, textvariable=organizacionBD_state)
organizacionBD.grid(column=1, row=row)
row+=1

# LENGUAJE BD
lenguajeBDLbl = tk.Label(p2, text="Lenguaje: ", bg=backgroudLblColor)
lenguajeBDLbl.grid(column=0, row=row)
lenguajeBD_state.set("")
lenguajeBD = tk.Entry(p2, width=15, textvariable=lenguajeBD_state)
lenguajeBD.grid(column=1, row=row)
row+=1

# COMMIT ID BD
commitIdBDLbl = tk.Label(p2, text="Commit ID: ", bg=backgroudLblColor)
commitIdBDLbl.grid(column=0, row=row)
commitIdBD_state.set("")
commitIdBD = tk.Entry(p2, width=15, textvariable=commitIdBD_state)
commitIdBD.grid(column=1, row=row)
row+=1

# SIZE BD
sizeBDLbl = tk.Label(p2, text="Tamaño (kilobytes): ", bg=backgroudLblColor)
sizeBDLbl.grid(column=0, row=row)
sizeBD_state.set(0)
sizeBD = tk.Entry(p2, width=15, textvariable=sizeBD_state)
sizeBD.grid(column=1, row=row)
row+=1

# CON E2E
boE2eLbl = tk.Label(p2, text="Con e2e", bg=backgroudLblColor)
boE2eLbl.grid(column=0, row=row)
boE2eCheck_state.set(True)
boE2eCheck = tk.Checkbutton(p2, var=boE2eCheck_state, bg=backgroudLblColor)
boE2eCheck.grid(column=1, row=row)
row+=1

# BOTÓN CONSULTA BBDD
consultaBDButton = tk.Button(p2, text="CONSULTAR BD", fg="green",  command=consultarBD, bg=backgroudLblColor)
consultaBDButton.grid(column=1, row=row)
row+=1

# Resultado de la búsqueda
resultadoLbl = tk.Label(p2, text="Resultado de la consulta:", bg=backgroudLblColor)
resultadoLbl.grid(column=1, row=row)
f = font.Font(resultadoLbl, resultadoLbl.cget("font"))
f.configure(underline=True)
resultadoLbl.configure(font=f)
row+=1
scrollbar = ttk.Scrollbar(p2, orient=tk.VERTICAL)
listadoBD = tk.Listbox(p2, borderwidth=1, yscrollcommand=scrollbar.set, width = 40)
listadoBD.grid(column=1, row=row)
row+=1

# BOTÓN LIMPIAR RESULTADOS
limpiarResultadosButton = tk.Button(p2, text="Limpiar", fg="black",  command=limpiarResultados, bg=backgroudLblColor)
limpiarResultadosButton.grid(column=1, row=row)
row+=1

# PESTAÑA 3

row = 0

# PRUEBAS
pruebasLbl = tk.Label(p3, text="PRUEBAS", font=('Helvetica', 18, 'bold'), bg=backgroudLblColor)
pruebasLbl.grid(column=0, row=row)
f = font.Font(pruebasLbl, pruebasLbl.cget("font"))
f.configure(underline=True)
pruebasLbl.configure(font=f)
row+=1

# ORGANIZACION
organizacionLbl = tk.Label(p3, text="Organización: ", bg=backgroudLblColor)
organizacionLbl.grid(column=0, row=row)
organizacion_state.set(pruebas.RepoPruebas.organizacion)
organizacion = tk.Entry(p3, width=15, textvariable=organizacion_state)
organizacion.grid(column=1, row=row)
row+=1

# NOMBRE REPO
nombreRepoLbl = tk.Label(p3, text="Nombre: ", bg=backgroudLblColor)
nombreRepoLbl.grid(column=0, row=row)
nombreRepo_state.set(pruebas.RepoPruebas.organizacion)
nombreRepo = tk.Entry(p3, width=15, textvariable=nombreRepo_state)
nombreRepo.grid(column=1, row=row)
row+=1

# BOTÓN EJECUTAR PRUEBA
ejecutaPruebaButton = tk.Button(p3, text="REALIZAR PRUEBA", fg="green",  command=ejecutaPrueba, bg=backgroudLblColor)
ejecutaPruebaButton.grid(column=1, row=row)
row+=1


nb.add(p1, text='Buscador')
nb.add(p2, text='BBDD')
nb.add(p3, text='PRUEBAS')

randomizarReposCheck_clicked()

app.mainloop()