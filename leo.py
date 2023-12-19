from turtle import Turtle, listen, Screen
leo = Turtle ()
tela = Screen()
leo.speed(2)
leo.pensize(6)

escolha =''

leo.color in ['pink', 'red', 'black', 'blue']

def quadrado():
    leo.forward(100)
    leo.right(90)
    leo.forward(100)
    leo.right(90)

def circulo():
    r = 45
    leo.pendown()
    leo.circle(r)


while(escolha != 0):

    print("----------------------")
    print("o Que voce que ver desenhado?")
    print ("1: Circulo")
    print("2: Quadrado")
    print("0:para")
    escolha = int(input())
    cor = input("Que cor voce quer ver desenhado? ")
    leo.color ()
    if escolha == 1:
        circulo()
    if escolha ==2:
        Quadrado()

listen()
tela.mainloop()