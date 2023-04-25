from Class_Persona import Persona    
#CLASE ALUMNO
class Alumno(Persona):
    def __init__(self, param_nombre, param_apellido, param_legajo, param_email, param_carrera, param_year):
        self.carrera = param_carrera
        self.year = param_year
        super().__init__(param_nombre,param_apellido,param_legajo,param_email)

#ALUMNO
alumno_martin = Alumno("Martin","Navarro",62181,"mt.navarro@alumno.um.edu.ar","Ingenieria en Informática","2 año")
print("ALUMNO")
print("-El nombre es: " , alumno_martin.nombre)
print("-El apellido es: " , alumno_martin.apellido)
print("-El legajo es: " , alumno_martin.legajo)
print("-El email es: " , alumno_martin.email)
print("-Esta en la carrera de: " , alumno_martin.carrera)  
print("-Esta en:v" , alumno_martin.year)

print("EL ALUMNO FUE A CLASE...")
alumno_martin.asistencia_clase() #CLASE 1
alumno_martin.asistencia_clase() #C;ASE 2
alumno_martin.asistencia_clase() #CLASE 3
alumno_martin.asistencia_clase() #CLASE 4
alumno_martin.asistencia_clase() #CLASE 5
alumno_martin.asistencia_clase() #CLASE 6 
alumno_martin.asistencia_clase() #CLASE 7
print("-Su asistencia es: " , alumno_martin.asistencia)