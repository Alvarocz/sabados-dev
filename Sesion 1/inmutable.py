def suma_inmutable(lista):
    """ Versión inmutable, funcional """
    def recorrer(fragmento, acumulador):
        if fragmento:
            num = fragmento[0]
            return recorrer(fragmento[1:], acumulador + num)
        else:
            return acumulador

    return recorrer(lista, 0)