class Ball2:

    def __init__(self,canvas,x,y,diameter,xa,ya, color):
        self.canvas= canvas
        self.image= canvas.create_oval(x,y,diameter,diameter,fill=color)
        self.xa=xa
        self.ya=ya
    def move(self):
        coordinates = self.canvas.coords(self.image)
        if coordinates[2] >700 or coordinates[0]<0:
            self.xa=-self.xa
        if coordinates[3] > 600 or coordinates[1]<0:
            self.ya = -self.ya

        self.canvas.move(self.image,self.xa,self.ya)
