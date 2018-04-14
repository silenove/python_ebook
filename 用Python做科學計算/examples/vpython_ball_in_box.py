# -*- coding: utf-8 -*-
from visual import *

display(title=u"简单动画".encode("gb2312"), width=500, height=500)

# 创建球体和6个墙面，墙面设置为半透明，以观察球体的运动轨迹
ball = sphere(pos=(-5,0,0), radius=0.5, color=color.red)
wall_right = box(pos=(6,0,0), size=(0.1, 12, 12), color=color.green, opacity = 0.2)
wall_left  = box(pos=(-6,0,0), size=(0.1, 12, 12), color=color.green, opacity = 0.2)
wall_front = box(pos=(0,-6,0), size=(12, 0.1, 12), color=color.green, opacity = 0.2)
wall_back  = box(pos=(0,6,0), size=(12, 0.1, 12), color=color.green, opacity = 0.2)
wall_bottom = box(pos=(0,0,-6), size=(12, 12, 0.1), color=color.green, opacity = 0.2)
wall_top   = box(pos=(0,0,6), size=(12, 12, 0.1), color=color.green, opacity = 0.2)

dt = 0.05
g = 9.8 # 重力加速度
f = 0.9 # 反弹能量保持系数，1.0表示完全反弹
ball.velocity = vector(8, 6, 12)
bv = arrow(pos = ball.pos, axis=ball.velocity*0.2, color=color.yellow)
ball.trail = curve(color=ball.color)
trail_color = 0 # 轨迹的颜色

while True:
    rate(1/dt)

    # 重力加速度改变z轴方向的速度，不存在反弹时修改速度
    ball.velocity.z -= g * dt

    # 根据速度修改球体的位置
    ball.pos += ball.velocity * dt

    ## 速度为正时判断正方向的墙，速度为负时判断负方向的墙
    ## 处理反弹时需要修正球的位置，使它正好和墙面接触
    # 处理左右墙的反弹
    if ball.velocity.x > 0 and ball.x >= wall_right.x - ball.radius:
        ball.x = wall_right.x - ball.radius
        ball.velocity.x *= -f    
    if ball.velocity.x < 0 and ball.x <= wall_left.x + ball.radius:
        ball.x = wall_left.x + ball.radius
        ball.velocity.x *= -f        

    # 处理前后墙的反弹
    if ball.velocity.y > 0 and ball.y >= wall_back.y - ball.radius:
        ball.y = wall_back.y - ball.radius
        ball.velocity.y *= -f
    if ball.velocity.y < 0 and ball.y <= wall_front.y + ball.radius:
        ball.y = wall_front.y + ball.radius
        ball.velocity.y *= -f

    # 处理上下墙的反弹
    if ball.velocity.z > 0 and ball.z >= wall_top.z - ball.radius:
        ball.z = wall_top.z - ball.radius 
        ball.velocity.z *= -f
    elif ball.velocity.z < 0 and ball.z <= wall_bottom.z + ball.radius:
        ball.z = wall_bottom.z + ball.radius
        ball.velocity.z *= -f

    # 更新速度箭头的位置和方向
    bv.pos = ball.pos
    bv.axis = ball.velocity*0.2
    # 添加球的轨迹点
    ball.trail.append( pos = ball.pos, color = (trail_color, 0, 0))
    trail_color += 1.0/30.0*dt # 30秒后颜色变为全红
    if trail_color > 1.0: trail_color = 1.0
