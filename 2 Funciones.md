# 《💻Sábados Dev ⌨️》| Aprendiendo sobre funciones

## Estructura de las funciones

### Función constante (siempre devuelve el mismo valor)
```haskell
nombre = 3
```
### Función de un parámetro
```haskell
nombre(parametro) = cuerpo
```
### Función de varios parámetros
```haskell
nombre(p1, p2, p3) = cuerpo
```

## Aplicación de funciones
La aplicación de una función es llamar a la función pasandole valores para obtener un resultado.

### Ejemplo:
```haskell
doble(n) = 2 * n
```
Aplicar la función al valor 10:
```haskell
doble(10)
```
Se reemplazan todas las ocurrencias del parámetro `n` en el cuerpo de la función:

doble(10) = 2 * **10**

Resultado: 20

### Ejemplo: Se requiere construir un programa que calcule la cantidad de material que requiere la estructura de un puente dada la siguiente fórmula:
$$ M(l) = 2 + \sqrt{l^2 + 1}$$
Donde l es la longitud del puente. El programa debe convertir el valor a metros ya que se da en pulgadas.

**Solución:**
```haskell
pulg_a_metros(valor) = valor / 39.37007

cantidad_material(longitud) = 2 + sqrt(longitud^2 + 1)
```

**Aplicación:**

Suponiendo que la longitud del puente es de 7874.02 pulgadas

```haskell
cantidad_material(pulg_a_metros(7874.02))
```
Se reemplaza el parámetro `valor` en la función `pulg_a_metros`:

pulg_a_metros(7874.02) = **7874.02** / 39.37007

= 200.0001

Se reemplaza el parámetro `longitud` de la función `cantidad_material`:

cantidad\_material(longitud) = 2 + sqrt(longitud^2 + 1)

cantidad\_material(**200.0001**) = 2 + sqrt(longitud^2 + 1)

Se reemplazan todas las ocurrencias de `longitud` en el cuerpo de la función:

= 2 + sqrt(**200.0001**^2 + 1)

Resultado: 202.002

## Conclusión
El objetivo de estos ejercicios es comprender de manera ejemplificada la forma en que se usan las funciones para obtener resultados. En el desarrollo de software no se realizan únicamente operaciones matemáticas. Las funciones se pueden pensar como procesos computacionales que pueden llamar otras funciones y procesos para obtener un resultado deseado. Recuerda que en este caso la regla es no mutar las variables creadas.
