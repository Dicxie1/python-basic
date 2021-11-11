"""
class what describe de entity of the Teacher of de University URACCAN
"""


class Employee:
    """
    Clase empleado que describe a los empleado de la universidad URACCAN
    """
    def __init__(self, name="", lastname="", age=0):
        self.name = name
        self.lastname = lastname
        self.age = age

    def getNombre(self):
        return  self.name

    def getApellido(self):
        return self.lastname

    def getEdad(self):
        return self.age


emp = Employee("Dicxie", "Madrigal", 24)

print("Hola me llama %s %s y tengo %d" % (emp.getNombre(), emp.getApellido(), emp.edad))
