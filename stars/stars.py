import thumby
import random
import math

thumby.display.setFPS(60)

particles = []

for i in range(1, 30):
    p = [random.randint(0, thumby.display.width),random.randint(0, thumby.display.height),random.randint(1,3),random.randint(0,359)]
    particles.append(p)

print(particles)

while True:
    thumby.display.fill(0) # clear
    
    for p in particles:
        p[0] += math.sin(math.radians(p[3]))
        p[1] -= math.cos(math.radians(p[3]))
        if p[0] < 0 - p[2]: p[0] = thumby.display.width
        if p[0] > thumby.display.width: p[0] = 0 - p[2]
        if p[1] < 0 - p[2]: p[1] = thumby.display.height
        if p[1] > thumby.display.height: p[1] = 0 - p[2]
        thumby.display.drawFilledRectangle(math.floor(p[0]),math.floor(p[1]),p[2],p[2],1)
    
    if thumby.inputJustPressed():
        thumby.reset()
    
    thumby.display.update() # update screen