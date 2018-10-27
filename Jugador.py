from htmlJugador import HTMLFicha
from bs4 import BeautifulSoup
import csv
import PetitionWeb
from PetitionWeb import PeticionWeb

class Jugador(object):
    """description of class"""
    Nombre       = ""
    Dorsal       = 0
    Posicion     = ""
    Fecha        = 0
    Altura       = 0
    Peso         = 0
    LugarNacim   = ""
    Nacionalidad = ""
    Url          = ""
    Deporte      = ""
    Categoria    = ""
    Genero       = ""
    Equipo       = ""  
    
    def __init__(self, url = ""):
        self.Url = url

    def Vacio(self):
        return not Nombre

class JugadorMng(object):
    """Clase encargada de manipular jugadores"""
    
    def __init__(self, peticion_web : PeticionWeb):
        self._nombre_fichero = "dataset.csv"
        if peticion_web == "":
            self._peticion_web = PeticionWeb()
        else:
            self._peticion_web = peticion_web

    def obtener_lista_datos(self, lista_Jugadores):                  
        for jugador in lista_Jugadores:
            self.obtener_datos(jugador)

    def obtener_datos(self, jugador: Jugador):                                   
        contenido = self._peticion_web.hacer_peticion(jugador.Url)
        #contenido = HTMLFicha
        soup = BeautifulSoup(contenido,'lxml')

        #jugador.Nombre       = self.soup_find(soup, 'div', {'id': 'nombre'})
        #jugador.Dorsal       = self.soup_find(soup, 'div', {'id': 'dorsal'})
        #jugador.Posicion     = self.soup_find(soup, 'div', {'id': 'posicion'})
        #jugador.Fecha        = self.soup_find(soup, 'div', {'id': 'fecha_nacimiento'})
        #jugador.Fecha        = jugador.Fecha.replace('Fecha nacimiento: ','').strip()
        #jugador.LugarNacim   = self.soup_find(soup, 'div', {'id': 'lugar_nacimiento'})
        #jugador.LugarNacim   = jugador.LugarNacim.replace('Lugar de nacimiento: ','').strip()
        #jugador.Nacionalidad = self.soup_find(soup, 'div', {'id': 'nacionalidad'})

        jugador.Nombre       = self.soup_text(soup.find('div', {'id': 'nombre'}))
        jugador.Dorsal       = self.soup_text(soup.find('div', {'id': 'dorsal'}))
        jugador.Posicion     = self.soup_text(soup.find('div', {'id': 'posicion'}))
        jugador.Fecha        = self.soup_text(soup.find('div', {'id': 'fecha_nacimiento'}))
        jugador.Fecha        = jugador.Fecha.replace('Fecha nacimiento: ','').strip()
        jugador.LugarNacim   = self.soup_text(soup.find('div', {'id': 'lugar_nacimiento'}))
        jugador.LugarNacim   = jugador.LugarNacim.replace('Lugar de nacimiento: ','').strip()
        jugador.Nacionalidad = self.soup_text(soup.find('div', {'id': 'nacionalidad'}))
        
    def guardar_lista(self, lista_Jugadores):
        dataset = open(self._nombre_fichero, 'w', encoding="utf-8", newline='\n')
        for jugador in lista_Jugadores:  # no se llama a Guardar para no abrir y cerrar el fichero por cada jugador            
            dtWriter = csv.writer(dataset, delimiter=';',quotechar='|', quoting=csv.QUOTE_MINIMAL)
            dtWriter.writerow([jugador.Genero, jugador.Categoria, jugador.Equipo, jugador.Nombre, jugador.Dorsal, jugador.Posicion, jugador.Fecha, jugador.Altura, jugador.Peso, jugador.LugarNacim, jugador.Nacionalidad])
        dataset.close()            

    def guardar(self, jugador: Jugador):
        dataset = open(self._nombre_fichero, 'w', encoding="utf-8",newline='\n')
        dtWriter = csv.writer(dataset, delimiter=';',quotechar='|', quoting=csv.QUOTE_MINIMAL)
        dtWriter.writerow([jugador.Genero, jugador.Categoria, jugador.Equipo, jugador.Nombre, jugador.Dorsal, jugador.Posicion, jugador.Fecha, jugador.Altura, jugador.Peso, jugador.LugarNacim, jugador.Nacionalidad])
        dataset.close()              
    
    def soup_find(self, soup, arg1, **attrs):
        try:
            print (attrs)
            resu = soup.find(arg1, attrs)
            if resu is None: 
                return ""
            else: 
                return resu.text            
        except :
        
            return ""


    def soup_text(self, valor):
        resu = ""
        try:                
            if valor is not None: 
                resu = valor.text            
        except :
            resu = ""
        return resu