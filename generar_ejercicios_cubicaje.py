
from random import choice, randint, shuffle
from dataclasses import dataclass


CIUDADES=[
    "Moscú", "Nueva York", "Boston", "Ciudad del Cabo", "Manila",
    "Shenzen", "Hong Kong", "Baltimore"
]

PRODUCTOS=[
    "latas", "cartuchos de tóner", "discos duros", "botes de conserva",
    "cajas de galletas", "conservas", "paquetes de folios"
]

INICIOS=[
    "Se pretende", "Se quiere", "Queremos", "Una empresa va a", "Nuestra empresa quiere",
    "La firma ACME desea"
]

ACCION=[("exportar", "hacia"), ("importar", "desde")]

SINTAGMAS=["un cargamento de", "una carga de", "un envío de", "una compra de"]

LONGITUD_MINIMA=7
LONGITUD_MAXIMA=15

@dataclass
class Medida(object):
    ancho:int
    alto:int
    largo:int

    def __init__(self):
        self.ancho       =randint(LONGITUD_MINIMA, LONGITUD_MAXIMA)
        self.alto        =randint(LONGITUD_MINIMA, LONGITUD_MAXIMA)
        self.largo       =randint(LONGITUD_MINIMA, LONGITUD_MAXIMA)
        self.descripcion=[
            ("ancho",self.ancho),
            ("alto",self.alto),
            ("largo", self.largo)
        ]
        shuffle(self.descripcion)

    def get_descripcion_x(self):
        (magnitud0, medida0)=self.descripcion[0]
        (magnitud1, medida1)=self.descripcion[1]
        (magnitud2, medida2)=self.descripcion[2]
        descripcion=f'{medida0}x{medida1}x{medida2} ({magnitud0} x {magnitud1} x {magnitud2})'
        return descripcion
    def func_ordenacion(self, medida):
        return medida[1]
    def ordenar(self):
        self.descripcion.sort(key=self.func_ordenacion)
        print(self.descripcion)

@dataclass
class ConstructorEnunciado(object):
    inicio      :str
    accion      :str
    preposicion :str
    ciudad      :str
    sintagma    :str
    producto    :str
    medida      :Medida
    def __init__(self):
        self.inicio                         =   choice(INICIOS)
        (self.accion,self.preposicion)      =   choice(ACCION)
        self.ciudad                         =   choice(CIUDADES)
        self.sintagma                       =   choice(SINTAGMAS)
        self.producto                       =   choice(PRODUCTOS)
        self.medida                         =   Medida()
        super().__init__()

    def __str__(self):
        texto_introduccion=f'{self.inicio} {self.accion} {self.sintagma} {self.producto} {self.preposicion} {self.ciudad}'
        texto_tenemos=" y tenemos que encargarnos del cubicaje."
        descripcion_medida=self.medida.get_descripcion_x()
        texto_medidas=f' Las medidas son {descripcion_medida}'
        return texto_introduccion+texto_tenemos+texto_medidas

    
if __name__=="__main__":
    
    for i in range(0, 10):
        m=Medida()
        print(m)
        print(m.ordenar())
        c=ConstructorEnunciado()
        print(c)
