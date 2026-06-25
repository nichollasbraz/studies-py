## Exercício 2

O método `index()` da classe `list` retorna o índice da primeira ocorrência do valor na lista. Entretanto, caso o valor não esteja na lista, uma exceção é levantada. Implemente uma função chamada `safeIndex()` que recebe como entradas uma lista e um valor e retorna o índice da primeira ocorrência do valor na lista. Caso o valor não esteja na lista, a função deve imprimir uma mensagem informando que o valor não está na lista e retornar `None`.

```
>>> lst = [23,42,54,39]
>>> lst.index(54)
2
```
``` 
>>> lst.index(0)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: 0 is not in list
```

```
>>> lst = [23,42,54,39]
>>> safeIndex(lst,54)
2
```
``` 
>>> safeIndex(lst,0)
O valor 0 não está na lista
None
``` 
