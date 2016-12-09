import time


def speed_test(func):
    def wrapper(*args, **kwargs):
        time1 = time.time()
        ret = func(*args, **kwargs)
        time2 = time.time()
        print '%s function took %0.3f ms' % (
            func.func_name, (time2 - time1) * 1000.0)
        return ret

    return wrapper


def chunks(l, n):
    n = max(1, n)
    return [l[i:i + n] for i in range(0, len(l), n)]


def flatten(l):
    return [item for sublist in l for item in sublist]


def gflatten(l):
    return (item for sublist in l for item in sublist)
