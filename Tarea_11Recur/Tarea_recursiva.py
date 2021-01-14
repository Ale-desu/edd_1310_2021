from Stack import Stack
from math import floor
#problema 2
def suma_lista_rec(lista):
    if len(lista)==1:
        return lista[0]
    else:
        return lista.pop()+suma_lista_rec(lista)
def main():
    datos = [4,2,3,5]
    res=suma_lista_rec(datos)
    print(res)
main()

#problema 1
def regresivo(num):
  for x in range(num):
    print(num,end=", ")
    num-=1
  print("\n c'est tout mon ami")
regresivo(12)

#problema 3
numeros=Stack()
numeros.push(3)
numeros.push(31)
numeros.push(11)
numeros.push(31)
numeros.push(30)
numeros.to_string()
print("---------------- \n\n")

def middle_Pop():
  copy=[]
  midle=floor(numeros.lenght()/2)
  for x in range(numeros.lenght()):
    if x!=midle:
      copy.append(numeros.pop())
    else:
      numeros.pop()
  copy.reverse()
  for x in range(len(copy)):
    numeros.push(copy[x])
  numeros.to_string()
middle_Pop()
