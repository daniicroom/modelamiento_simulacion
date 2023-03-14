class Person:
    id:str = None
    fullName: str = None
    email: str = None

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
    
    def setEmail(self, email:str):
        self.email = email

    def getEmail(self):
        return self.email