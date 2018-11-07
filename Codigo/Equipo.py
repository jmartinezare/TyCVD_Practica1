from Jugador import Jugador, JugadorMng
from PetitionWeb import PeticionWeb
from bs4 import BeautifulSoup

class Equipo(object):
    """description of class"""
    Nombre    = ""
    Categoria = ""
    Genero    = ""
    Liga      = ""
    Url       = ""
    Jugadores = []

    def __init__(self, url= ""):
        self.Url = url

class EquipoMng(object):
    """Clase encargada de manipular equipos"""

    def __init__(self, peticion_web : PeticionWeb):        
        self._peticion_web = PeticionWeb()
        self._jugador_Mng = JugadorMng(self._peticion_web)
        if peticion_web == "":
            self._peticion_web = PeticionWeb()
        else:
            self._peticion_web = peticion_web

    def obtener_lista_datos(self, lista_Equipos):
        for equipo in lista_Equipos:
            self.obtener_datos(equipo)


    def obtener_datos(self, equipo: Equipo): 
        contenido = self._peticion_web.hacer_peticion(equipo.Url)
        soup = BeautifulSoup(contenido,'lxml')
        equipo.Nombre     = self.soup_text(soup.find('h1', {'class': 'titulo_equipo'}))        
        enlaces_jugadores = soup.select("a.box-jugador")        
         
        equipo.Jugadores = []

        for enlace in enlaces_jugadores:
            jugador = Jugador(enlace.get('href'))
            jugador.Liga      = equipo.Liga
            jugador.Categoria = equipo.Categoria
            jugador.Genero    = equipo.Genero
            jugador.Equipo    = equipo.Nombre
            equipo.Jugadores.append(jugador)            
        
        self._jugador_Mng.obtener_lista_datos(equipo.Jugadores)
        # Aquí se podría cambiar el orden de los jugadores a la hora de guardarlos
        self._jugador_Mng.guardar_lista(equipo.Jugadores)

    def soup_text(self, valor):
        resu = ""
        try:                
            if valor is not None: 
                resu = valor.text            
        except :
            resu = ""
        return resu