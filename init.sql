CREATE DATABASE buscadorGitHubRepos;

USE buscadorGitHubRepos;

-- Script generador del esquema:

/*DROP TABLE BD_D_REPO;*/
/*DROP TABLE BD_D_BUSQUEDA;*/
/*DROP TABLE BD_D_CONFIGURACION;*/
/*DROP TABLE BD_D_CONFIGURACIONTIPO;*/

CREATE TABLE IF NOT EXISTS BD_D_BUSQUEDA(idbusqueda int(11) NOT NULL AUTO_INCREMENT, 
lenguaje varchar(50), 
stars varchar(50), 
forks varchar(50), 
created varchar(100), 
pushed varchar(100), 
archived int(1), 
public int(1), 
research LONGBLOB,
contadores BLOB,
tstbd varchar(100), 
PRIMARY KEY (idbusqueda));

INSERT INTO BD_D_BUSQUEDA (lenguaje, stars, forks, created, pushed, archived, public, tstbd) 
VALUES ("PLenguaje", "pStars", "pForks", "pCreated", "pPushed", 0, 1, "pTstbd");

CREATE TABLE IF NOT EXISTS BD_D_REPO(idrepo int(11) NOT NULL AUTO_INCREMENT, 
nombre varchar(200), 
organizacion varchar(200), 
lenguaje varchar(50), 
url varchar(1000), 
commitid varchar(20), 
size int(20), 
boe2e int(1),
idbusqueda int(11),
tstbd varchar(100), 
PRIMARY KEY (idrepo),
INDEX (idbusqueda),
FOREIGN KEY (idbusqueda) REFERENCES BD_D_BUSQUEDA(idbusqueda));

INSERT INTO BD_D_REPO (nombre, organizacion, lenguaje, url, commitid, size, boe2e, tstbd) 
VALUES("pNombre", "pOrganizacion", "pLenguaje", "pUrl", "123456789A", 1000, 0, "pTstbd");

CREATE TABLE IF NOT EXISTS BD_D_CONFIGURACIONTIPO(idconfiguraciontipo int(11) NOT NULL AUTO_INCREMENT, 
codigo varchar(50),
descripcion varchar(500), 
PRIMARY KEY (idconfiguraciontipo));

INSERT INTO BD_D_CONFIGURACIONTIPO(codigo, descripcion)
VALUES ("CREDENCIALES", "Configuración relativa a las credenciales de GitHub");

INSERT INTO BD_D_CONFIGURACIONTIPO(codigo, descripcion)
VALUES ("SEARCH_PARAM", "Configuración relativa al funcionamiento del buscador");

INSERT INTO BD_D_CONFIGURACIONTIPO(codigo, descripcion)
VALUES ("FILTROS_PARAM", "Configuración inicial del filtro de búsqueda");

CREATE TABLE IF NOT EXISTS BD_D_CONFIGURACION(idconfiguracion int(11) NOT NULL AUTO_INCREMENT,
campo varchar(100),
valor varchar(500),
descripcion varchar(500),
idconfiguraciontipo int(11),
PRIMARY KEY (idconfiguracion),
INDEX (idconfiguraciontipo),
FOREIGN KEY (idconfiguraciontipo) REFERENCES BD_D_CONFIGURACIONTIPO(idconfiguraciontipo) );

-- Configuración de las credenciales de GitHub
INSERT INTO BD_D_CONFIGURACION(campo, valor, descripcion, idconfiguraciontipo)
VALUES(
	"user", 
	"jorcontrerasp", 
	"Nombre de usuario de GitHub", 
	(SELECT IDCONFIGURACIONTIPO FROM BD_D_CONFIGURACIONTIPO WHERE CODIGO = 'CREDENCIALES')
);

INSERT INTO BD_D_CONFIGURACION(campo, valor, descripcion, idconfiguraciontipo)
VALUES(
	"token", 
	"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", 
	"Token de autenticación GitHub", 
	(SELECT IDCONFIGURACIONTIPO FROM BD_D_CONFIGURACIONTIPO WHERE CODIGO = 'CREDENCIALES')
);

-- Configuración del filtro de búsqueda
INSERT INTO BD_D_CONFIGURACION(campo, valor, descripcion, idconfiguraciontipo)
VALUES(
	"language", 
	"Java", 
	"Indica el 'lenguaje' que se carga en el filtro de búsqueda inicial", 
	(SELECT IDCONFIGURACIONTIPO FROM BD_D_CONFIGURACIONTIPO WHERE CODIGO = 'FILTROS_PARAM')
);

