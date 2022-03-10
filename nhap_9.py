from tkinter import*
from Ball2 import *
import time
window=Tk()
window.title("Multiple balls")
window.geometry("700x600")
canvas= Canvas(window,width=700,height=600,bg="grey")
canvas.pack()

volley_ball= Ball2(canvas,0,0,60,1,1,"blue")
tennis_ball= Ball2(canvas,0,0,40,7,8,"yellow")
basket_ball= Ball2(canvas,0,0,125,4,5,"red")

while True:
    volley_ball.move()
    window.update()
    time.sleep(0.000008)

    tennis_ball.move()
    basket_ball.move()


window.mainloop()
