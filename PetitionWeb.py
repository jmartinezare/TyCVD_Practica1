import requests
import time
import random
import urllib
import os
import pathlib

class PeticionWeb(object):
    """Clase encargada de hacer la peticios de datos a una url y devolver la respuesta """
    #user-agent = Mediapartners-Google (https://support.google.com/webmasters/answer/1061943?hl=es)

    def __init__(self):
        self._tiempo_ult_peticion = time.time()
        self._primera_peticion    = True
        self._delay = 5                
        self._offset_delay = 5 
        self._user_agent = "Mediapartners-Google"
        self._max_peticiones = 999999
        self._num_peticiones = 0
        self._dir_imagenes = "./imagenes/"
        self._activado_descarga_img = True
        self._sobrescribir_img = False

    def comprobar_retraso(self):        
        tiempo_ahora  = time.time()
        tiempo_espera = 0            

        if self._primera_peticion:
            self._primera_peticion = False
        else:
            if tiempo_ahora - self._tiempo_ult_peticion < self._delay:
                tiempo_espera = self._delay - (tiempo_ahora - self._tiempo_ult_peticion)
                tiempo_espera = tiempo_espera + random.randint(0, self._offset_delay)

        print(f"Tiempo espera: ", "{0:.2f}".format(tiempo_espera))        
        time.sleep(tiempo_espera)
        return tiempo_espera
    
    def hacer_peticion(self, url):
        if self._num_peticiones < self._max_peticiones:        
            contenido = ""
            self.comprobar_retraso()            
            print(f"Petición Url: ",  url)    
            pagina = requests.get(url, headers = {'User-agent': self._user_agent})            
                     
            if pagina.status_code == 200:
                contenido = pagina.content
            else:                
                print(f"    Resultado: ",  "Error ", pagina.status_code)    
        
            self._tiempo_ult_peticion = time.time()
            self._num_peticiones = self._num_peticiones + 1
            return contenido 
        else:
            return ""

    def descargar_img(self, url, nombre):
        ruta = ""
        if self._activado_descarga_img and url != "":    
            print(f"Descarga imagen: ", nombre, " --> ", url, ".")
            try:    
                extension = os.path.splitext(url)[-1]
                nombre_completo = nombre + extension                
                pathlib.Path(self._dir_imagenes).mkdir(exist_ok=True) 
                ruta = os.path.join(self._dir_imagenes, nombre_completo)               
                if not os.path.isfile(ruta) or self._sobrescribir_img == True:
                    self.comprobar_retraso()
                    req = urllib.request.Request(url)
                    page = urllib.request.urlopen(req)
                    self._tiempo_ult_peticion = time.time()
                    f = open(ruta, 'bw')
                    f.write(page.read())
                    f.close()
            except urllib.error.HTTPError as e:
                 print("Error al descargar imagen: ", url)            
            except:
                print("Error al crear la imagen ", ruta ) 
    
    
