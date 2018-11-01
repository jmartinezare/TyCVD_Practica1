import os
from bs4 import BeautifulSoup
import PetitionWeb
from PetitionWeb import PeticionWeb
from EscritorCSV import EscritorCSV

class Jugador(object):
    """Clase que representa la información de un jugador"""
    Nombre       = ""
    ShorName     = ""
    Dorsal       = 0
    Posicion     = ""
    Fecha        = 0
    Altura       = 0
    Peso         = 0
    LugarNacim   = ""
    Nacionalidad = ""
    UrlImagen    = ""
    Url          = ""
    Categoria    = ""
    Genero       = ""
    Equipo       = ""
    Liga         = ""
    
    def __init__(self, url = ""):
        self.Url      = url
        self.ShorName = os.path.basename(url)

    def Vacio(self):
        return not Nombre

class JugadorMng(object):
    """Clase encargada de manipular jugadores"""
    
    def __init__(self, peticion_web : PeticionWeb):
        self._nombre_fichero = "dataset.csv"
        self._cabera = 'Género','Categoría','Equipo','Nombre','Dorsal','Posición','Fecha','Altura','Peso','LugarNacimiento','Nacionalidad', 'Url Imagen'
        self._escritor_CSV = EscritorCSV(self._nombre_fichero,self._cabera)
        self._activado_descarga_img = True
        if peticion_web == "":
            self._peticion_web = PeticionWeb()
        else:
            self._peticion_web = peticion_web

    def obtener_lista_datos(self, lista_Jugadores):                      
        for jugador in lista_Jugadores:            
            self.obtener_datos(jugador)

    #def obtener_lista_datos(self, lista_Jugadores):                          
    #    for jugador in lista_Jugadores:
    #        if jugador.ShorName == "rakitic":
    #            self.obtener_datos(jugador)            

    def obtener_datos(self, jugador: Jugador):                                   
        contenido = self._peticion_web.hacer_peticion(jugador.Url)
        soup = BeautifulSoup(contenido,'lxml')        
        jugador.Nombre       = self.soup_text(soup.find('div', {'id': 'nombre'}))
        jugador.Dorsal       = self.soup_text(soup.find('div', {'id': 'dorsal'}))
        jugador.Posicion     = self.soup_text(soup.find('div', {'id': 'posicion'}))
        jugador.Fecha        = self.soup_text(soup.find('div', {'id': 'fecha_nacimiento'}))
        jugador.Fecha        = jugador.Fecha.replace('Fecha nacimiento: ','').strip()
        jugador.LugarNacim   = self.soup_text(soup.find('div', {'id': 'lugar_nacimiento'}))
        jugador.LugarNacim   = jugador.LugarNacim.replace('Lugar de nacimiento: ','').strip()
        jugador.Nacionalidad = self.soup_text(soup.find('div', {'id': 'nacionalidad'}))
        jugador.Nacionalidad = jugador.Nacionalidad.replace('Nacionalidad: ','').strip()
        jugador.UrlImagen    = self.soup_imgsrc(soup.find('div', {'id': 'foto-perfil'})) 
        
        datos = soup.select("section.datos-sidebar-jugador > div.box-datos > div.box-dato") 
#
        for dato in datos:
            nombre_dato = self.soup_text(dato.find('h2', {'class': 'nombre'}))
            if nombre_dato == "Altura":
                jugador.Altura   = self.soup_text(dato.find('div', {'class': 'dato'}))
            elif nombre_dato == "Peso":
                jugador.Peso     = self.soup_text(dato.find('div', {'class': 'dato'}))                   
        
    def guardar_lista(self, lista_Jugadores):        
        for jugador in lista_Jugadores:
            self.guardar(jugador, False)                        
        self._escritor_CSV.cerrar()

    def guardar(self, jugador: Jugador, cerrar = True):
        self._escritor_CSV.escribir_linea(jugador.Genero, jugador.Categoria, jugador.Equipo, jugador.Nombre, jugador.Dorsal, jugador.Posicion, jugador.Fecha, jugador.Altura, jugador.Peso, jugador.LugarNacim, jugador.Nacionalidad, jugador.UrlImagen)
        if self._activado_descarga_img:
            self._peticion_web.descargar_img(jugador.UrlImagen, jugador.ShorName)            
        if cerrar:
            self._escritor_CSV.cerrar()
        
    def soup_text(self, valor):
        resu = ""
        try:                
            if valor is not None: 
                resu = valor.text            
        except :
            resu = ""
        return resu

    def soup_imgsrc(self, valor):
        resu = ""
        try:                
            if valor is not None: 
                resu = valor.img['src']
        except :
            resu = ""
        return resu