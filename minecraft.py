from crypt import crypt
from pyexpat import model
from statistics import mode
from ursina import *

def update():
    if held_keys['a']:
        test_square.x -= 4 * time.dt

app = Ursina()

test_square = Entity(
    model = 'quad', 
    color = color.red, 
    scale = (1,5),
    position = (5,4)
)

sans_texture = load_texture('assets/crypto.png')
sans = Entity(model = 'quad',
texture = sans_texture)

app.run()