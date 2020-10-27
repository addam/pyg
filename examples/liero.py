import pyg

# for each player (be it local or network):
# left-right arrows set acceleration while pressed
  # there is low maximum speed and much friction on contact with ground
  # the effect goes in waves after each press
# up-down arrows set aiming speed while pressed
# left&right at the same time cuts a hole in ground before the worm
# "shoot" key invokes the current weapon
# "switch" key changes current weapon to the next in list
# "rope" key, when pressed, shoots the rope
# "rope" key, while not pressed, instantly removes rope
# on contact rope<->ground:
  # rope pulls the player towards the rope
# the view of each player's game is fixed on the player

