from Alumno.person import Person #importar solo una parte del archivo
from typing import List

program = int(input("A que programa desea ingresar: 1. Finalización semestre \n 2. Admisión: \n"))

    

match program:
    case 1:
        peopleMecatronica:List[Person] = []
        peopleTelecomunicaciones:List[Person] = []
        stop = True
        while stop:
            materia = int(input("Seleccione materia a finalizar: 1. Mecatronica. \n 2. Telecomunicaciones. \n"))
            numAlumnos = int(input("Ingresar número de alumnos:\n"))
            for i in range(numAlumnos):
                id: str = input("insert identification: ")
                fullName: str = input("Insert full name: ")
                sexo: int = int(input("Seleccione sexo del estudiante: 1. Masculino. \n 2. Femenino. \n"))
                edad: int = int(input("Ingrese la edad del estudiante: "))

                listNotas: list[int] = []
                for i in range(5):
                    nota = int(input(f"Inserte la nota {i+1} del estudiante {fullName}: "))
                    listNotas.append(nota)
                
                person = Person(id=id)
                person.setFullName(fullName)
                person.setSexo(sexo)
                person.setEdad(edad)
                person.setListNotas(listNotas)
                person.setPromedioNotas(sum(listNotas))

                if(materia == 1):
                    peopleMecatronica.append(person)
                else:
                    peopleTelecomunicaciones.append(person)

                stopExecution = input("Seleccionar otra materia \n1. si \n2. no")
                if(stopExecution == "2"):
                    stop = False
        manMecatronica = 0
        mujerMecatronica = 0
        listAllPromMe: list[int] = []
        
        for i in peopleMecatronica:
            nota = i.getPromedioNotas
            listAllPromMe.append(nota)
            sexo = i.getSexo()
            if(sexo == 1):
                manMecatronica += 1
            else:
                mujerMecatronica += 1
        promedioNotas = sum(listAllPromMe)/len(peopleMecatronica)
        print("En el programa de Mecatronica hay ", manMecatronica , " hombres y " , mujerMecatronica ,"mujeres")
        print("El promedio de la nota en mecatronica es: " , promedioNotas)
        hombreTelecomunicaciones = 0
        mujerTelecomunicaciones = 0
        listAllPromTe: list[int] = []
        for i in peopleTelecomunicaciones:
            nota = i.getPromedioNotas
            listAllPromTe.append(nota)
            sexo = i.getSexo()
            if(sexo == 1):
                manMecatronica += 1
            else:
                mujerMecatronica += 1
        promedioNotas = sum(listAllPromTe)/len(peopleTelecomunicaciones)
        print("En el programa de Telecomunicaciones hay ", hombreTelecomunicaciones , " hombres y " , mujerTelecomunicaciones +"mujeres")
        print("El promedio de la nota en telecomunicaciones es: " , promedioNotas)
    
    case 2:
        people:List[Person] = []
        while True:
            id: str = input("insert identification: ")
            fullName: str = input("Insert full name: ")
            sexo: int = int(input("Seleccione sexo del estudiante: 1. Masculino. \n 2. Femenino. \n"))
            edad: int = int(input("Ingrese la edad del estudiante: "))

            person = Person(id=id)
            person.setFullName(fullName)
            person.setSexo(sexo)
            person.setEdad(edad)

            people.append(person)

            stopExecution = input("Desea matricular a otra persona \n1 si \n2 no")
            if(stopExecution == "2"):
                man = 0
                lisEdades: List[int] = []
                for i in people:
                    lisEdades.append(i.getEdad())
                    sexo = i.getSexo()
                    if(sexo == 1):
                        man += 1
                women = len(people)-man
                print("Cantidad total de estudiantes matriculados: ", len(people))
                print("Edad promedio de los matriculados: ", (sum(lisEdades)/len(people)))
                print("La cantidad de hombres matriculados son", man , " y mujeres es " , women)
                break
