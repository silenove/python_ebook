# -*- coding: utf-8 -*-
from visual import *

display(title=u"简单动画".encode("gb2312"), width=500, height=300)

ball = sphere(pos=(-5,0,0), radius=0.5, color=color.red)
wall_right = box(pos=(6,0,0), size=(0.1, 4, 4), color=color.green)
wall_left  = box(pos=(-6,0,0), size=(0.1, 4, 4), color=color.green)

dt = 0.05
ball.velocity = vector(6, 0, 0)

while True:
    rate(1/dt)
    ball.pos = ball.pos + ball.velocity*dt
    if ball.x > wall_right.x-ball.radius or ball.x < wall_left.x+ball.radius:
        ball.velocity.x *= -1

