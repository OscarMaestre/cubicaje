
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

palets=[
    ("Euro-pallet", 120, 80)
]

NUM_DECIMALES = 2

class Palet(object):
    nombre      :   str
    ancho       :   int
    alto        :   int

    def __init__(self, tupla) -> None:
        super().__init__()
        (self.nombre, self.ancho, self.alto) = tupla
    
    @staticmethod
    def get_palet():
        palet=Palet(choice(palets))
        return palet

    def __str__(self) -> str:
        return f'Nombre {self.nombre}, ancho {self.ancho}, alto {self.alto}'

    
class Solver(object):
    def __init__(self, palet, medida) -> None:
        super().__init__()
        self.palet  =   palet
        self.medida =   medida
        
        
    def get_solucion(self):
        #print(self.medida.ancho)
        self.ratio1=round(self.palet.ancho / self.medida.ancho, NUM_DECIMALES)
        self.ratio2=round(self.palet.ancho / self.medida.alto, NUM_DECIMALES)

        self.ratio3=round(self.palet.alto / self.medida.ancho, NUM_DECIMALES)
        self.ratio4=round(self.palet.alto / self.medida.alto, NUM_DECIMALES)

    def get_texto_ratios(self):
        txt_ratio1=f'{self.palet.ancho} / {self.medida.ancho} = {self.ratio1}'
        txt_ratio2=f'{self.palet.ancho} / {self.medida.alto} = {self.ratio2}'

        txt_ratio3=f'{self.palet.alto} / {self.medida.ancho} = {self.ratio3}'
        txt_ratio4=f'{self.palet.alto} / {self.medida.alto} = {self.ratio4}'

        return [txt_ratio1, txt_ratio2, txt_ratio3, txt_ratio4]

@dataclass
class Medida(object):
    ancho:int
    alto:int
    #largo:int

    def __init__(self):
        self.ancho       =randint(LONGITUD_MINIMA, LONGITUD_MAXIMA)
        self.alto        =randint(LONGITUD_MINIMA, LONGITUD_MAXIMA)
        #self.largo       =randint(LONGITUD_MINIMA, LONGITUD_MAXIMA)
        self.descripcion=[
            ("ancho",self.ancho),
            ("alto",self.alto),
            #("largo", self.largo)
        ]
        shuffle(self.descripcion)

    def get_descripcion_x(self):
        (magnitud0, medida0)=self.descripcion[0]
        (magnitud1, medida1)=self.descripcion[1]
        #descripcion=f'{medida0}x{medida1}x{medida2} ({magnitud0} x {magnitud1} x {magnitud2})'
        descripcion=f'{medida0}x{medida1} ({magnitud0} x {magnitud1})'
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
        self.palet                          =   Palet.get_palet()
        super().__init__()

    def get_descripcion_palet(self):
        texto=f'Se va a usar un palet {self.palet.nombre} cuya base mide {self.palet.ancho} x {self.palet.alto}.'
        return texto

    def resolver(self):
        solver=Solver(self.palet, self.medida)
        ratios=solver.get_solucion()
        return solver.get_texto_ratios()

    def __str__(self):
        texto_introduccion=f'{self.inicio} {self.accion} {self.sintagma} {self.producto} {self.preposicion} {self.ciudad}'
        texto_tenemos=" y tenemos que encargarnos del cubicaje."
        descripcion_medida=self.medida.get_descripcion_x()
        texto_medidas=f' Las medidas del producto ya embalado son {descripcion_medida}. '
        texto_palet=self.get_descripcion_palet()
        texto_final=" y se desea saber cuantas unidades podremos almacenar. Se desea que todos los productos sigan la misma disposición. "
        texto_decimales="Utilizar redondeo a {0} decimales.".format(NUM_DECIMALES)
        return texto_introduccion+texto_tenemos+texto_medidas+texto_palet+texto_final+texto_decimales

    
if __name__=="__main__":
    
    for i in range(0, 10):
        m=Medida()
        p=Palet.get_palet()
        #print(m)
        #print(m.ordenar())
        c=ConstructorEnunciado()
        #print(c)
        print (c.resolver())
