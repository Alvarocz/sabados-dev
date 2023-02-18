from typing import List

def promedio(numeros: List[float]):
    if numeros == []:
        return 0
    return sum(numeros) / len(numeros)


resultado = promedio([1, 2, 3, 4, 5])
assert resultado == 3.0
print(resultado)

assert promedio([]) == 0
print(promedio([]))