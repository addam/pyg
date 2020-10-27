import pyg

view, game = pyg.createGame(1, 1)
view.zoom(0.9)  # display space this wide around the playfield

pad = pyg.Actor()
pad.position = (0.5, 0)
padHeight = 0.05
pad.drawable = pyg.drawables.Rectangle(0.2, padHeight)
pad.calculateShape()
shader = pyg.shaders.Color("gray")
shader = pyg.shaders.Bubble(shader, height=0, rounded=padHeight)
shader = pyg.shaders.Rounded(shader, padHeight)
pad.drawable.shader = shader

ball = pyg.Actor()
pad.children.append(ball)
ball.shape = circle(padHeight)
ball.y = padHeight
ball.drawable = pyg.drawables.Image("ball.svg", position='CENTERED', gameSize=0.05)
ball.kinetics.collisionFactor = 1.0

walls = pyg.Actor(kinetics=pyg.kinetics.Fixed())
walls.shape = pyg.shapes.Polygon((0,-1), (0,1), (1,1), (1,-1))
game.append(walls)

box = pyg.Actor()
box.drawable = pyg.drawables.Rectangle(0.1, 0.05)
box.drawable.color = "#ff0"
box.calculateShape()
box.groups.add('box')
shader = pyg.shaders.Outline(box.drawable.defaultShader, "#440")
shader = pyg.shaders.Noise(shader, 0.1)
box.drawable.shader = shader

@collision(self=ball, group='box')
def hitBrick(collision):
	ball.speed += collision.speed()
	brick = collision.hit
	game.detach(brick)
	if brick.var.bonus:
		bonus = pyg.Actor()
		bonus.groups.add('bonus')
		bonus.speed.y = -0.1
		bonus.var.bonusType = brick.var.brickType
		game.append(bonus)
		pyg.sound.play("bonus.flac")

@collision(self=ball, hit=pad)
def hitPad(collision):
	ball.speed.x = (ball.x - pad.x) / pad.width
	ball.speed.y = (1-ball.speed.y**2)**0.5

@collision(self.pad, group='bonus')
def hitBonus(collision):
	bonus = collision.hit
	game.detach(bonus)
	bt = bonus.var.bonusType
	if bt == 'ENLARGE' or bt == 'DIMINISH':
		step = 0.05 if bt == 'ENLARGE' else -0.05 if pad.width > 0.1 else 0
		pad.width += step

# create a level
for 
for x in range(10):
	for y in range(4):
		newBrick = brick.clone()
		brick.position = x/10, 1 - y/20
		if randint(
