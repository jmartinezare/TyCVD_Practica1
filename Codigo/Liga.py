from Equipo import Equipo, EquipoMng
from PetitionWeb import PeticionWeb
from bs4 import BeautifulSoup

class Liga(object):
    """Clase con los datos de una liga"""
    Nombre    = ""
    Categoria = ""
    Genero    = ""
    Url       = ""
    Equipos   = []

    def __init__(self, url= ""):
        self.Url = url

class LigaMng(object):
    """Clase encargada de manipular Ligas"""

    def __init__(self):        
        self._peticion_web = PeticionWeb()
        self._equipo_Mng   = EquipoMng(self._peticion_web)        

    def obtener_lista_datos(self, lista_Ligas):
        for liga in lista_Ligas:
            self.obtener_datos(liga)

    def obtener_datos(self, liga: Liga): 
        contenido = self._peticion_web.hacer_peticion(liga.Url)
        soup = BeautifulSoup(contenido,'lxml')        
        enlaces_equipos = soup.select("table.datatable_clasificacion td.contenedor-nombre a")       
        
        liga.Equipos = []

        for enlace in enlaces_equipos:
            equipo = Equipo(enlace.get('href'))
            equipo.Categoria = liga.Categoria
            equipo.Genero    = liga.Genero
            equipo.Liga      = liga.Nombre
            liga.Equipos.append(equipo) 

        self._equipo_Mng.obtener_lista_datos(liga.Equipos)

    #def guardar_lista(self, lista_ligas):
    #    for liga in lista_ligas:
    #        self.guardar(liga)

    #def guardar(self, liga: Liga):
    #    self._equipo_Mng.guardar_lista(liga.equipos)


class FactoriaLigas(object):
    """ Obtiene los objetos de Liga que se van a utilizar en este proceso"""
    def obtener_ligas(self):
        ligas = []
        liga1M = Liga()
        liga1M.Nombre    = "Santander"
        liga1M.Genero    = "Masculino"
        liga1M.Categoria = "Primera"
        liga1M.Url       = "https://www.laliga.es/laliga-santander"

        ligas.append(liga1M)

        liga2M = Liga()
        liga2M.Nombre    = "1|2|3"
        liga2M.Genero    = "Masculino"
        liga2M.Categoria = "Segunda"
        liga2M.Url       = "https://www.laliga.es/laliga-123"
        
        ligas.append (liga2M)

        return ligas