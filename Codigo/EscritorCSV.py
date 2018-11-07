import os
import csv
import pathlib

class EscritorCSV(object):     
    def __init__(self, nombre_fichero, *cabecera):
        self._nombre_fichero = nombre_fichero
        self._cabera = cabecera
        self._fichero_abierto = False
        self._fichero_nuevo   = True
        self._tipo_escritura   = 'w'     
        self._dir_resultado = "../Resultado/"  
        self._ruta_dataset = os.path.join(self._dir_resultado, nombre_fichero)

    def escribir_linea (self, *linea):
        try:
            if self._fichero_abierto == False:
                pathlib.Path(self._dir_resultado).mkdir(exist_ok=True) 
                if self._fichero_nuevo == False:
                    self._tipo_escritura   = 'a'            

                self._fichero_abierto = True
                self._dataset  = open(self._ruta_dataset, self._tipo_escritura, newline='',encoding='utf-8')
                self._escritor = csv.writer(self._dataset, delimiter=';',quoting=csv.QUOTE_MINIMAL)

                if self._fichero_nuevo:
                    self._escritor.writerow(['Género','Categoría','Equipo','Nombre','Dorsal','Posición','Fecha','Altura','Peso','LugarNacimiento','Nacionalidad', 'Url Imagen'])
                    self._fichero_nuevo = False            

            self._escritor.writerow(linea)
        except:
            print("Error al escribir en el fichero: ", linea)
     
    def cerrar(self):
        self._fichero_abierto = False
        self._dataset.close()