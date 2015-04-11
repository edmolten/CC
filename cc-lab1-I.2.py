
import sys
from decimal import Decimal
def show(exp, x):
    print exp, " = ", x

# (b) Primer flotante fl(x) + e_mach no representable
e_mach = 2.0**(-52)

def flNoRepresentable(x):
    while(1):
        print Decimal(x)
        anterior = x
        x += e_mach
        if(x == anterior):
            return x

print "El primer fl(x) tal que fl(x) + e_mach no es representable es: " + str(flNoRepresentable(1.9999999999999))

raw_input("Presiona una tecla para continuar")
            
# (c) Primer flotante fl(x) + e_mach / 2  representable

#def flRepresentable(x):
    #while(1):
      

print "El primer fl(x) tal que fl(x) + e_mach / 2 es representable es: "# + str(flRepresentable(?))


