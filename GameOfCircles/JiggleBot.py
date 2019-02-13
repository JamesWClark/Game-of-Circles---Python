class JiggleBot:
    speed = 4
    diameter = 50
    c = color(100, 100, 255)

    def __init__(self, x, y, team):
        self.x = x
        self.y = y
        self.team = team

    def move(self):
        self.y += random(-self.speed, self.speed)
        self.x += random(-self.speed, self.speed)
        self.x = constrain(self.x, 0, width)
        self.y = constrain(self.y, 0, height)

    def display(self):
        fill(self.c)
        ellipse(self.x, self.y, self.diameter, self.diameter)

    def animate(self):
        self.move()
        self.display()
