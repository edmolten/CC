from decimal import Decimal

#Epsilon machine para flotantes segun estandar ISO 754
e_mach = 2.0**(-52)

#(b)
def flNoRepresentable(i = 0.0, verbose = False):
    """ Encuentra el menor flotante fl(x), buscando desde i, tal que fl(x) + e_mach no sea representable
    i : Flotante inicial para busqueda, por defecto 0.0
    verbose: True si se desea imprimir cada numero analizado, por defecto False
    """
    while(1):
        if verbose :
            print Decimal(i)
        anterior = i
        i += e_mach
        if(i == anterior):
            return i

#(c)
def flRepresentable(i = 0.0, verbose = False):
    """Encuentra el mayor flotante fl(x), buscando desde i, tal que fl(x) + e_mach / 2 sea representable
    i : Flotante inicial para busqueda, por defecto 0.0
    verbose : True si se desea imprimir cada numero analizado, por defecto False
    """
    while(1):
        if verbose :
            print Decimal(i)
        anterior = i
        i += e_mach/2
        if i - anterior == 0:
            return anterior - e_mach/2

#Usando funciones
print "Obteniendo menor flotante fl(x) + e_mach no representable"
fl = flNoRepresentable(2 - 10 * e_mach)
print "El menor fl(x) tal que fl(x) + e_mach no es representable es: ", Decimal(fl)
raw_input("Presiona una tecla para continuar")
print "Obteniendo mayor flotante fl(x) + e_mach / 2  representable"
fl = flRepresentable(1 - 10 * e_mach)
print "El mayor fl(x) tal que fl(x) + e_mach / 2 es representable es: ", Decimal(fl)
raw_input("Presiona una tecla para salir")
