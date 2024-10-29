def mayor(a, b):
    resultado = True

    for pos, elem in enumerate(a):
        if (a[pos] <= b[pos]):
            resultado = False
            break

    return resultado


print(mayor([1, 2, 3], [0, 1, 2])) # True
print(mayor([0, 2, 3], [1, 2, 3])) # False