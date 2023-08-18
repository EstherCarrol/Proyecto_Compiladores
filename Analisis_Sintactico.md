# Análisis Sintáctico

## Terminales no utilizados

| Terminal       |
|----------------|
| BINARIO        |
| DOMINO         |
| EOF            |
| HEXADECIMAL    |
| MAYA           |
| OCTAL          |
| ROMANO         |

## Gramática

| Regla | Producción                |
|-------|---------------------------|
| 0     | S' -> conversion          |
| 1     | conversion -> NUMERO sistema_conversion |
| 2     | sistema_conversion -> ID |

## Terminales, con reglas donde aparecen

| Terminal     | Reglas       |
|--------------|--------------|
| BINARIO      |       -      |
| DOMINO       |       -      |
| EOF          |       -      |
| HEXADECIMAL  |       -      |
| ID           | 2            |
| MAYA         |       -      |
| NUMERO       | 1            |
| OCTAL        |       -      |
| ROMANO       |       -      |
| error        |       -      |

## No terminales, con reglas donde aparecen

| No terminal         | Reglas       |
|---------------------|--------------|
| S'                  | 0            |
| conversion          | 1            |
| sistema_conversion  | 2            |


| No terminal        | Reglas                        |
|--------------------|-------------------------------|
| conversión         | 0. S' -> conversión           |
| sistema_conversion | 1. conversión -> NUMERO sistema_conversion |

## Método de análisis

| Método      |
|-------------|
| LALR        |

## Estados

### Estado 0

| Regla | Acción                        |
|-------|-------------------------------|
| (0)   | S' -> . conversión             |
| (1)   | conversión -> . NUMERO sistema_conversion |
|       | **NUMERO**: shift (estado 2)  |
|       | **conversión**: shift (estado 1) |

### Estado 1

| Regla | Acción                |
|-------|-----------------------|
| (0)   | S' -> conversión .    |

### Estado 2

| Regla | Acción                        |
|-------|-------------------------------|
| (1)   | conversión -> NUMERO . sistema_conversion |
| (2)   | sistema_conversion -> . ID   |
|   -   | **ID**: shift (estado 4)     |
|   -   | **sistema_conversion**: shift (estado 3) |

### Estado 3

| Regla | Acción                                         |
|-------|------------------------------------------------|
| (1)   | conversión -> NUMERO sistema_conversion .     |
|   -   | **$end**: reduce (conversión -> NUMERO sistema_conversion .) |

### Estado 4

| Regla | Acción                                         |
|-------|------------------------------------------------|
| (2)   | sistema_conversion -> ID .                    |
|   -   | **$end**: reduce (sistema_conversion -> ID .) |
