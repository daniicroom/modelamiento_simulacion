class Person:
    id: str = None
    fullName: str = None
    sexo: int = None
    edad: int = None
    listNotas: list[int] = None
    promedioNotas: int = None

    def __init__(self, id:str):
        self.id = id

    def setId(self, id:str):
        self.id = id

    def getId(self):
        return self.id
    
    def setFullName(self, fullName:str):
        self.fullName = fullName

    def getFullName(self):
        return self.fullName
    
    def setSexo(self, sexo:int):
        self.sexo = sexo

    def getSexo(self):
        return self.sexo
    
    def setEdad(self, edad:int):
        self.edad = edad

    def getEdad(self):
        return self.edad
    
    def setListNotas(self, listNotas:list[int]):
        self.listNotas = listNotas

    def getListNotas(self):
        return self.listNotas
    
    def setPromedioNotas(self, promedioNotas:int):
        self.promedioNotas = promedioNotas

    def getPromedioNotas(self):
        return self.promedioNotas