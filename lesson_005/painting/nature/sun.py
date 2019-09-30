import simple_draw as sd


def sun(x, y):
    sun_point = sd.get_point(x, y)
    sd.circle(center_position=sun_point, radius=50, width=0)
    angle = 0
    for _ in range(10):
        v_sun = sd.get_vector(sun_point, angle=angle, length=100, width=4)
        v_sun.draw(sd.COLOR_YELLOW)
        angle += 36
