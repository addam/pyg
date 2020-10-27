import pyg

# on game start, there are two obstacles at pseudorandom positions
# arrows set speed to one of four directions
# "shoot" key, if gun is loaded:
  # shoots a projectile
  # unloads one round
# "reload" key:
  # unloads all rounds
  # after a timeout, loads full gun
# on contact projectile<->player:
  # delete both
  # player respawns on any empty position after a timeout
# on contact projectile<->obstacle:
  # delete projectile
