from Class_Persona import  Persona
#CLASE PROFESOR    
class Profesor(Persona):
    def __init__(self, param_nombre, param_apellido, param_legajo, param_email):
        super().__init__(param_nombre, param_apellido, param_legajo, param_email)

#PROFESOR
profesor_gabriel = Profesor("Gabriel","Flores",12345,"gabriel@um.edu.ar")
print("PROFESOR")
print("-El nombre es: " , profesor_gabriel.nombre)
print("-El apellido es: " , profesor_gabriel.apellido)
print("-El legajo es: " , profesor_gabriel.legajo)
print("-El email es: " , profesor_gabriel.email)

print("EL PROFESOR FUE A CLASE...")
profesor_gabriel.asistencia_clase() #CLASE 1
profesor_gabriel.asistencia_clase() #CLASE 2
profesor_gabriel.asistencia_clase() #CLASE 3
profesor_gabriel.asistencia_clase() #CLASE 4
profesor_gabriel.asistencia_clase() #CLASE 5
profesor_gabriel.asistencia_clase() #CLASE 6
profesor_gabriel.asistencia_clase() #CLASE 7
print("-Su asistencia es: " , profesor_gabriel.asistencia)