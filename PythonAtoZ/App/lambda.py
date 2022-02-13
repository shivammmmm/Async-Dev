fun = (lambda x: x*2)
print(fun(5))

thread = [1, 2, 3, 4, 5, 6]
print(list(map(fun , thread)), "\n")
print("Using Lambda \n")
print(list(map(lambda x: x*2, thread)), "\n")
print("Using List Comprehensions \n")
print(list(x*2 for x in thread))

