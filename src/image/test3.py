import turtle

# 设置色彩模式是RGB:
turtle.colormode(255)

turtle.lt(90)

lv = 14
l = 120
s = 45

turtle.width(lv)

# 初始化RGB颜色:
r = 0
g = 0
b = 0
turtle.pencolor(r, g, b)

turtle.penup()
turtle.bk(l)
turtle.pendown()
turtle.fd(l)

def draw_tree(l, level):
    global r, g, b
    # save the current pen width
    w = turtle.width()

    # narrow the pen width
    turtle.width(w * 3.0 / 4.0)
    # set color:
    r = r + 1
    g = g + 2
    b = b + 3
    turtle.pencolor(r % 200, g % 200, b % 200)

    l = 3.0 / 4.0 * l

    turtle.lt(s)
    turtle.fd(l)

    if level < lv:
        draw_tree(l, level + 1)
    turtle.bk(l)
    turtle.rt(2 * s)
    turtle.fd(l)

    if level < lv:
        draw_tree(l, level + 1)
    turtle.bk(l)
    turtle.lt(s)

    # restore the previous pen width
    turtle.width(w)

turtle.speed("fastest")

draw_tree(l, 4)

turtle.done()
