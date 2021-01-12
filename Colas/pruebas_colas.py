from Colas import Queue,BoundedPriorityQueue
import random
q1=Queue()
q1.enqueue(3)
q1.enqueue(33)
q1.enqueue(34)
print(q1.toString())
print("prueba dos de cola")
c1={"id":1,"nombre":"mario","balance":20.5}
c2={"id":2,"nombre":"juan","balance":3456.5}
c3={"id":3,"nombre":"diana","balance":10000000.5}
atencion=Queue()
atencion.enqueue(c1)
atencion.enqueue(c2)
atencion.enqueue(c3)
print(atencion.toString())
siguiente=atencion.dequeue()
print(f"bienvenido sr.{siguiente['nombre']},en que podemos ayudar?")
print (atencion.toString())

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


cpa=BoundedPriorityQueue(7)
cpa.enqueue(maestre["prioridad"],maestre)
cpa.enqueue(Niño["prioridad"],Niño)
cpa.enqueue(mecanico["prioridad"],mecanico)
cpa.enqueue(Hombre["prioridad"],Hombre)
cpa.enqueue(Vigia["prioridad"],Vigia)
cpa.enqueue(Capitan["prioridad"],Capitan)
cpa.enqueue(Timonel["prioridad"],Timonel)
cpa.enqueue(Mujer["prioridad"],Mujer)
cpa.enqueue(Viejo["prioridad"],Viejo)
cpa.enqueue(Niña["prioridad"],Niña)

cpa.to_string()

print("EL TITANIC HA GOLPEADO UN ICEBERG!!")
print("PROCEDA A EVACUAR LA NAVE")
integridad=100
while cpa.is_empty() ==False and integridad>0:
  agua=random.randint(0,20)
  integridad=integridad-agua
  escape=cpa.dequeue()
  print(f"el pasajero: {escape['personas']} de prioridad {escape['prioridad']} ha subido al bote")
  print(f"integridad: {integridad}")
if integridad<=0 and cpa.is_empty() ==False:
  print("el resto de personas murieron de hipotermia...")
else:
    print("Lo lograste!! todos han subido al bote!")
    print("(no hay nadie en la cola, el barco ya ha sido evacuado por completo)")
