from math import inf
def divide (first, second):
    if second > 0:
        result = first / second
        print(result)
    elif second < 0:
        result = first / second
        print(result)
    else:
        print(inf)
        return inf