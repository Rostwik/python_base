import simple_draw as sd

def draw_branches(point, angle, length):
    if length < 10:
        return
    v1 = sd.get_vector(start_point=point, angle=angle, length=length, width=1)
    v1.draw(color=sd.COLOR_GREEN)
    next_point = v1.end_point
    rnd_angle = sd.random_number(18, 42)
    rnd_length_kof = sd.random_number(6, 9)
    next_angle0 = angle - rnd_angle
    next_angle1 = angle + rnd_angle
    next_length = length * rnd_length_kof / 10
    draw_branches(point=next_point, angle=next_angle0, length=next_length)
    draw_branches(point=next_point, angle=next_angle1, length=next_length)