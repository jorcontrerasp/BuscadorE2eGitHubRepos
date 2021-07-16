import auxiliares

class FiltrosQuery():
    language = None
    stars = None
    forks = None
    created = None
    pushed = None
    archived = None
    qIs = None

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
        queryIni = "\n" + "     "
        if len(self.language)>0:
            queryIni += "   language:" + self.language + " \n"

        if len(self.stars)>0:
            queryIni += "       stars:" + self.stars + " \n"

        if len(self.forks)>0:
            queryIni += "       forks:" + self.forks + " \n"

        if len(self.created)>0:
            queryIni += "       created:" + self.created + " \n"

        if len(self.pushed)>0:
            queryIni += "       pushed:" + self.pushed + " \n"

        if len(self.archived)>0:
            queryIni += "       archived:" + self.archived + " \n"

        if len(self.qIs)>0:
            queryIni += "       is:" + self.qIs + " \n"

        queryIni = queryIni + "     "

        return queryIni

filtrosQuery = FiltrosQuery()