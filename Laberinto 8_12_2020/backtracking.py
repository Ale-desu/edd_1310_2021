from Array2D import Array2D

from Stack import Stack

class LaberintoADT:
    """
    0pasillo, 1 pared, S salida, E entrada
    pasillo es una tupla((2,1)(2,2)(2,3)(2,4)(3,2)(4,2))
    entrada en tupla(5,1)
    salida en tupla(2,5)
    """
    def __init__(self,rens,cols,pasillos, entrada, salida):
        self.__laberinto= Array2D(rens,cols,"1")
        for pasillo in pasillos:
            self.__laberinto.set_item(pasillo[0], pasillo[1],"0")
        self.set_entrada(entrada[0],entrada[1])
        self.set_salida(salida[0],salida[1])
        self.__camino=Stack()
        self.__previa=None# guarda la posición previa

    def to_string(self):
        self.__laberinto.to_string()
        """
        establece la entrada E de la matriz, verificar limites
        """
    def set_entrada(self,ren,col):
        #terminar la validación de  las coordenadas
        self.__laberinto.set_item(ren,col,"E")

    def set_salida(self,ren,col):
        self.__laberinto.set_item(ren,col,"S")

    def es_salida(self,ren,col):
        return self.__laberinto.get_item(ren,col)=="S"

    def buscar_entrada (self):
        encontrado =False
        for renglon in range(self.__laberinto.get_num_rows()):
            for columna in range(self.__laberinto.get_num_cols()):
                if self.__laberinto.get_item(renglon,columna)=="E":
                    self.__camino.push((renglon,columna))
                    encontrado=True
        return encontrado

    def set_previa(self, pos_prev):
        self.__previa =pos_prev

    def get_previa (self):
        return self.__previa

    def get_pos_actual(self):
        return self.__camino.peek()

    def resolver_laberinto(self):
        actual=self.__camino.peek()
        #a la izquierda
        #agregar validaciones para los limites
        if actual[1]-1!=-1 and self.__laberinto.get_item(actual[0],actual[1]-1)=="0" \
        and self.get_previa( )!= (actual[0],actual[1]-1) \
        and (actual[0],actual[1]-1)!="X":
            self.set_previa(actual)
            self.__camino.push((actual[0],actual[1]-1))
        #arriba
        elif actual[0]-1!=-1 and self.__laberinto.get_item(actual[0]-1,actual[1])=="0" \
        and self.get_previa( )!= (actual[0]-1,actual[1]) \
        and (actual[0]-1,actual[1])!="X":
            self.set_previa(actual)
            self.__camino.push((actual[0]-1,actual[1]))
        #abajo
        elif actual[0]+1!=-1 and self.__laberinto.get_item(actual[0]+1,actual[1])=="0" \
        and self.get_previa( )!= (actual[0]+1,actual[1]) \
        and (actual[0]+1,actual[1])!="X":
            self.set_previa(actual)
            self.__camino.push((actual[0]+1,actual[1]))
        #derecha
        elif actual[1]+1!=-1 and self.__laberinto.get_item(actual[0],actual[1]+1)=="0" \
        and self.get_previa( )!= (actual[0],actual[1]+1) \
        and (actual[0],actual[1]+1)!="X":
            self.set_previa(actual)
            self.__camino.push((actual[0],actual[1]+1))
            #debug
        else:
            self.__laberinto.set_item(actual[0],actual[1],"X")
            self.__previa=actual
            self.__camino.pop()
            
    def imprimir_camino(self):
        self.__camino.to_string()
        #aplicar reglas
