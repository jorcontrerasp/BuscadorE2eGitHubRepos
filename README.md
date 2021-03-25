# BuscadorGitHubRepos

Buscador de repositorios GitHub en función de un heurístico desarrollado previamente. 
Se trata de encontrar repositorios de GitHub que puedan tener pruebas ent-to-end (e2e).

### Pre-requisitos 📋

<p>pip install PyGithub</p>
<p>pip install pandas</p>
<p>pip install openpyxl</p>
<p>pip install pillow</p>
<p>xcode-select —install (para corregir un posible xcrun error)</p>
<p>pip install pymysql</p>

### Variables de configuración 🔧

- Actualizar BD: si se marca esta opción se almacenarán los datos obtenidos en base de datos. Para ello se ha utilizado una BB MySql.

  <p>CONFIGURACIÓN DE LA BBDD:</p>
  Mysql -u root -p

  CREATE DATABASE buscadorGitHubRepos;

  USE buscadorGitHubRepos;

  CREATE TABLE IF NOT EXISTS BD_D_REPO(id int(11) NOT NULL AUTO_INCREMENT, nombre varchar(50), organizacion varchar(200), url varchar(1000), commitid varchar(20), size int(20), boe2e int(1), PRIMARY KEY (id));

  INSERT INTO BD_D_REPO (nombre, organizacion, url, commitID, size, boE2E) VALUES("AAA", "BBB", "CCC", "123456789A", 1000, 0);

- Buscar repos en LOCAL: si se marca esta opción se clonan los proyectos que se van a utilizar en la carpeta “repositories”, y una vez clonados, la búsqueda se realiza sobre dichos ficheros en local. Al finalizar el proceso se borra la carpeta “repositories” y se genera un fichero zip a modo de snapshot con todos esos repositorios clonados inicialmente.
- Generar lista repos ('.pickle’): si se marca esta opción se genera un nuevo fichero “.pickle” con todos los repositorios que se van a utilizar en el proceso de búsqueda. Si no se marca se reutiliza el fichero “.pickle” existente en la carpeta del proyecto.
- Randomizar repositorios: si se marca esta opción, de todos los repositorios obtenidos inicialmente para realizar la búsqueda, se utilizan un número x de forma aleatoria.
- Clonar repositorios resultantes: si se marca esta opción se clonan en local los repositorios que hayan cumplido algún criterio.
- Generar excel: si se marca esta opción se guarda el resultado de la búsqueda en un fichero en formato excel.
- Generar Csv: si se marca esta opción se guarda el resultado de la búsqueda en un fichero en formato csv.

<p>Pestaña 1:</p>
<img src="imgs/interfaz_p1.png" alt=“interfaz” width="450"/>

<p>Pestaña 2:</p>
<img src="imgs/interfaz_p2.png" alt=“interfaz” width="450"/>

<p>Pestaña 3:</p>
<img src="imgs/interfaz_p3.png" alt=“interfaz” width="450"/>

## Construido con 🛠️

* [PyCharm Community](https://www.jetbrains.com/es-es/pycharm/?ref=hackernoon.com)

## Autores ✒️

* **Jorge Contreras Padilla** - [jorcontrerasp](https://github.com/jorcontrerasp)

## Licencia 📄

Este proyecto está bajo la Licencia (Apache-2.0 License) - mirar el archivo [LICENSE](https://github.com/jorcontrerasp/BuscadorGitHubRepos/blob/main/LICENSE) para más detalles.
