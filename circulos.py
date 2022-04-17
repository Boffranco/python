import random
#init()
ventana=(500,500)
pantalla=display.set_mode(ventana)
display.set_mode(ventana)
display.set_caption("SteCUACK")

mouse=0
mousey=0
color1=(255,0,0)
color2=(0,0,255)
fondoimg=image.load("paisage.jpg")
reloj=time.Clock()
r1=Rect(350,350,20,20)
r2=Rect(mousex,mousey,50,50)
salir=False
while salir==False:
    for evento in event.get():
       if evento.type==MOUSEMOTION:
        (mousex,mousey)=mouse.get_pos()
        pantalla.blit(fondoimg(0,0))

        r2.center=mouse.get_pos()
        if r2.center.colliderec(r1):
           r1.movee(10,100)

        if evento.type==pygame.Quit:
            salir=True

        draw.rect(pantalla,color1,r1)
        draw.rect(pantalla,color2,r2)
        display.update()
    quit()  
