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
     def transversal(self, format= "inorden"):
        if format == "inorden":
          self.__recorrido_in(self.__root)
        elif format =="preorden":
          print("Recorrido en pre")
        elif format =="posorden":
          print("Recorrido pos")
        else:
          print("Error, formato inexistente")
        print("")  

      def __search(self, nodo, value):
        if nodo:
          return None
        elif nodo.data== value :#Caso Base de RECURSIVIDAD
           print("Encontrado")
           return nodo.data
        elif value < nodo.data: 
            print ("Buscar a la izquierda")
            return self.__search(nodo.left, value)
        else: 
            print ("Buscar a la derecha")
            return self.__search()  
        def search( self , value ):
            if self.__root == None:
                return None
            else:
                return self.__search( self.root , value ) 

        def remove (self, value):
            encontrado=self.search(value)
    #Caso 1
            if encontrado.left ==None and encontrado.right ==None:
                print("Eliminando", encontrado.data)
                encontrado=None
    #Caso 2
            elif (encontrado. left != None and encontrado.right ==None) or (encontrado.left == None and encontrado.right != None):
                pass
