import pyg

# left, right arrow sets pad velocity while pushed down
# pad cannot move outside view
# space creates a projectile
# projectiles move upwards
  # outside of screen, they die
# on collision projectile<->invader, both die
# on collision invader<->bottom screen:
  # display score
  # reset the game
# when there are no invaders and no projectiles:
  # increase round counter
  # create a grid of invaders
# invaders move left to right in a slightly random wave
# invaders move downwards
