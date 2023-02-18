lista = list(range(1, 11))


def suma(lista):
    """ Versión mutable, imperativa """
    sum = 0
    for i in lista:
        sum += i  # Muta a sum
    return sum


def suma_inmutable(lista):
    """ Versión inmutable, funcional """
    def recorrer(fragmento, acumulador):
        if fragmento:
            num = fragmento[0]
            return recorrer(fragmento[1:], acumulador + num)
        else:
            return acumulador

    return recorrer(lista, 0)


resultado_mut = suma(lista)
resultado_inmut  = suma_inmutable(lista)
print(resultado_mut)
print(resultado_inmut)

assert resultado_mut == sum(lista)
assert resultado_inmut == sum(lista)
