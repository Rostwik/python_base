import simple_draw as sd


def snowdrift(x, y, quantity):
    while quantity > 0:
        x0 = x
        for _ in range(quantity):
            point = sd.get_point(x0, y)
            sd.snowflake(center=point, length=20)
            x0 += 20
        x += 20
        y += 20
        quantity -= 2


