import main
import configuracion as conf
import tkinter as tk
from tkinter import ttk
from tkinter import font
from PIL import Image
from PIL import ImageTk
import pruebas

app = tk.Tk()
app.title("BuscadorGitHubRepos")
width = '650'
height = '650'
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
buscarEnLocalCheck_state = tk.BooleanVar()
generarListaReposCheck_state = tk.BooleanVar()
randomizarReposCheck_state = tk.BooleanVar()
clonarReposCheck_state = tk.BooleanVar()
doExcelCheck_state = tk.BooleanVar()
doCsvCheck_state = tk.BooleanVar()
scriptLapseExeCheck_state = tk.BooleanVar()

# STATE (Base de datos)
nombreRepoBD_state = tk.StringVar()
organizacionBD_state = tk.StringVar()
commitIdBD_state = tk.StringVar()
sizeBD_state = tk.IntVar()

# STATE (Pruebas)
organizacion_state = tk.StringVar()
nombreRepo_state = tk.StringVar()

def exe():
    print("Ejecutando proceso desde buscador-UI")
    # Filtros Query:
    conf.FiltrosQuery.language = lenguaje_state.get().lower()
    conf.FiltrosQuery.stars = stars_state.get()
    conf.FiltrosQuery.forks = forks_state.get()
    conf.FiltrosQuery.created = created_state.get()
    conf.FiltrosQuery.pushed = pushed_state.get()

    if archivedCheck_state.get():
        conf.FiltrosQuery.qIs = "true"
    else:
        conf.FiltrosQuery.qIs = "false"

    if publicCheck_state.get():
        conf.FiltrosQuery.qIs = "public"
    else:
        conf.FiltrosQuery.qIs = "private"

    # Configuración
    conf.Configuracion.buscarEnLocal = buscarEnLocalCheck_state.get()
    conf.Configuracion.generarListaRepos = generarListaReposCheck_state.get()
    conf.Configuracion.randomizarListaRepos = randomizarReposCheck_state.get()
    conf.Configuracion.lapseExe = False
    conf.Configuracion.clonarRepositorios = clonarReposCheck_state.get()
    conf.Configuracion.doExcel = doExcelCheck_state.get()
    conf.Configuracion.doCsv = doCsvCheck_state.get()
    conf.Configuracion.N_RANDOM = nRandomRepos_state.get()
    conf.Configuracion.N_LAPSE_REPOS = 0
    conf.Configuracion.REPO_SIZE_LIMIT = sizeLimit_state.get()
    main.exe()

def ejecutaPrueba():
    pruebas.RepoPruebas.organizacion = organizacion_state.get()
    pruebas.RepoPruebas.nombre = nombreRepo_state.get()
    pruebas.ejecutaPrueba()

def consultarBD():
    print("Consultando base de datos...")

def randomizarReposCheck_clicked():
    if randomizarReposCheck_state.get():
        nRandomRepos_state.set(conf.Configuracion.N_RANDOM)
        nRandomRepos.config(state=tk.NORMAL)
    else:
        nRandomRepos_state.set(0)
        nRandomRepos.config(state=tk.DISABLED)

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
user_state.set(conf.Configuracion.user)
user = tk.Entry(p1,width=15, textvariable=user_state)
user.grid(column=1, row=row)
row+=1

tokenLbl = tk.Label(p1, text="Token: ", bg=backgroudLblColor)
tokenLbl.grid(column=0, row=row)
token_state.set(conf.Configuracion.token)
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
lenguaje_state.set(conf.FiltrosQuery.language)
lenguaje = tk.Entry(p1, width=15, textvariable=lenguaje_state)
lenguaje.grid(column=1, row=row)
row+=1

# STARS
starsLbl = tk.Label(p1, text="Stars: ", bg=backgroudLblColor)
starsLbl.grid(column=0, row=row)
stars_state.set(conf.FiltrosQuery.stars)
stars = tk.Entry(p1, width=15, textvariable=stars_state)
stars.grid(column=1, row=row)
row+=1

# FORKS
forksLbl = tk.Label(p1, text="Forks: ", bg=backgroudLblColor)
forksLbl.grid(column=0, row=row)
forks_state.set(conf.FiltrosQuery.forks)
forks = tk.Entry(p1, width=15, textvariable=forks_state)
forks.grid(column=1, row=row)
row+=1

