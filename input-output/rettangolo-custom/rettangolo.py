lato_minore = float(input("Inserire il lato minore: "))
lato_maggiore = float(input("Inserire il lato maggiore: "))

area = float(lato_minore * lato_maggiore)
perimetro = float((lato_minore * 2) + (lato_maggiore * 2))

colore = str(input("Inserire il colore del perimetro: "))

import turtle

t = turtle.Turtle()

if((colore == "red") | (colore == "pink") | (colore == "blue")):
    t.color(colore)
else:
    t.color("black")

t.speed(1)
t.forward(lato_minore)
t.left(90)
t.forward(lato_maggiore)
t.left(90)
t.forward(lato_minore)
t.left(90)
t.forward(lato_maggiore)

turtle.done()

print("L'area è " + str(area))
print("Il perimetro è " + str(perimetro))