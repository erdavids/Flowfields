w, h = 1000, 1000

grid_height = 100
grid_width = 100

cell_size_h = h/grid_height
cell_size_w = w/grid_width

noise_scale = .05

change_chance = .05

particles = []

flowfield = []

max_vel = 1

class Particle:
    def __init__(self, location):
        self.location = location
        self.velocity = PVector(0, 0)
        self.acceleration = (0, 0)
    
    def update(self):
        grid_x = int(self.location[0]/cell_size_w)
        grid_y = int(self.location[1]/cell_size_h)
        flowforce = flowfield[int(grid_y + grid_x * grid_height)]
        self.acceleration = flowforce
        self.velocity = PVector(self.velocity[0] + self.acceleration[0], self.velocity[1] + self.acceleration[1])
        #self.acceleration = (0, 0)
        
        self.velocity.setMag(10)
            
        self.location = (self.location[0] + self.velocity[0], self.location[1] + self.velocity[1])
    
    def edge(self):
        if (self.location[0] >= w):
            self.location = (0, self.location[1])
        elif (self.location[0] < 0):
            self.location = (w - 1, self.location[1])
        if (self.location[1] >= h):
            self.location = (self.location[0], 0)
        elif (self.location[1] < 0):
            self.location = (self.location[0], h-1)
        
    def display(self):
        stroke(random(100, 200), random(100, 200), random(100), 10)
        point(self.location[0], self.location[1])

def stroke_random_color():
    stroke(random(50, 200), random(50, 200), random(50, 200), 150)

def setup():
    size(w, h)
    
    background(30, 30, 30)
    stroke_random_color()
    
    for x in range(grid_width):
        for y in range(grid_height):
            n = noise(x * noise_scale, y * noise_scale) * (2 * PI)
            # pushMatrix()
            # translate(cell_size_w * x, cell_size_h * y)
            # rotate(n)
            # line(0, 0, cell_size_w, 0)
            # popMatrix()
            
            flowfield.append(PVector.fromAngle(n))
    
    print(len(flowfield))
    for i in range(10000):
        particles.append(Particle((random(w), random(h))))
                                 
def draw():
    for i in range(len(particles)):
        particles[i].update()
        particles[i].display()
        particles[i].edge()
