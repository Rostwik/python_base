import simple_draw as sd


def smile(x, y, color):
    lb_el = sd.get_point(x, y)
    rt_el = sd.get_point(x + 50, y + 42.5)
    sd.ellipse(left_bottom=lb_el, right_top=rt_el, color=color, width=1)
    x += 12.5
    y += 31.75
    cp = sd.get_point(x, y)
    sd.circle(center_position=cp, radius=3, color=color)
    x += 25
    cp = sd.get_point(x, y)
    sd.circle(center_position=cp, radius=3, color=color)
    l_smile = sd.get_point(x - 30, y - 15)
    mid_l_smile = sd.get_point(x - 22.5, y - 20)
    mid_r_smile = sd.get_point(x - 5, y - 20)
    r_smile = sd.get_point(x + 5, y - 15)
    smile_list = [l_smile, mid_l_smile, mid_r_smile, r_smile]
    sd.lines(point_list=smile_list, color=color, closed=False, width=1)


