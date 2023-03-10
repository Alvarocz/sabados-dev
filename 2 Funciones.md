# 銆婐煉籗谩bados Dev 鈱笍銆媩 Aprendiendo sobre funciones

## Estructura de las funciones

### Funci贸n constante (siempre devuelve el mismo valor)
```haskell
nombre = 3
```
### Funci贸n de un par谩metro
```haskell
nombre(parametro) = cuerpo
```
### Funci贸n de varios par谩metros
```haskell
nombre(p1, p2, p3) = cuerpo
```

## Aplicaci贸n de funciones
La aplicaci贸n de una funci贸n es llamar a la funci贸n pasandole valores para obtener un resultado.

### Ejemplo:
```haskell
doble(n) = 2 * n
```
Aplicar la funci贸n al valor 10:
```haskell
doble(10)
```
Se reemplazan todas las ocurrencias del par谩metro `n` en el cuerpo de la funci贸n:

doble(10) = 2 * **10**

Resultado: 20

### Ejemplo: Se requiere construir un programa que calcule la cantidad de material que requiere la estructura de un puente dada la siguiente f贸rmula:
$$ M(l) = 2 + \sqrt{l^2 + 1}$$
Donde l es la longitud del puente. El programa debe convertir el valor a metros ya que se da en pulgadas.

**Soluci贸n:**
```haskell
pulg_a_metros(valor) = valor / 39.37007

cantidad_material(longitud) = 2 + sqrt(longitud^2 + 1)
```

**Aplicaci贸n:**

Suponiendo que la longitud del puente es de 7874.02 pulgadas

```haskell
cantidad_material(pulg_a_metros(7874.02))
```
Se reemplaza el par谩metro `valor` en la funci贸n `pulg_a_metros`:

pulg_a_metros(7874.02) = **7874.02** / 39.37007

= 200.0001

Se reemplaza el par谩metro `longitud` de la funci贸n `cantidad_material`:

cantidad\_material(longitud) = 2 + sqrt(longitud^2 + 1)

cantidad\_material(**200.0001**) = 2 + sqrt(longitud^2 + 1)

Se reemplazan todas las ocurrencias de `longitud` en el cuerpo de la funci贸n:

= 2 + sqrt(**200.0001**^2 + 1)

Resultado: 202.002

## Conclusi贸n
El objetivo de estos ejercicios es comprender de manera ejemplificada la forma en que se usan las funciones para obtener resultados. En el desarrollo de software no se realizan 煤nicamente operaciones matem谩ticas. Las funciones se pueden pensar como procesos computacionales que pueden llamar otras funciones y procesos para obtener un resultado deseado. Recuerda que en este caso la regla es no mutar las variables creadas.
