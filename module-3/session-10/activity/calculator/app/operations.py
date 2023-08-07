def get_fractions(frac_str):
    if isinstance(frac_str, (int, float)):
        return frac_str

    if "/" not in frac_str:
        return float(frac_str)
    try:
        return float(frac_str)
    except ValueError:
        num, denom = frac_str.split("/")
        try:
            leading, num = num.split(" ")
            whole = float(leading)
        except ValueError:
            whole = 0
        frac = float(num) / float(denom)
        return whole - frac if whole < 0 else whole + frac


def sum(x, y):

    # This function performs the SUM operation
    # x takes any value and makes it to Float
    # and take any value and make it to Float

    try:
        try:
            if len(x.split("/")) > 0:
                x = float(x.split("/")[0]) / float(x.split("/")[1])

            if len(y.split("/")) > 0:
                y = float(y.split("/")[0]) / float(y.split("/")[1])

        except:
            x = float(x)
            y = float(y)

        return x + y

    except:
        print("The operation cannot be performed :( ")


def substract(a, b):
    minuendo = get_fractions(a)
    sustraendo = get_fractions(b)
    return minuendo - sustraendo


def multiply(a, b):
    multiply = get_fractions(a)
    multiply = get_fractions(b)
    return multiply * multiply


def divide(a, b):
    dividendo = get_fractions(a)
    divisor = get_fractions(b)
    try:
        return dividendo / divisor
    except ZeroDivisionError:
        return "Division between zero"
