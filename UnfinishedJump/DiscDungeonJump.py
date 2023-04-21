import thumby

# # # To do
# dynamic collisions
# sawblades and enemies
# multiple maps

thumby.display.setFPS(120)

arrPlayer = bytearray([15,13])
sprPlayer = thumby.Sprite(2,4,arrPlayer,8,8)

velocity = [0,0]

def lerp(a, b, f):
    return (a * (1.0 - f)) + (b * f)

while True:
    thumby.display.fill(0)
    thumby.display.drawSprite(sprPlayer)
    thumby.display.update()
    
    if thumby.buttonL.pressed():
        velocity[0] = -0.2
    if thumby.buttonR.pressed():
        velocity[0] = 0.2
        
    sprPlayer.x += velocity[0]
    
    sprPlayer.y += velocity[1]
    
    velocity[0] = lerp(velocity[0], 0, 0.1)
    velocity[1] = lerp(velocity[1], 1, 0.01)
    
    if sprPlayer.y > thumby.display.height - 8: sprPlayer.y = thumby.display.height - 8

    if thumby.actionJustPressed():
        velocity[1] = -.5
        