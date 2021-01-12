from ColasPrior import PriorityQueue
import random
maestre={"prioridad":4,"descripcion":"Maestre","personas":"Juan N"}
Niño={"prioridad":2,"descripcion":"niño","personas":"pedro N"}
mecanico={"prioridad":4,"descripcion":"mecanico","personas":"maria N"}
Hombre={"prioridad":3,"descripcion":"hombre","personas":"jesus N"}
Vigia={"prioridad":4,"descripcion":"Vigia","personas":"Lisa k"}
Capitan={"prioridad":5,"descripcion":"Capitan","personas":"Morgan Jack"}
Timonel={"prioridad":4,"descripcion":"Timonel","personas":"Gibbs"}
Mujer={"prioridad":3,"descripcion":"mujer","personas":"Nora Z"}
Viejo={"prioridad":2,"descripcion":"abuelo","personas":"Dedushka"}
Niña={"prioridad":1,"descripcion":"Niña","personas":"Liliana"}

Titanic=PriorityQueue()
Titanic.enqueue(maestre["prioridad"],maestre)
Titanic.enqueue(Niño["prioridad"],Niño)
Titanic.enqueue(mecanico["prioridad"],mecanico)
Titanic.enqueue(Hombre["prioridad"],Hombre)
Titanic.enqueue(Vigia["prioridad"],Vigia)
Titanic.enqueue(Capitan["prioridad"],Capitan)
Titanic.enqueue(Timonel["prioridad"],Timonel)
Titanic.enqueue(Mujer["prioridad"],Mujer)
Titanic.enqueue(Viejo["prioridad"],Viejo)
Titanic.enqueue(Niña["prioridad"],Niña)

print("EL TITANIC HA GOLPEADO UN ICEBERG!!")
print("PROCEDA A EVACUAR LA NAVE")
integridad=100
while Titanic.is_empty() ==False and integridad>0:
  agua=random.randint(0,20)
  integridad=integridad-agua
  escape=Titanic.dequeue()
  print(f"el pasajero: {escape['personas']} de prioridad {escape['prioridad']} ha subido al bote")
  print(f"integridad: {integridad}")
if integridad<=0 and Titanic.is_empty() ==False:
  print("el resto de personas murieron de hipotermia...")
else:
    print("Lo lograste!! todos han subido al bote!")
    print("(no hay nadie en la cola, el barco ya ha sido evacuado por completo)")
