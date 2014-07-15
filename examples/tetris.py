import pyge
from random import choice as randchoice
#TODO vyresit: je Square pozicovany od sveho stredu, nebo od leveho spodniho rohu?
# Jak jsou pozicovane drawables? Ktere pozicovani je defaultni a ktere se musi nastavit rucne?
#Pro inspiraci: v pripade rucniho pozicovani nekterych actoru by se hodilo spustit transakci a zrusit v pripade kolize

view, game = pyge.createGame(12, 6)

box = pyge.Actor(kinetics=pyge.kinetics.Fixed())
#mozna: box = pyge.Actor(pyge.kinetics.FIXED)
box.drawable = pyge.drawables.Square(gameSize=(1,1))
# the first parameter means: no input connected yet; save to a user-defined variable
box.var.outlineShader = pyge.Shaders.Outline(None, 3, "#000")
# fancy bubble reflection shading
box.drawable.shader = pyge.Shaders.Bubble(box.var.outlineShader, pointLight)

def resetBrick(brick):
	brickShapes = [[(0,0), (1,0), (2,0), (3,0)],
			[(0,0), (1,0), (1,1), (2,1)],
			[(0,0), (1,0), (1,1), (2,0)]]
	colors = [(1,0,0), (0,1,0), (0,0,1)]
	randColor = randchoice(colors)
	for x, y in randchoice(brickShapes):
		newBox = box.clone()
		newBox.position = x, y
		# connect the free socket
		box.var.outlineShader.inputs[0] = pyge.Shaders.Color(randColor)
		brick.children.append(newBox)
	brick.position = 3, 12

brick = pyge.Actor()
kinetics = pyge.kinetics.Quantized(ticksPerSecond=1.0)
kinetics.addForce(pyge.forces.Gravity(-1))
brick.kinetics = kinetics

bottom = pyge.Actor(kinetics=pyge.kinetics.Fixed())
bottom.shape = pyge.shapes.halfPlane("y<0")
game.append(bottom)

brick = pyge.Actor()
resetBrick(brick)

@pyge.collide(selfParent=brick, parent=bottom)  # parent: parent node of the obstacle
@pyge.collide(selfParent=brick, hit=bottom)
def land(collision):
	if collision.direction.y == 0:
		return
	
	bottom.children.extend(brick.children)
	for box in brick.children:
		box.position = pyge.relPosition(bottom, collision.previousPosition) + box.position
	brick.children.clear()
	brick = randomBrick()
	
	bottomRow = [box for box in bottom.children if box.y == 0]
	if len(bottomRow) == game.width:
		# clear the bottom row and shift everything down
		bottom.children.removeAll(bottomRow)
		for box in bottom.children:
			box.y -= 1

@pyge.input(self=brick, gesture='QUANTIZED_MOVEMENT')
def move(event):
	brick.x += event.direction.x

game.append(brick)
pyge.launch(game, windowSize='FULL')
