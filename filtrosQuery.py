import auxiliares

class FiltrosQuery():
    language = "java"
    stars = ">=500"
    forks = ">=300"
    created = "<2015-01-01"
    pushed = ">2020-01-01"
    archived = "false"
    qIs = "public"

    def __init__(self):
        self.inicializaFiltrosQuery()

    def inicializaFiltrosQuery(self):
        self.language = auxiliares.getConfiguracion("FILTROS_PARAM", "language")
        self.stars = auxiliares.getConfiguracion("FILTROS_PARAM", "stars")
        self.forks = auxiliares.getConfiguracion("FILTROS_PARAM", "forks")
        self.created = auxiliares.getConfiguracion("FILTROS_PARAM", "created")
        self.pushed = auxiliares.getConfiguracion("FILTROS_PARAM", "pushed")
        self.archived = auxiliares.getConfiguracion("FILTROS_PARAM", "archived")
        self.qIs = auxiliares.getConfiguracion("FILTROS_PARAM", "qIs")

    def getQueryIni(self):
        queryIni = ""
        if len(self.language)>0:
            queryIni += "language:" + self.language + "\n"

        if len(self.stars)>0:
            queryIni += "stars:" + self.stars + "\n"

        if len(self.forks)>0:
            queryIni += "forks:" + self.forks + "\n"

        if len(self.created)>0:
            queryIni += "created:" + self.created + "\n"

        if len(self.pushed)>0:
            queryIni += "pushed:" + self.pushed + "\n"

        if len(self.archived)>0:
            queryIni += "archived:" + self.archived + "\n"

        if len(self.qIs)>0:
            queryIni += "is:" + self.qIs + "\n"

        return queryIni

filtrosQuery = FiltrosQuery()