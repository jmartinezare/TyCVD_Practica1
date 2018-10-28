import csv

class EscritorCSV(object):
     
    def __init__(self, nombre_fichero, *cabecera):
        self._nombre_fichero = nombre_fichero
        self._cabera = cabecera
        self._fichero_abierto = False
        self._fichero_nuevo   = True
        self._tipo_escritura   = 'w'
        #self._cabera = ['Género','Categoría','Equipo','Nombre','Dorsal','Posición','Fecha','Altura','Peso','LugarNacimiento','Nacionalidad']

    def escribir_linea (self, *linea):
        if self._fichero_abierto == False:
            if self._fichero_nuevo == False:
                self._tipo_escritura   = 'a'            

            self._fichero_abierto = True
            self._dataset  = open(self._nombre_fichero, self._tipo_escritura, encoding="utf-8",newline='')
            self._escritor = csv.writer(self._dataset, delimiter=';', quotechar='|', quoting=csv.QUOTE_MINIMAL)

            if self._fichero_nuevo:
                self._escritor.writerow(['Género','Categoría','Equipo','Nombre','Dorsal','Posición','Fecha','Altura','Peso','LugarNacimiento','Nacionalidad'])
                self._fichero_nuevo = False            

        self._escritor.writerow(linea)
        
    def cerrar(self):
        self._fichero_abierto = False
        self._dataset.close()
        self._cabera 