INSERT INTO BD_D_CONFIGURACION(campo, valor, descripcion, idconfiguraciontipo)
VALUES(
	"stars", 
	">=500", 
	"Indica las 'estrellas' que se cargan en el filtro de búsqueda inicial", 
	(SELECT IDCONFIGURACIONTIPO FROM BD_D_CONFIGURACIONTIPO WHERE CODIGO = 'FILTROS_PARAM')
);

INSERT INTO BD_D_CONFIGURACION(campo, valor, descripcion, idconfiguraciontipo)
VALUES(
	"forks", 
	">=300", 
	"Indica los 'forks' que se cargan en el filtro de búsqueda inicial", 
	(SELECT IDCONFIGURACIONTIPO FROM BD_D_CONFIGURACIONTIPO WHERE CODIGO = 'FILTROS_PARAM')
);

INSERT INTO BD_D_CONFIGURACION(campo, valor, descripcion, idconfiguraciontipo)
VALUES(
	"created", 
	"<2015-01-01", 
	"Indica la 'fecha de creación' que se carga en el filtro de búsqueda inicial", 
	(SELECT IDCONFIGURACIONTIPO FROM BD_D_CONFIGURACIONTIPO WHERE CODIGO = 'FILTROS_PARAM')
);

INSERT INTO BD_D_CONFIGURACION(campo, valor, descripcion, idconfiguraciontipo)
VALUES(
	"pushed", 
	">2020-01-01", 
	"Indica la 'fecha de lanzamiento a la plataforma' que se carga en el filtro de búsqueda inicial", 
	(SELECT IDCONFIGURACIONTIPO FROM BD_D_CONFIGURACIONTIPO WHERE CODIGO = 'FILTROS_PARAM')
);

INSERT INTO BD_D_CONFIGURACION(campo, valor, descripcion, idconfiguraciontipo)
VALUES(
	"archived", 
	"false", 
	"Indica el campo 'archived' que se carga en el filtro de búsqueda inicial", 
	(SELECT IDCONFIGURACIONTIPO FROM BD_D_CONFIGURACIONTIPO WHERE CODIGO = 'FILTROS_PARAM')
);

INSERT INTO BD_D_CONFIGURACION(campo, valor, descripcion, idconfiguraciontipo)
VALUES(
	"qIs", 
	"public", 
	"Indica el campo 'public' que se carga en el filtro de búsqueda inicial", 
	(SELECT IDCONFIGURACIONTIPO FROM BD_D_CONFIGURACIONTIPO WHERE CODIGO = 'FILTROS_PARAM')
);

-- Configuración de los parámetros de búsqueda
INSERT INTO BD_D_CONFIGURACION(campo, valor, descripcion, idconfiguraciontipo)
VALUES(
	"actualizarBD", 
	"True", 
	"Indica si se actualiza la BD en la ejecución del proceso", 
	(SELECT IDCONFIGURACIONTIPO FROM BD_D_CONFIGURACIONTIPO WHERE CODIGO = 'SEARCH_PARAM')
);

INSERT INTO BD_D_CONFIGURACION(campo, valor, descripcion, idconfiguraciontipo)
VALUES(
	"buscarEnLocal", 
	"True", 
	"Indica si el proceso se realiza en local o no", 
	(SELECT IDCONFIGURACIONTIPO FROM BD_D_CONFIGURACIONTIPO WHERE CODIGO = 'SEARCH_PARAM')
);

INSERT INTO BD_D_CONFIGURACION(campo, valor, descripcion, idconfiguraciontipo)
VALUES(
	"generarListaRepos", 
	"True", 
	"Indica si se reutiliza los repositorios obtenidos de un fichero pickle existente o si genera uno nuevo", 
	(SELECT IDCONFIGURACIONTIPO FROM BD_D_CONFIGURACIONTIPO WHERE CODIGO = 'SEARCH_PARAM')
);

INSERT INTO BD_D_CONFIGURACION(campo, valor, descripcion, idconfiguraciontipo)
VALUES(
	"randomizarListaRepos", 
	"True", 
	"Indica si se randomizan los repositorios obtenidos o no", 
	(SELECT IDCONFIGURACIONTIPO FROM BD_D_CONFIGURACIONTIPO WHERE CODIGO = 'SEARCH_PARAM')
);

