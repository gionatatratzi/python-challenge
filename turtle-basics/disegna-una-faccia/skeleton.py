import turtle;

t = turtle.Turtle()

# imposta il colore della linea
t.color("Black")

# imposta il colore di riempimento
t.fillcolor("Yellow")

# disegna un quadrato pieno di lato 50
t.begin_fill()
t.forward(50)
t.left(90)
t.forward(50)
t.left(90)
t.forward(50)
t.left(90)
t.forward(50)
t.left(90)
t.end_fill()

# solleva la testina
t.up()

# sposta la tartaruga alla nuova posizione (x,y)
t.setpos(150,0)

# abbassa la testina
t.down()

# imposta il colore della linea in modalità RGB (Red, Green, Blue)
t.color("yellow")

# disegna un cerchio di raggio 50
t.circle(50)

#faccia
t.penup()
t.color("purple")
t.right(90)
t.forward(50)
t.right(90)
t.forward(200)
t.pendown()
t.circle(100)

t.penup()
t.forward(70)
t.left(90)
t.forward(50)
t.pendown()
t.circle(20)

t.penup()
t.left(80)
t.forward(120)
t.pendown()
t.circle(20)

t.penup()
t.right(90)
t.forward(100)
t.right(90)
t.pendown()
t.forward(100)

turtle.done()