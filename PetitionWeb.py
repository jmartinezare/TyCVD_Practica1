import requests
import time

class PeticionWeb(object):
    """Clase encargada de hacer la peticios de datos a una url y devolver la respuesta """
    #user-agent = Mediapartners-Google (https://support.google.com/webmasters/answer/1061943?hl=es)

    def __init__(self):
        self._tiempo_ult_peticion = time.time()
        self._primera_peticion    = True
        self._delay = 5                
        self._user_agent = "Mediapartners-Google"

    def hacer_peticion(self, url):
        tiempo_ahora  = time.time()
        tiempo_espera = 0
        contenido = ""

        if self._primera_peticion:
            self._primera_peticion = False
        else:
            if tiempo_ahora - self._tiempo_ult_peticion < self._delay:
                tiempo_espera = self._delay - (tiempo_ahora - self._tiempo_ult_peticion)

        print(f"tiempo espera: ", tiempo_espera)

        time.sleep(tiempo_espera)
        pagina = requests.get(url, headers = {'User-agent': self._user_agent})

        print ("peticion: ", url)

        if pagina.status_code == 200:
            contenido = pagina.content            
        
        self._tiempo_ult_peticion = time.time()
        return contenido 
