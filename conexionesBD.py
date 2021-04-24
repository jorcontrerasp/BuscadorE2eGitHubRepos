import datetime
import pymysql
import pymysql.cursors
import executeQuery

class ConexionesBD():
    host = "localhost"
    port = "3306"
    user = "root"
    password = "password"
    db = "buscadorGitHubRepos"
    cursorClass = pymysql.cursors.DictCursor