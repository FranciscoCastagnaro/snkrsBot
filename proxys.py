class Proxys:
    def __init__(self, nombre, telefono, dni, email, password):
        self.nombre = nombre
        self.telefono = telefono
        self.dni = dni
        self.email = email
        self.password = password

p1 = Proxys("FCastagnaro", 1126441825, 44759045, "francastagnaro@hotmail.com", "Pedopedo10")
p2 = Proxys("NLuque", 1144248611, 44670463, "", "")
p3 = Proxys("SAcevedo", 1160265312, 20711288, "sucusraices@gmail.com", "Sucusraices123")

proxys = [p1, p2, p3] 