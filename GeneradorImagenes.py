#!/usr/bin/python3


from PIL import Image, ImageDraw
from dataclasses import dataclass

import PIL

@dataclass
class Imagen(object):
    ancho               :int
    alto                :int      
    nombre_archivo      :str

    def __init__(self, ancho, alto, nombre_archivo) -> None:
        self.COLOR_FONDO    =   "#ffffff"
        self.COLOR_LINEAS   =   "#0000ff"
        self.alto   =alto
        self.ancho  =alto
        self.imagen =Image.new("RGB",(ancho, alto), color="#ffffff")

        self.nombre_archivo=nombre_archivo
    
    def guardar(self):
        self.imagen.save(self.nombre_archivo)

    @staticmethod
    def anadir_caja(imagen, ancho, alto, largo, ox=20, oy=20, color="#0000ff", ancho_linea=3):
        w, h = ancho, alto
        shape = [ox, oy, ancho, alto]
        longitud_diagonales_profundidad=
        dibujante=ImageDraw.Draw(imagen)
        dibujante.rectangle(shape, outline=color, width=ancho_linea)
        imagen.show()


if __name__=="__main__":
    i=Imagen(100,100, "prueba.png")
    Imagen.anadir_caja(i.imagen, 50,30, 70)
    i.guardar()