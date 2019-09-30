import simple_draw as sd

def house(point_x, point_y):
    for delta, y in enumerate(range(0, 300, 20)):
        for x in range(0, 500, 50):
            x0 = x - 25 if delta % 2 else x
            l_point = sd.get_point(x0 + point_x, y + point_y)
            t_point = sd.get_point(x0 + point_x + 50, y + point_y + 20)
            sd.rectangle(left_bottom=l_point, right_top=t_point, width=2)
    l_point = sd.get_point(point_x - 25, point_y)
    t_point = sd.get_point(point_x + 500, point_y + 300)
    sd.rectangle(left_bottom=l_point, right_top=t_point, width=2)
    l_window = sd.get_point(point_x + 150, point_y + 100)
    t_window = sd.get_point(point_x + 325, point_y + 200)
    sd.rectangle(left_bottom=l_window, right_top=t_window, color=sd.COLOR_DARK_BLUE, width=0)
    sd.rectangle(left_bottom=l_window, right_top=t_window, color=sd.COLOR_WHITE, width=2)
    point_list = [sd.get_point(point_x - 25, point_y + 300), sd.get_point(point_x + 500, point_y + 300),
                  sd.get_point(point_x + 237.5, point_y + 400)]
    sd.polygon(point_list=point_list, color=sd.COLOR_RED, width=0)
    cross_window_v1 = sd.get_point(point_x + 237.5, point_y + 100)
    cross_window_v2 = sd.get_point(point_x + 237.5, point_y + 200)
    sd.line(start_point=cross_window_v1, end_point=cross_window_v2, color=sd.COLOR_WHITE, width=2)
    cross_window_h1 = sd.get_point(point_x + 150, point_y + 150)
    cross_window_h2 = sd.get_point(point_x + 325, point_y + 150)
    sd.line(start_point=cross_window_h1, end_point=cross_window_h2, color=sd.COLOR_WHITE, width=2)