INSERT INTO BD_D_CONFIGURACION(campo, valor, descripcion, idconfiguraciontipo)
VALUES(
	"lapseExe", 
	"False", 
	"Indica si se va a ejecutar mediante lapsos de tiempo (ScriptLapseExe)", 
	(SELECT IDCONFIGURACIONTIPO FROM BD_D_CONFIGURACIONTIPO WHERE CODIGO = 'SEARCH_PARAM')
);

INSERT INTO BD_D_CONFIGURACION(campo, valor, descripcion, idconfiguraciontipo)
VALUES(
	"clonarRepositorios", 
	"False", 
	"Indica si se van a clonar los repositorios resultantes", 
	(SELECT IDCONFIGURACIONTIPO FROM BD_D_CONFIGURACIONTIPO WHERE CODIGO = 'SEARCH_PARAM')
);

INSERT INTO BD_D_CONFIGURACION(campo, valor, descripcion, idconfiguraciontipo)
VALUES(
	"doExcel", 
	"True", 
	"Indica si se transforma el DataFrame a Excel", 
	(SELECT IDCONFIGURACIONTIPO FROM BD_D_CONFIGURACIONTIPO WHERE CODIGO = 'SEARCH_PARAM')
);

INSERT INTO BD_D_CONFIGURACION(campo, valor, descripcion, idconfiguraciontipo)
VALUES(
	"doCsv", 
	"False", 
	"Indica si se transforma el DataFrame a Csv", 
	(SELECT IDCONFIGURACIONTIPO FROM BD_D_CONFIGURACIONTIPO WHERE CODIGO = 'SEARCH_PARAM')
);

INSERT INTO BD_D_CONFIGURACION(campo, valor, descripcion, idconfiguraciontipo)
VALUES(
	"escribirEnLog", 
	"False", 
	"Indica si se escribe en log o no", 
	(SELECT IDCONFIGURACIONTIPO FROM BD_D_CONFIGURACIONTIPO WHERE CODIGO = 'SEARCH_PARAM')
);

INSERT INTO BD_D_CONFIGURACION(campo, valor, descripcion, idconfiguraciontipo)
VALUES(
	"N_RANDOM", 
	"30", 
	"Número de repositorios random que se van a seleccionar", 
	(SELECT IDCONFIGURACIONTIPO FROM BD_D_CONFIGURACIONTIPO WHERE CODIGO = 'SEARCH_PARAM')
);

INSERT INTO BD_D_CONFIGURACION(campo, valor, descripcion, idconfiguraciontipo)
VALUES(
	"N_LAPSE_REPOS", 
	"20", 
	"Número de repositorios que se utilizan en cada lapso de tiempo (ScriptLapseExe)", 
	(SELECT IDCONFIGURACIONTIPO FROM BD_D_CONFIGURACIONTIPO WHERE CODIGO = 'SEARCH_PARAM')
);

INSERT INTO BD_D_CONFIGURACION(campo, valor, descripcion, idconfiguraciontipo)
VALUES(
	"REPO_SIZE_LIMIT", 
	"10000000", 
	"Límite de tamaño de un repositorio que se va a clonar", 
	(SELECT IDCONFIGURACIONTIPO FROM BD_D_CONFIGURACIONTIPO WHERE CODIGO = 'SEARCH_PARAM')
);

INSERT INTO BD_D_CONFIGURACION(campo, valor, descripcion, idconfiguraciontipo)
VALUES(
	"ITEMS_FOUND_LIMIT", 
	"50", 
	"Límite de elementos que va a poder encontrar por cada criterio", 
	(SELECT IDCONFIGURACIONTIPO FROM BD_D_CONFIGURACIONTIPO WHERE CODIGO = 'SEARCH_PARAM')
);

INSERT INTO BD_D_CONFIGURACION(campo, valor, descripcion, idconfiguraciontipo)
VALUES(
	"SEARCH_TIME_LIMIT", 
	"30", 
	"Límite de tiempo (en minutos) que va a estar el programa buscando un criterio en cada repositorio", 
	(SELECT IDCONFIGURACIONTIPO FROM BD_D_CONFIGURACIONTIPO WHERE CODIGO = 'SEARCH_PARAM')
);

COMMIT;
