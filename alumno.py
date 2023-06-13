import unittest

class Almno:


    def  __init__(self,param_nombre,param_mail,param_edad):

        self.nombre=param_nombre
        self.mail=param_mail
        self.edad=0
        

    def cambiar_mail (self , nuevo_mail):
        self.mail = nuevo_mail
    
    
    print("como es su nombre?")
    nombre= input ()
    print("cual es su mail?")
    mail= input()
    print("cual es tu edad?")
    edad = input ()



print (id(Almno))

