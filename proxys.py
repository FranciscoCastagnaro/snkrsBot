class Proxys:
    def __init__(self, nombre, telefono, dni, email, password):
        self.nombre = nombre
        self.telefono = telefono
        self.dni = dni
        self.email = email
        self.password = password

p1 = Proxys("FCastagnaro", 112000000, 44759045, "fran@hotmail.com", "testing")
p2 = Proxys("NLuque", 112000000, 44670463, "", "")
p3 = Proxys("SAcevedo", 112000000, 20711288, "san@gmail.com", "testing")

proxys = [p1, p2, p3] 
