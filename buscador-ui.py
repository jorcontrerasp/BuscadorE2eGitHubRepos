import tkinter as tk
import main
import configuracion
from pandas.core.resample import method

app = tk.Tk()
app.title("BuscadorGitHubRepos")
app.geometry('380x205')

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
    configuracion.Configuracion.buscarEnLocal = buscarEnLocalCheck_state.get()
    configuracion.Configuracion.generarListaRepos = generarListaReposCheck_state.get()
    configuracion.Configuracion.randomizarListaRepos = randomizarReposCheck_state.get()
    configuracion.Configuracion.lapseExe = False
    configuracion.Configuracion.clonarRepositorios = clonarReposCheck_state.get()
    configuracion.Configuracion.doExcel = doExcelCheck_state.get()
    configuracion.Configuracion.doCsv = doCsvCheck_state.get()
    configuracion.Configuracion.N_RANDOM = nRandomRepos_state.get()
    configuracion.Configuracion.N_LAPSE_REPOS = 0
    main.exe()

def buscarEnLocalCheck_clicked():
    if buscarEnLocalCheck_state.get():
        print("Buscar en local 'activado'")

row = 0

# VARIABLES DE CONFIGURACIÓN
configuracionLbl = tk.Label(app, text="VARIABLES DE CONFIGURACIÓN")
configuracionLbl.grid(column=0, row=row)
row+=1

# BUSCAR REPOS EN LOCAL
buscarEnLocalReposLbl = tk.Label(app, text="Buscar repos en LOCAL")
buscarEnLocalReposLbl.grid(column=0, row=row)
#buscarEnLocalReposLbl.pack()
buscarEnLocalCheck_state.set(True)
buscarEnLocalCheck = tk.Checkbutton(app, var=buscarEnLocalCheck_state, command=buscarEnLocalCheck_clicked)
buscarEnLocalCheck.grid(column=1, row=row)
#buscarEnLocalCheck.pack()
row+=1

# GENERAR LISTA REPOS
generarListaReposLbl = tk.Label(app, text="Generar lista repos ('.pickle')")
generarListaReposLbl.grid(column=0, row=row)
#generarListaReposLbl.pack()
generarListaReposCheck_state.set(False)
generarListaReposCheck = tk.Checkbutton(app, var=generarListaReposCheck_state)
generarListaReposCheck.grid(column=1, row=row)
#generarListaReposCheck.pack()
row+=1

# ScriptLapseExe
scriptLapseExeLbl = tk.Label(app, text="Ejecutar mediante 'ScriptLapseExe'")
#scriptLapseExeLbl.grid(column=0, row=row)
#scriptLapseExeLbl.pack()
scriptLapseExeCheck_state.set(True)
scriptLapseExeCheck = tk.Checkbutton(app, var=scriptLapseExeCheck_state)
#scriptLapseExeCheck.grid(column=1, row=row)
#scriptLapseExeCheck.pack()

# Nº LAPSE REPOS
#nLapseReposLbl = tk.Label(app, text="Nº lapse repos: ")
#nLapseReposLbl.grid(column=0, row=row)
#nLapseReposLbl.pack()
nLapseRepos_state.set(20)
nLapseRepos = tk.Entry(app,width=5, textvariable=nLapseRepos_state)
#nLapseRepos.grid(column=2, row=row)
#nLapseRepos.pack()

row+=1

# RANDOMIZAR REPOSITORIOS
randomizarReposLbl = tk.Label(app, text="Randomizar repositorios")
randomizarReposLbl.grid(column=0, row=row)
#randomizarReposLbl.pack()
randomizarReposCheck_state.set(True)
randomizarReposCheck = tk.Checkbutton(app, var=randomizarReposCheck_state)
randomizarReposCheck.grid(column=1, row=row)
#randomizarReposCheck.pack()

# Nº REPOS RANDOM
#nRandomReposLbl = tk.Label(app, text="Nº repos random: ")
#nRandomReposLbl.grid(column=0, row=row)
#nRandomReposLbl.pack()
nRandomRepos_state.set(30)
nRandomRepos = tk.Entry(app,width=5, textvariable=nRandomRepos_state)
nRandomRepos.grid(column=2, row=row)
#nRandomRepos.pack()

row+=1

# CLONAR REPOSITORIOS
clonarReposLbl = tk.Label(app, text="Clonar repositorios resultantes")
clonarReposLbl.grid(column=0, row=row)
#clonarReposLbl.pack()
clonarReposCheck_state.set(False)
clonarReposCheck = tk.Checkbutton(app, var=clonarReposCheck_state)
clonarReposCheck.grid(column=1, row=row)
#clonarReposCheck.pack()
row+=1

# DO EXCEL
doExcelLbl = tk.Label(app, text="Generar Excel")
doExcelLbl.grid(column=0, row=row)
#doExcelLbl.pack()
doExcelCheck_state.set(True)
doExcelCheck = tk.Checkbutton(app, var=doExcelCheck_state)
doExcelCheck.grid(column=1, row=row)
#doExcelCheck.pack()
row+=1

# DO CSV
doCsvLbl = tk.Label(app, text="Generar Csv")
doCsvLbl.grid(column=0, row=row)
#doCsvLbl.pack()
doCsvCheck_state.set(False)
doCsvCheck = tk.Checkbutton(app, var=doCsvCheck_state)
doCsvCheck.grid(column=1, row=row)
#doCsvCheck.pack()
row+=1

# BOTÓN EJECUTAR
exeButton = tk.Button(app, text="EJECUTAR", fg="green",  command=exe)
#exeButton.pack()
exeButton.grid(column=1, row=row)
row+=1

#buscarEnLocalCheck_clicked()

app.mainloop()