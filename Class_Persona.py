
#HERENCIA   
class Persona:
    def __init__(self, param_nombre, param_apellido, param_legajo, param_email):
        self.nombre = param_nombre 
        self.apellido = param_apellido
        self.legajo = param_legajo
        self.email = param_email
        self.asistencia = 0 

    def cambiar_nombre(self, nuevo_nombre):
        self.nombre = nuevo_nombre
    
    def asistencia_clase(self):
        self.asistencia += 1