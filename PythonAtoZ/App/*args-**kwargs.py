def display_person(*args):
    print(args)

result,_ = (4,5)
print(result)

def outer_fun(a, b):
    def inner_fun(c, d):
        return c + d
    return inner_fun(a, b)

res = outer_fun(5, 10)
print(res)

def outer_fun(a, b):
    def inner_fun(c, d):
        return c + d

    return inner_fun(a, b)

result = outer_fun(5, 10)
print(result)
