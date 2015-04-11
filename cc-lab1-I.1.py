def show(exp, x):
    print exp, " = ", x

#Distacia 1.1

print "Distacia 1.1"
x = 1.0 + 2.0**(-52)
exp = "1.0 + 2.0**(-52)"
show(exp, x)
x -= 1.0
exp = "(" + exp + ") - 1.0"
show(exp, x)
x += 2.0**(-54)
exp = "(" + exp + ") + 2.0**(-54)"
show(exp, x)
x += 1.0
exp = exp + " + 1.0"
show(exp,x)
print

#Distancia 1.2

print "Distacia 1.2"
x = 1.0 + 2.0**(-54)
exp = "1.0 + 2.0**(-54)"
show(exp, x)
x -= 1.0
exp = "(" + exp + ") - 1.0"
show(exp, x)
x += 2.0**(-52)
exp = "(" + exp + ") + 2.0**(-52)"
show(exp, x)
x += 1.0
exp = exp + " + 1.0"
show(exp,x)
print

#Distancia 2.1

print "Distancia 2.1"

x = 5.0 - 4.0 
exp = "5.0 - 4.0"
show(exp,x)
x += 2.0**(-52)
exp = "(" + exp + ") + 2.0**(-52)"
show(exp,x)
print

#Distacia 2.2

print "Distancia 2.2"

x = 4.0 - 2.0**(-52)
exp = "4.0 - 2.0**(-52)"
show(exp,x)
x = 5.0 - x
exp = "5.0 - (" + exp + ")"
show(exp,x)
print

#Distacia 3.1

print "Distancia 3.1"

x1 = 2.0**(-53) - 2.0**(-53)
exp1 = "2.0**(-53) - 2.0**(-53)"
show(exp1,x1)
x2 = 1.0 + 0.5
exp2 = "1.0 + 0.5"
show(exp2,x2)
x2 += 0.25
exp2 += " + 0.25"
show(exp2,x2)
x = x1 + x2
exp = "(" + exp1 + ") + (" + exp2 + ")"
show(exp,x)
print

#Distacia 3.2

print "Distancia 3.2"
x = 1.0 + 0.5
exp = "1.0 + 0.5"
show(exp,x)
x += 0.25
exp += " + 0.25"
show(exp,x)
x += 2.0**53
exp = "(2.0**53 + (" + exp + "))"
show(exp,x)
x -= 2.0**53
exp += " - 2.0**53"
show(exp,x)
print
