import main
import configuracion as conf
import tkinter as tk
from tkinter import ttk
from tkinter import font
from PIL import Image
from PIL import ImageTk

app = tk.Tk()
app.title("BuscadorGitHubRepos")
width = '650'
height = '650'
app.geometry(width + 'x' + height)
app.resizable(False, False)

nb = ttk.Notebook(app)
nb.pack(fill='both', expand='yes')

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
widget = tk.Label(p1, image=photoImg)
widget.grid(column=0, row=row)
titleAppLbl = tk.Label(p1, text="BuscadorGitHubRepos", font=('Helvetica', 18, 'bold'))
titleAppLbl.grid(column=1, row=row)
f = font.Font(titleAppLbl, titleAppLbl.cget("font"))
f.configure(underline=True)
titleAppLbl.configure(font=f)
row+=1

# CREDENCIALES
credencialesLbl = tk.Label(p1, text="CREDENCIALES")
credencialesLbl.grid(column=0, row=row)
f = font.Font(credencialesLbl, credencialesLbl.cget("font"))
f.configure(underline=True)
credencialesLbl.configure(font=f)
row+=1

userLbl = tk.Label(p1, text="Usuario: ")
userLbl.grid(column=0, row=row)
user_state.set(conf.Configuracion.user)
user = tk.Entry(p1,width=15, textvariable=user_state)
user.grid(column=1, row=row)
row+=1

tokenLbl = tk.Label(p1, text="Token: ")
tokenLbl.grid(column=0, row=row)
token_state.set(conf.Configuracion.token)
token = tk.Entry(p1,width=34, textvariable=token_state)
token.grid(column=1, row=row)
row+=1

# FILTROS QUERY
filtrosQueryLbl = tk.Label(p1, text="FILTROS QUERY")
filtrosQueryLbl.grid(column=0, row=row)
f = font.Font(filtrosQueryLbl, filtrosQueryLbl.cget("font"))
f.configure(underline=True)
filtrosQueryLbl.configure(font=f)
row+=1

# LENGUAJE
lenguajeLbl = tk.Label(p1, text="Lenguaje: ")
lenguajeLbl.grid(column=0, row=row)
lenguaje_state.set(conf.FiltrosQuery.language)
lenguaje = tk.Entry(p1, width=15, textvariable=lenguaje_state)
lenguaje.grid(column=1, row=row)
row+=1

# STARS
starsLbl = tk.Label(p1, text="Stars: ")
starsLbl.grid(column=0, row=row)
stars_state.set(conf.FiltrosQuery.stars)
stars = tk.Entry(p1, width=15, textvariable=stars_state)
stars.grid(column=1, row=row)
row+=1

# FORKS
forksLbl = tk.Label(p1, text="Forks: ")
forksLbl.grid(column=0, row=row)
forks_state.set(conf.FiltrosQuery.forks)
forks = tk.Entry(p1, width=15, textvariable=forks_state)
forks.grid(column=1, row=row)
row+=1

# CREATED
createdLbl = tk.Label(p1, text="Created: ")
createdLbl.grid(column=0, row=row)
created_state.set(conf.FiltrosQuery.created)
created = tk.Entry(p1, width=15, textvariable=created_state)
created.grid(column=1, row=row)
row+=1

# PUSHED
pushedLbl = tk.Label(p1, text="Pushed: ")
pushedLbl.grid(column=0, row=row)
pushed_state.set(conf.FiltrosQuery.pushed)
pushed = tk.Entry(p1, width=15, textvariable=pushed_state)
pushed.grid(column=1, row=row)
row+=1

# ARCHIVED
archivedLbl = tk.Label(p1, text="Archived ")
archivedLbl.grid(column=0, row=row)
archivedCheck_state.set(False)
archivedCheck = tk.Checkbutton(p1, var=archivedCheck_state)
archivedCheck.grid(column=1, row=row)
archivedCheck.config(state=tk.DISABLED)
row+=1

# PUBLIC
publicLbl = tk.Label(p1, text="Public")
publicLbl.grid(column=0, row=row)
publicCheck_state.set(True)
publicCheck = tk.Checkbutton(p1, var=publicCheck_state)
publicCheck.grid(column=1, row=row)
publicCheck.config(state=tk.DISABLED)
row+=1

# SIZE LIMIT
sizeLimitLbl = tk.Label(p1, text="Size Limit (kilobytes): ")
sizeLimitLbl.grid(column=0, row=row)
sizeLimit_state.set(conf.Configuracion.REPO_SIZE_LIMIT)
sizeLimit = tk.Entry(p1, width=7, textvariable=sizeLimit_state)
sizeLimit.grid(column=1, row=row)
sizeLimit.config(state=tk.DISABLED)
row+=1

# VARIABLES DE CONFIGURACIÓN
configuracionLbl = tk.Label(p1, text="VARIABLES DE CONFIGURACIÓN")
configuracionLbl.grid(column=0, row=row)
f = font.Font(configuracionLbl, configuracionLbl.cget("font"))
f.configure(underline=True)
configuracionLbl.configure(font=f)
row+=1

