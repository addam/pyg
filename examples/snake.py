import pyg

# head goes one grid step each time step
# each dot copies the position of its parent
# pressing a key changes the head direction
  # direction towards the first dot is ignored
# collision head<->dot:
  # displays score
  # resets the game
# collision head<->wall:
  # moves head to the other wall
# collision head<->apple:
  # creates a new dot,
  # resets the apple to any empty position

game, view = pyg.create()
player = pyg.local()
head = game.Actor()
apple = game.Actor()

class Dot(game.Actor):
  def __init__(self, parent):
    @parent.on_move
    def follow(self, parent):
      self.position = parent.position

head.on_contact(Dot)(head.die)

@head.on_contact(view.border)
def mirror(head, border):
  head.position = pyg.mirror(head.position, 'vertical' if border in (view.top, view.bottom) else 'horizontal')

@head.on_contact(apple)
def grow(head, apple):
  tail.append(Dot(tail[-1]))
  apple.move()

@game.on_start
def start():
  tail = [head, Dot(head)]
  