# CREATED
createdLbl = tk.Label(p1, text="Created: ", bg=backgroudLblColor)
createdLbl.grid(column=0, row=row)
created_state.set(conf.FiltrosQuery.created)
created = tk.Entry(p1, width=15, textvariable=created_state)
created.grid(column=1, row=row)
row+=1

# PUSHED
pushedLbl = tk.Label(p1, text="Pushed: ", bg=backgroudLblColor)
pushedLbl.grid(column=0, row=row)
pushed_state.set(conf.FiltrosQuery.pushed)
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
sizeLimit_state.set(conf.Configuracion.REPO_SIZE_LIMIT)
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

# BUSCAR REPOS EN LOCAL
buscarEnLocalReposLbl = tk.Label(p1, text="Buscar repos en LOCAL", bg=backgroudLblColor)
buscarEnLocalReposLbl.grid(column=0, row=row)
#buscarEnLocalReposLbl.pack()
buscarEnLocalCheck_state.set(conf.Configuracion.buscarEnLocal)
buscarEnLocalCheck = tk.Checkbutton(p1, var=buscarEnLocalCheck_state, bg=backgroudLblColor)
buscarEnLocalCheck.grid(column=1, row=row)
#buscarEnLocalCheck.pack()
row+=1

# GENERAR LISTA REPOS
generarListaReposLbl = tk.Label(p1, text="Generar lista repos ('.pickle')", bg=backgroudLblColor)
generarListaReposLbl.grid(column=0, row=row)
#generarListaReposLbl.pack()
generarListaReposCheck_state.set(conf.Configuracion.generarListaRepos)
generarListaReposCheck = tk.Checkbutton(p1, var=generarListaReposCheck_state, bg=backgroudLblColor)
generarListaReposCheck.grid(column=1, row=row)
#generarListaReposCheck.pack()
row+=1

# ScriptLapseExe
scriptLapseExeLbl = tk.Label(p1, text="Ejecutar mediante 'ScriptLapseExe'", bg=backgroudLblColor)
#scriptLapseExeLbl.grid(column=0, row=row)
#scriptLapseExeLbl.pack()
scriptLapseExeCheck_state.set(conf.Configuracion.lapseExe)
scriptLapseExeCheck = tk.Checkbutton(p1, var=scriptLapseExeCheck_state, bg=backgroudLblColor)
#scriptLapseExeCheck.grid(column=1, row=row)
#scriptLapseExeCheck.pack()
#row+=1

# Nº LAPSE REPOS
#nLapseReposLbl = tk.Label(p1, text="Nº lapse repos: ", bg=backgroudLblColor)
#nLapseReposLbl.grid(column=0, row=row)
#nLapseReposLbl.pack()
nLapseRepos_state.set(conf.Configuracion.N_LAPSE_REPOS)
nLapseRepos = tk.Entry(p1, width=5, textvariable=nLapseRepos_state)
#nLapseRepos.grid(column=2, row=row)
#nLapseRepos.pack()
row+=1

# RANDOMIZAR REPOSITORIOS
randomizarReposLbl = tk.Label(p1, text="Randomizar repositorios", bg=backgroudLblColor)
randomizarReposLbl.grid(column=0, row=row)
#randomizarReposLbl.pack()
randomizarReposCheck_state.set(conf.Configuracion.randomizarListaRepos)
randomizarReposCheck = tk.Checkbutton(p1, var=randomizarReposCheck_state, command=randomizarReposCheck_clicked, bg=backgroudLblColor)
randomizarReposCheck.grid(column=1, row=row)
#randomizarReposCheck.pack()

# Nº REPOS RANDOM
#nRandomReposLbl = tk.Label(p1, text="Nº repos random: ", bg=backgroudLblColor)
#nRandomReposLbl.grid(column=0, row=row)
#nRandomReposLbl.pack()
nRandomRepos_state.set(conf.Configuracion.N_RANDOM)
nRandomRepos = tk.Entry(p1, width=5, textvariable=nRandomRepos_state)
nRandomRepos.grid(column=2, row=row)
#nRandomRepos.pack()
row+=1

