class NodoArbol:
    def __init__(self, value,left=None,right=None):
        self.data=value
        self.left=left
        self.right=right

class BinarySearchTree:
    def __init__(self):
        self.__root=None
    def insert (self, valor):
        if self.__root==None:
            self.__root=NodoArbol(valor)
        else:
            self.__insert__(self.__root,valor)

    def __insert__(self,nodo, value):
        if nodo.data==value:
            print("el dato ya existe")
        elif value<nodo.data:
            if nodo.left==None:
                nodo.left=NodoArbol(value)
            else:
                self.__insert__(nodo.left,value)
        else:
            if nodo.right==None:
                nodo.right=NodoArbol(value)
            else:
                self.__insert__(nodo.right,value)
    def __recorrido_in (self,nodo):
        if nodo!=None:
            self.__recorrido_in(nodo.left)
            print(nodo.data , end=", ")
            self.__recorrido_in(nodo.right)
            
    def transversal (self, format="inorden"):
        if format =="inorden":
            self.__recorrido_in(self.__root)
        elif format=="preorden":
            print("recorido en pre")
        elif format=="posorden":
            print("posorden")
        else:
            print("xd")

    def __search(self, nodo, value):
        if nodo:
            return None
        elif nodo.data== value: #Caso Base de RECURSIVIDAD
            print("Encontrado")
            return nodo.data
        elif value < nodo.data:
            print ("Buscar a la izquierda")
            return self.__search(nodo.left, value)
        else:
            print ("Buscar a la derecha")
            return self.__search(nodo.right,value)

    def remove (self, value):
        if self.__root=None:
            print("nada que eliminar")
        else:
            self.__remove(None,None,self.__root,value)

    def __remove(self,padre_hi,padre_hd,actual,value):
        if actual==None:
            print("caso base")
            return None
        elif actual.data==value:#caso base
            print("encontrado",actual.data)
            #caso 1 hoja
            if actual.left==None and actual.right==None:
                if padre_hi!=None:
                    padre_hd.right=None
                else:
                    padre_hd.right=None
            #caso 2 con hijo (en 109)
            if (encontrado. left != None and encontrado.right ==None) or (encontrado.left == None and encontrado.right != None):
                print("Es un Nodo con hijo")
                if actual.left!=None:
                    actual.data=actual.left.data
                    actual.left=None
                else:
                    actual.data=actual.right.data
                    actual.right=None
            #caso3 con 2 hijos

        elif value <actual.data:
            print("buscar a la izquierda")
            self.__remove(actual,None,actual.left,value)
        else:
            print("buscar a la derecha")
            self.__remove(None,actual,actual.right,value)
