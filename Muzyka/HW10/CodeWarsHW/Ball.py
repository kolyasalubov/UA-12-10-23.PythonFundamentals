"""
Create a class Ball. Ball objects should accept one argument for "ball type" when instantiated.
If no arguments are given, ball objects should instantiate with a "ball type" of "regular."
"""


class Ball(object):
    def __init__(self, ball_type='regular'):
        self.ball_type = ball_type

    def get_ball_type(self):
        return self.ball_type


normal_ball = Ball()
special_ball = Ball(ball_type='special')

print(normal_ball.get_ball_type())
print(special_ball.get_ball_type())

"""
Test Results:
Log
regular
special
Fixed Tests
Basic Test Cases
Test Passed
Test Passed
Completed in 0.02ms
Completed in 0.04ms
You have passed all of the tests! :)
"""