# BUSCAR REPOS EN LOCAL
buscarEnLocalReposLbl = tk.Label(p1, text="Buscar repos en LOCAL")
buscarEnLocalReposLbl.grid(column=0, row=row)
#buscarEnLocalReposLbl.pack()
buscarEnLocalCheck_state.set(conf.Configuracion.buscarEnLocal)
buscarEnLocalCheck = tk.Checkbutton(p1, var=buscarEnLocalCheck_state)
buscarEnLocalCheck.grid(column=1, row=row)
#buscarEnLocalCheck.pack()
row+=1

# GENERAR LISTA REPOS
generarListaReposLbl = tk.Label(p1, text="Generar lista repos ('.pickle')")
generarListaReposLbl.grid(column=0, row=row)
#generarListaReposLbl.pack()
generarListaReposCheck_state.set(conf.Configuracion.generarListaRepos)
generarListaReposCheck = tk.Checkbutton(p1, var=generarListaReposCheck_state)
generarListaReposCheck.grid(column=1, row=row)
#generarListaReposCheck.pack()
row+=1

# ScriptLapseExe
scriptLapseExeLbl = tk.Label(p1, text="Ejecutar mediante 'ScriptLapseExe'")
#scriptLapseExeLbl.grid(column=0, row=row)
#scriptLapseExeLbl.pack()
scriptLapseExeCheck_state.set(conf.Configuracion.lapseExe)
scriptLapseExeCheck = tk.Checkbutton(p1, var=scriptLapseExeCheck_state)
#scriptLapseExeCheck.grid(column=1, row=row)
#scriptLapseExeCheck.pack()
#row+=1

# Nº LAPSE REPOS
#nLapseReposLbl = tk.Label(p1, text="Nº lapse repos: ")
#nLapseReposLbl.grid(column=0, row=row)
#nLapseReposLbl.pack()
nLapseRepos_state.set(conf.Configuracion.N_LAPSE_REPOS)
nLapseRepos = tk.Entry(p1, width=5, textvariable=nLapseRepos_state)
#nLapseRepos.grid(column=2, row=row)
#nLapseRepos.pack()
row+=1

# RANDOMIZAR REPOSITORIOS
randomizarReposLbl = tk.Label(p1, text="Randomizar repositorios")
randomizarReposLbl.grid(column=0, row=row)
#randomizarReposLbl.pack()
randomizarReposCheck_state.set(conf.Configuracion.randomizarListaRepos)
randomizarReposCheck = tk.Checkbutton(p1, var=randomizarReposCheck_state, command=randomizarReposCheck_clicked)
randomizarReposCheck.grid(column=1, row=row)
#randomizarReposCheck.pack()

# Nº REPOS RANDOM
#nRandomReposLbl = tk.Label(p1, text="Nº repos random: ")
#nRandomReposLbl.grid(column=0, row=row)
#nRandomReposLbl.pack()
nRandomRepos_state.set(conf.Configuracion.N_RANDOM)
nRandomRepos = tk.Entry(p1, width=5, textvariable=nRandomRepos_state)
nRandomRepos.grid(column=2, row=row)
#nRandomRepos.pack()
row+=1

# CLONAR REPOSITORIOS
clonarReposLbl = tk.Label(p1, text="Clonar repositorios resultantes")
clonarReposLbl.grid(column=0, row=row)
#clonarReposLbl.pack()
clonarReposCheck_state.set(conf.Configuracion.clonarRepositorios)
clonarReposCheck = tk.Checkbutton(p1, var=clonarReposCheck_state)
clonarReposCheck.grid(column=1, row=row)
#clonarReposCheck.pack()
row+=1

# DO EXCEL
doExcelLbl = tk.Label(p1, text="Generar Excel")
doExcelLbl.grid(column=0, row=row)
#doExcelLbl.pack()
doExcelCheck_state.set(conf.Configuracion.doExcel)
doExcelCheck = tk.Checkbutton(p1, var=doExcelCheck_state)
doExcelCheck.grid(column=1, row=row)
#doExcelCheck.pack()
row+=1

# DO CSV
doCsvLbl = tk.Label(p1, text="Generar Csv")
doCsvLbl.grid(column=0, row=row)
#doCsvLbl.pack()
doCsvCheck_state.set(conf.Configuracion.doCsv)
doCsvCheck = tk.Checkbutton(p1, var=doCsvCheck_state)
doCsvCheck.grid(column=1, row=row)
#doCsvCheck.pack()
row+=1

# BOTÓN EJECUTAR
exeButton = tk.Button(p1, text="EJECUTAR", fg="green",  command=exe)
#exeButton.pack()
exeButton.grid(column=1, row=row)
row+=1

# PESTAÑA 2

row = 0

proximamenteLbl = tk.Label(p2, text="PRÓXIMAMENTE")
proximamenteLbl.grid(column=0, row=row)
row+=1


# PESTAÑA 3

row = 0

proximamenteLbl = tk.Label(p3, text="PRÓXIMAMENTE")
proximamenteLbl.grid(column=0, row=row)
row+=1


nb.add(p1, text='P1')
nb.add(p2, text='P2')
nb.add(p3, text='P3')

#buscarEnLocalCheck_clicked()
randomizarReposCheck_clicked()

app.mainloop()