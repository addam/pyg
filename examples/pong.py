import pyg

# up, down and W, S keys set velocity of each pad while pressed
# pads cannot move outside view
# in flying state:
  # on collision ball<->pad or ball<->top, bottom wall:
    # ball bounces
  # on collision ball<->left, right wall:
    # increase score of the winner
    # put ball in waiting state to the loser
# in waiting state:
  # left and D (depending on who holds the ball) releases the ball
  # ball is released in 45 degrees
