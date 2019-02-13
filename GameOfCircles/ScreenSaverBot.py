class ScreenSaverBot:
    xspeed = 8
    yspeed = 4
    diameter = 50
    c = color(0, 255, 255)

    def __init__(self, x, y, team):
        self.x = x
        self.y = y
        self.team = team

    def move(self):
        self.x += self.xspeed
        self.y += self.yspeed
        if self.x < 0 or self.x > width:
            self.xspeed *= -1
        if self.y < 0 or self.y > height:
            self.yspeed *= -1

    def display(self):
        fill(self.c)
        ellipse(self.x, self.y, self.diameter, self.diameter)

    def animate(self):
        self.move()
        self.display()
