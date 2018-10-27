#imports

#if __name__=='__main__':

#ObtenerEquipos()
#mientras lstEquipos <> vacia
#    equipo = sigEquipo()
#    obtenerJugadores(equipo)
#    mientras lstJugadores <> vacia
#    jugador = SigJugador
#    Jugador = ObtDatosJugador(jugador)
#    guardarJugador

#from htmlJugador import HTMLJugador, HTMLFicha
from Jugador import JugadorMng
from bs4 import BeautifulSoup
import requests
import htmlF1M
import htmlMadrid
from Jugador import Jugador, JugadorMng


#page = requests.get("https://www.laliga.es/laliga-santander/real-madrid")
page = requests.get("https://www.laliga.es/laliga-123/malaga")
htmlContent = page.content
#htmlContent = htmlMadrid.HTMLMADRID

soup = BeautifulSoup(htmlContent,'lxml')
enlaces = soup.select("a.box-jugador")

#print (soup.prettify())

lstJugadores = []

for jugador in enlaces:
    jugador = Jugador(jugador.get('href'))
    lstJugadores.append(jugador)

   
#jugador = Jugador('https://www.laliga.es/jugador/sergio-ramos')



jugadorMng = JugadorMng("")

jugadorMng.obtener_lista_datos(lstJugadores)
jugadorMng.guardar_lista(lstJugadores)
#print(jugador.Nombre)
#print(jugador.Nombre)

print('Fin')
