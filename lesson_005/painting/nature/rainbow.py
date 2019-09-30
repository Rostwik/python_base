import simple_draw as sd


def unicorn_road(x):

    rainbow_colors = (sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
                      sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE)

    s_point = sd.get_point(x, -50)
    radius = 900
    for color_is in rainbow_colors:
        sd.circle(center_position=s_point, radius=radius, color=color_is, width=20)
        radius += 21
