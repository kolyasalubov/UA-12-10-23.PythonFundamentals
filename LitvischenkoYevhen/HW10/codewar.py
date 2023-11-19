#Regular Ball Super Ball
# class Ball():
#     def __init__(self, ball='regular') -> None:
#         self.ball_type = ball

# ball1 = Ball()
# ball2 = Ball("super")
# ball1.ball_type  #=> "regular"
# ball2.ball_type  #=> "super"

#Color Ghost
from random import randint
class Ghost(object):
    def __init__(self):
        color_arr = ["white", "yellow", "purple", "red"]
        self.color = color_arr[randint(0, 3)]

ghost = Ghost()
print(ghost.color)