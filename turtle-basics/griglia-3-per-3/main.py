# Il programma disegna un quadrato, in senso antiorario.

import turtle

pippo = turtle.Turtle(); # crea una tartaruga, chiamata pippo

# rettangolo esterno
pippo.forward(300);
pippo.left(90);
pippo.forward(300);
pippo.left(90);
pippo.forward(300);
pippo.left(90);
pippo.forward(300);

# aggiungere codice qui sotto
pippo.penup()
pippo.left(90)
pippo.forward(100)
pippo.pendown()
pippo.left(90)
pippo.forward(300)

pippo.penup()
pippo.right(90)
pippo.forward(100)
pippo.right(90)
pippo.pendown()
pippo.forward(300)

pippo.penup()
pippo.left(90)
pippo.forward(100)
pippo.left(90)
pippo.forward(100)
pippo.pendown()
pippo.left(90)
pippo.forward(300)

pippo.penup()
pippo.right(90)
pippo.forward(100)
pippo.right(90)
pippo.pendown()
pippo.forward(300)

turtle.done()
