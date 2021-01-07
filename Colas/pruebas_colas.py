from Colas import Queue,BoundedPriorityQueue
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
print(f"bienvenido sr.{siguiente["nombre"]},en que podemos ayudar?")
print atencion.toString()

maestre={"prioridad":4,"descripcion":"Maestre","personas":"Juan N"}
Niño={"prioridad":2,"descripcion":"niño","personas":"pedro N"}
mecanico={"prioridad":4,"descripcion":"mecanico","personas":"maria N"}

cpa=BoundedPriorityQueue(7):
cpa.enqueue(maestre["prioridad"],maestre)
cpa.enqueue(Niño["prioridad"],Niño)
cpa.enqueue(mecanico["prioridad"],mecanico)
