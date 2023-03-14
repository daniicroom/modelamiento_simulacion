from Register.person import Person #importar solo una parte del archivo
from typing import List


people:List[Person] = []

while True:
    id: str = input("insert identification: ")
    fullName: str = input("Insert full name: ")
    email: str = input("Insert email: ")

    person = Person(id=id)
    person.setEmail(email)
    person.setFullName(fullName)
    people.append(person)
    stopExecution = input("nueva persona \n1 si \n2 no")
    if(stopExecution == "2"):
        break
    
for i in people:
    print(i.getId(), " - ", i.getFullName(), " - ", i.getEmail())
    
"""
person = Person()
person.setEmail("valbuena@gmail.com")
person.setFullName("Juan")
person.setId("1234")
print(person.getFullName())
"""
