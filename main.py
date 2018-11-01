from Liga import Liga, LigaMng, FactoriaLigas

factoriaLigas = FactoriaLigas()
lista_ligas = factoriaLigas.obtener_ligas()

liga_Mng = LigaMng()
liga_Mng.obtener_lista_datos(lista_ligas)

print('Fin')