# CLONAR REPOSITORIOS
clonarReposLbl = tk.Label(p1, text="Clonar repositorios resultantes", bg=backgroudLblColor)
clonarReposLbl.grid(column=0, row=row)
#clonarReposLbl.pack()
clonarReposCheck_state.set(conf.Configuracion.clonarRepositorios)
clonarReposCheck = tk.Checkbutton(p1, var=clonarReposCheck_state, bg=backgroudLblColor)
clonarReposCheck.grid(column=1, row=row)
#clonarReposCheck.pack()
row+=1

# DO EXCEL
doExcelLbl = tk.Label(p1, text="Generar Excel", bg=backgroudLblColor)
doExcelLbl.grid(column=0, row=row)
#doExcelLbl.pack()
doExcelCheck_state.set(conf.Configuracion.doExcel)
doExcelCheck = tk.Checkbutton(p1, var=doExcelCheck_state, bg=backgroudLblColor)
doExcelCheck.grid(column=1, row=row)
#doExcelCheck.pack()
row+=1

# DO CSV
doCsvLbl = tk.Label(p1, text="Generar Csv", bg=backgroudLblColor)
doCsvLbl.grid(column=0, row=row)
#doCsvLbl.pack()
doCsvCheck_state.set(conf.Configuracion.doCsv)
doCsvCheck = tk.Checkbutton(p1, var=doCsvCheck_state, bg=backgroudLblColor)
doCsvCheck.grid(column=1, row=row)
#doCsvCheck.pack()
row+=1

# BOTÓN EJECUTAR
exeButton = tk.Button(p1, text="EJECUTAR", fg="green",  command=exe, bg=backgroudLblColor)
#exeButton.pack()
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
nombreRepoBD_state.set(" ")
nombreRepoBD = tk.Entry(p2, width=15, textvariable=nombreRepoBD_state)
nombreRepoBD.grid(column=1, row=row)
row+=1

# ORGANIZACION BD
organizacionBDLbl = tk.Label(p2, text="Organizacion: ", bg=backgroudLblColor)
organizacionBDLbl.grid(column=0, row=row)
organizacionBD_state.set(" ")
organizacionBD = tk.Entry(p2, width=15, textvariable=organizacionBD_state)
organizacionBD.grid(column=1, row=row)
row+=1

# COMMIT ID BD
commitIdBDLbl = tk.Label(p2, text="Commit ID: ", bg=backgroudLblColor)
commitIdBDLbl.grid(column=0, row=row)
commitIdBD_state.set(" ")
commitIdBD = tk.Entry(p2, width=15, textvariable=commitIdBD_state)
commitIdBD.grid(column=1, row=row)
row+=1

# SIZE BD
sizeBDLbl = tk.Label(p2, text="Tamaño (kilobytes): ", bg=backgroudLblColor)
sizeBDLbl.grid(column=0, row=row)
sizeBD_state.set(" ")
sizeBD = tk.Entry(p2, width=15, textvariable=sizeBD_state)
sizeBD.grid(column=1, row=row)
row+=1

# BOTÓN CONSULTA BBDD
consultaBDButton = tk.Button(p2, text="CONSULTAR BD", fg="green",  command=consultarBD, bg=backgroudLblColor)
#consultaBDButton.pack()
consultaBDButton.grid(column=1, row=row)
row+=1

# Resultado de la búsqueda
resultadoLbl = tk.Label(p2, text="Resultado de la consulta:", bg=backgroudLblColor)
resultadoLbl.grid(column=0, row=row)
f = font.Font(resultadoLbl, resultadoLbl.cget("font"))
f.configure(underline=True)
resultadoLbl.configure(font=f)
row+=1
scrollbar = ttk.Scrollbar(p2, orient=tk.VERTICAL)
listadoBD = tk.Listbox(p2, borderwidth=1, yscrollcommand=scrollbar.set)
listadoBD.grid(row=row)
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
#ejecutaPruebaButton.pack()
ejecutaPruebaButton.grid(column=1, row=row)
row+=1


nb.add(p1, text='Buscador')
nb.add(p2, text='BBDD')
nb.add(p3, text='PRUEBAS')

#buscarEnLocalCheck_clicked()
randomizarReposCheck_clicked()

app.mainloop()