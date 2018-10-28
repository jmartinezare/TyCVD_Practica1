
from Liga import Liga, LigaMng, FactoriaLigas

#from Equipo import Equipo, EquipoMng

factoriaLigas = FactoriaLigas()
lista_ligas = factoriaLigas.obtener_ligas()

liga_Mng = LigaMng()
liga_Mng.obtener_lista_datos(lista_ligas)

#equipo = Equipo("https://www.laliga.es/laliga-santander/real-madrid")
#equipo_mng = EquipoMng()
#equipo_mng.obtener_datos(equipo)
#equipo_mng.guardar(equipo)

##page = requests.get("https://www.laliga.es/laliga-santander/real-madrid")
#page = requests.get("https://www.laliga.es/laliga-123/malaga")
#htmlContent = page.content
##htmlContent = htmlMadrid.HTMLMADRID

#soup = BeautifulSoup(htmlContent,'lxml')
#enlaces = soup.select("a.box-jugador")

##print (soup.prettify())

#lstJugadores = []

#for jugador in enlaces:
#    jugador = Jugador(jugador.get('href'))
#    lstJugadores.append(jugador)

   
##jugador = Jugador('https://www.laliga.es/jugador/sergio-ramos')

#jugadorMng = JugadorMng("")

#jugadorMng.obtener_lista_datos(lstJugadores)
#jugadorMng.guardar_lista(lstJugadores)
##print(jugador.Nombre)
##print(jugador.Nombre)

print('Fin')

