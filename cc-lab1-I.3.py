from math import log, floor, sin

# (a)
def epsilon(fl):
    """Retorna el valor estimado de la diferencia entre fl y el
    siguiente flotante representable
    fl : flotante a analizar
    """
    exp = floor(log(float(fl),2))
    return abs((2.0**(exp+1) - 2.0**(exp)) / 2.0**(52))

# (b)
#matplotlib no viene con Python 2.7 y tiene muchas dependencias.
#No se asegura el correccto funcionamiento del siguiente codigo.

from matplotlib import pyplot

fls = []
for i in range(-50,51):
    fls.append(2.0**(i))
pyplot.plot(fls, [epsilon(i) for i in fls])
pyplot.ylabel('epsilon')
pyplot.xlabel('flotante')
pyplot.grid(True)
pyplot.show()    

