# BuscadorGitHubRepos

Buscador de repositorios GitHub en función de un heurístico desarrollado previamente. 
Se trata de encontrar repositorios de GitHub que puedan tener pruebas ent-to-end (e2e).

### Pre-requisitos 📋

<p>pip install PyGithub</p>
<p>pip install pandas</p>
<p>pip install openpyxl</p>

### Variables de configuración 🔧

- Buscar repos en LOCAL: si se marca esta opción se clonan los proyectos que se van a utilizar en la carpeta “repositories”, y una vez clonados, la búsqueda se realiza sobre dichos ficheros en local. Al finalizar el proceso se borra la carpeta “repositories” y se genera un fichero zip a modo de snapshot con todos esos repositorios clonados inicialmente.
- Generar lista repos ('.pickle’): si se marca esta opción se genera un nuevo fichero “.pickle” con todos los repositorios que se van a utilizar en el proceso de búsqueda. Si no se marca se reutiliza el fichero “.pickle” existente en la carpeta del proyecto.
- Randomizar repositorios: si se marca esta opción, de todos los repositorios obtenidos inicialmente para realizar la búsqueda, se utilizan un número x de forma aleatoria.
- Clonar repositorios resultantes: si se marca esta opción se clonan en local los repositorios que hayan cumplido algún criterio.
- Generar excel: si se marca esta opción se guarda el resultado de la búsqueda en un fichero en formato excel.
- Generar Csv: si se marca esta opción se guarda el resultado de la búsqueda en un fichero en formato csv.

## Construido con 🛠️

* [PyCharm Community](https://www.jetbrains.com/es-es/pycharm/?ref=hackernoon.com)

## Autores ✒️

* **Jorge Contreras Padilla** - [jorcontrerasp](https://github.com/jorcontrerasp)

## Licencia 📄

Este proyecto está bajo la Licencia (Apache-2.0 License) - mirar el archivo [LICENSE](https://github.com/jorcontrerasp/BuscadorGitHubRepos/blob/main/LICENSE) para más detalles.
