def format_float(number):
    return "{:.3f}".format(number)


def format_dd(dd):
    return "(" + format_float(dd[0]) + ", " + format_float(dd[1]) + ")"
