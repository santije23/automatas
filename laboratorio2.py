#Elaborar un programa en Python que permita simular el comportamiento del 
# autómata indicado en esta figura. El programa deberá reconocer el 
# lenguaje del autómata.

alfabeto = {0,1}

class Automata:
    def __init__(self,cadena):
        self.estado_inicial="q0"
        self.estado_actual = "q0"
        self.estado_aceptacion="q3"
        self.estado_anterior=None
        self.cadena=cadena

    def sigma(self):
        for x in self.cadena:
            if x == "0" and self.estado_actual=="q0":
                self.estado_anterior=self.estado_actual
                self.estado_actual="q2"
                print(f"Estando en ----> {self.estado_anterior}  Llega un {x} voy a {self.estado_actual}")
                continue
            elif x == "1" and self.estado_actual=="q0":
                self.estado_anterior=self.estado_actual
                self.estado_actual="q1"
                print(f"Estando en ----> {self.estado_anterior}  Llega un {x} voy a {self.estado_actual}")
                continue     

            if x == "0" and self.estado_actual=="q1":
                self.estado_anterior=self.estado_actual
                self.estado_actual="q3"
                print(f"Estando en ----> {self.estado_anterior}  Llega un {x} voy a {self.estado_actual}")
                print(f"El automata llego al estado de aceptacion {self.estado_aceptacion}")
                continue
            elif x == "1" and self.estado_actual=="q1":
                self.estado_anterior=self.estado_actual
                self.estado_actual="q0"
                print(f"Estando en ----> {self.estado_anterior}  Llega un {x} voy a {self.estado_actual}")
                print(f"El automata llego al estado de aceptacion {self.estado_aceptacion}") 
                continue

            if x == "0" and self.estado_actual=="q2":
                self.estado_anterior=self.estado_actual
                self.estado_actual="q0"
                print(f"Estando en ----> {self.estado_anterior}  Llega un {x} voy a {self.estado_actual}")
                print(f"El automata llego al estado de aceptacion {self.estado_aceptacion}")
                continue
            elif x == "1" and self.estado_actual=="q2":
                self.estado_anterior=self.estado_actual
                self.estado_actual="q3"
                print(f"Estando en ----> {self.estado_anterior}  Llega un {x} voy a {self.estado_actual}")
                print(f"El automata llego al estado de aceptacion {self.estado_aceptacion}")
                continue

            if x == "0" and self.estado_actual=="q3":
                self.estado_anterior=self.estado_actual
                self.estado_actual="q2"
                print(f"Estando en ----> {self.estado_anterior}  Llega un {x} voy a {self.estado_actual}")
                continue
            elif x == "1" and self.estado_actual=="q3":
                self.estado_anterior=self.estado_actual
                self.estado_actual="q1"
                print(f"Estando en ----> {self.estado_anterior}  Llega un {x} voy a {self.estado_actual}")
                continue

cadena = input(f"Ingrese la cadena el alfabeto disponible es {alfabeto}:")
ejecucion_automata = Automata(cadena)
ejecucion_automata.sigma()                
                






        

