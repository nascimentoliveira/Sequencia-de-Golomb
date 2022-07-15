Repositório de programas e scripts utilitários para problemas aplicáveis à Sequência de Solomon Golomb.

Inspired by Problem #10049 Self-describing Sequence in

https://onlinejudge.org/external/100/10049.pdf

# Sequência Auto Descritiva de Solomon Golomb

Em homenagem ao matemático, engenheiro e professor Solomon Wolf Golomb,
a chamada sequência (auto descritiva) de Solomon Golomb (ou simplesmente
sequência de Golomb, que por vezes é também chamada de sequência de
Silverman) é definida como uma sequência de números inteiros positivos
($\mathbb{Z^{*+}}$), monoticamente crescrente (ou não decrescente se
preferir), de inteiros $a_1, a_2, ..., a_n$ com as seguintes
propriedades:

1.  $a_n$ é o número de vezes que $n$ ocorre na sequência;
2.  $a_1 = 1$;
3.  quando $n > 1$, $a_n$ é o menor inteiro único que torna possível a
    primeira condição.

O primeiro número da sequência é 1, a partir daí o número $n$ ocorre
$a_n$ vezes na sequência ordenada e não decrescente, isto é,
$a_1 \le a_2 \le a_3 \le ... \le a_n$

Dessa forma calculamos:

-   $a_1 = 1$ → 1 ocorre uma vez na sequência;
-   $a_2 = 2$ → 2 ocorre duas vezes na sequência;
-   $a_3 = 2$ → 3 ocorre duas vezes na sequência;
-   $a_4 = 3$ → 4 ocorre três vezes na sequência;
-   $a_5 = 3$ → 5 ocorre três vezes na sequência;
-   $a_6 = 4$ → 6 ocorre quatro vezes na sequência;
-   $a_n = x$ → n ocorre $x$ vezes na sequência;
-   \...

| n | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 |  12 | 13 | ... |
|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|
| $a_n$ | 1 | 2 | 2 | 3 | 3 | 4 | 4 | 4 | 5 | 5 | 5 | 6 | 6 | ... | 

Seguindo as propriedades, podemos mostrar os 45 primeiros números da
sequência:

Sequência de Golomb = (1, 2, 2, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 6, 7,
7, 7, 7, 8, 8, 8, 8, 9, 9, 9, 9, 9, 10, 10, 10, 10, 10, 11, 11, 11, 11,
11, 12, 12, 12, 12, 12, 12, 13, \...)

# 1) Gerador da lista dos $n$ primeiros números da Sequência de Golomb
Podemos desenvolver uma função, utilizando Python 3 para gerar uma lista
com os primeiros $n$ valores da sequência.

``` {.python}
#Python 3 script to list the first n numbers of the sequence

def golombListGenerator(n):
    
    #unexpected parameter
    if (n <= 0):
        print("Expected positive values (nth position in the sequence, starting at 1)!")
        return 

    GolombSequence = list()
    a_n = 1
    
    #generate list 
    while (len(GolombSequence) < n):
        GolombSequence.append(a_n)
        #add n, (a_n - 1) more times
        for _ in range(GolombSequence[a_n - 1] - 1):
            if (len(GolombSequence) == n): return tuple(GolombSequence)
            GolombSequence.append(a_n)
        a_n += 1
```

``` {.python}
from time import time
inicio = time()

firstNumbers = 45
print("The first " +str(firstNumbers) + " numbers of the sequence are:\n", golombListGenerator(firstNumbers))

fim = time()
print("\n⏱️ Runtime: " + str(fim - inicio)[:7] + " seconds.")
```
Output:

``` {.python}
    The first 45 numbers of the sequence are:
     (1, 2, 2, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 8, 9, 9, 9, 9, 9, 10, 10, 10, 10, 10, 11, 11, 11, 11, 11, 12, 12, 12, 12, 12, 12, 13)

    ⏱️ Runtime: 0.00217 seconds.
```

------------------------------------------------------------------------

Gerando a lista completa podemos consultar o elemento de interesse e sua
posição.

E quando estamos interessados em um elemento que está muito distante do
início da sequência?

Gerar uma lista muito grande de elementos da sequência pode esbarrar em
limitações de tempo e espaço. Além disso é desconfortável procurar um
elemento visualmente em uma lista grande.

**Se estivermos interessados em uma posição $n$ específica na sequência,
será que conseguimos informações sobre o elemento nesta posição sem
gerar a lista completa?**

A resposta é sim, de várias maneiras!

# 2) Consultando a $n-ésima$ posição na sequência

A primeira e mais imediata é utilizar a relação de recorrência
desenvolvida por Colin Mallows:

$a_1 = a(1) = 1$

$a_n = a(n) = 1 + a(n - a(a(n-1)))$

$a_{n+1} = a(n + 1) = 1 + a(n + 1 - a(a(n)))$

Abaixo, uma função desenvolvida em Python 3 que implementa essa relação
de recorrência.


``` {.python}
#Python 3 script to find the n-th number of Golomb's sequence

def findNthElement(n):
    
    #unexpected parameter
    if (n <= 0):
        print("Expected positive values (nth position in the sequence, starting at 1)!")
        return

    #recursion stop condition (base)
    elif (n == 1):
        return 1

    return 1 + findNthElement(n - findNthElement(findNthElement(n - 1)))
```

``` {.python}
inicio = time()

searchedIndex = 45
print("The element #" + str(searchedIndex) +  " of the sequence is " + str(findNthElement(searchedIndex)))

fim = time()
print("\n⏱️ Runtime: " + str(fim - inicio)[:7] + " seconds.")
```
Output:

``` {.python}
    The element #45 of the sequence is 13

    ⏱️ Runtime: 2.04841 seconds.
```

------------------------------------------------------------------------

Note que a implementação da relação de recorrência pode, muito
facilmente, enfrentar problemas de tempo de execução e stack overflow.
Explicitamente ela não retorna a sequência de Golomb, porém internamente
ela armazena os elementos na pilha de recursão.

Logo nos valores mais baixos de posição do elemento da sequência, você
irá notar que é mais eficiente gerar a lista toda e depois consultar.

**Existe outra solução?**

Sim, uma segunda solução é mapear a sequência em uma \"*sequência
auxiliar*\" que indica a posição do primeiro $n$ na sequencia de Golomb.

# 3) Solução alternativa para consultar a $n-ésima$ posição na sequência

Veja:

-   $a_1 = 1$ → 1 ocorre pela primeira vez (e única) na posição 1;
-   $a_2 = 2$ → 2 ocorre pela primeira vez na posição 2;
-   $a_3 = 2$
-   $a_4 = 3$ → 3 ocorre pela primeira vez na posição 4;
-   $a_5 = 3$
-   $a_6 = 4$ → 4 ocorre pela primeira vez na posição 6;
-   ...

Dessa forma, conseguimos mapear a sequência original da seguinte forma:

| n | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 |  12 | 13 | ... |
|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|
| índice do $1^{st}$ (n) | 1 | 2 | 4 | 6 | 9 | 12 | 16 | 20 | 24 | 29 | 34 | 39 | 45 | ... | 

Abaixo, a implementação da função que gera a \"*sequência auxiliar*\" e
a armazena no vetor \"*indexFirst*\" (índice do primeiro). Ela busca,
iterativamente o índice do último $n$ e acrescenta a esse índice o
número de vezes que $n$ ocorre, gerando portanto o índice em que $n+1$
ocorre primeiro.

-   $1^{st}$ ocorrência do 2 = $1^{st}$ ocorrência do 1 + quantas vezes
    o 1 ocorre;
-   $1^{st}$ ocorrência do 3 = $1^{st}$ ocorrência do 2 + quantas vezes
    o 2 ocorre;
-   $1^{st}$ ocorrência do 4 = $1^{st}$ ocorrência do 3 + quantas vezes
    o 3 ocorre;
-   $1^{st}$ ocorrência do 5 = $1^{st}$ ocorrência do 4 + quantas vezes
    o 4 ocorre;
-   $1^{st}$ ocorrência do $n$ = $1^{st}$ ocorrência do $n-1$ + quantas
    vezes o $n-1$ ocorre;
-   $1^{st}$ ocorrência do $n+1$ = $1^{st}$ ocorrência do $n$ + quantas
    vezes o $n$ ocorre;
-   \...

Talvez você esteja se perguntando: como saber quantas vezes um
determinado $n$ ocorre se não construímos a lista?

A resposta para essa pergunta é a chave desta solução. Como a sequência
é não descrescente, podemos consultar a quantidade de ocorrências de
determinado número na própria lista auxiliar.

Por exemplo: como saber quantas vezes o 5 ocorre? Vamos olhar nossa
\"*sequência auxiliar*\"

| n | 1 | 2 | 3 | 4 | 5 | 6 | 
|--|--|--|--|--|--|--|
| índice do $1^{st}$ (n) | 1 | 2 | 4 | 6 | 9 | ? |

O primeiro 3 ocorre na posição 4 ($a_4 = 3$) e o primeiro 4 ocorre na
posição 6 ($a_6 = 4$) logo podemos restaurar a sequência original:

| n | ... | 4 | 5 | 6 | ... |
|--|--|--|--|--|--|
| $a_n$ | ... | 3 | 3 | 4 | ... | 

Portanto, concluímos com convicção que o 5 ocorre 3 vezes na sequência.

-   $1^{st}$ ocorrência do $n+1$ = $1^{st}$ ocorrência do $n$ + quantas
    vezes o $n$ ocorre;
-   $1^{st}$ ocorrência do 6 = $1^{st}$ ocorrência do $5$ + quantas
    vezes o $5$ ocorre;
-   $1^{st}$ ocorrência do 6 = 9 + 3 = 12;

| n | 1 | 2 | 3 | 4 | 5 | 6 | 7 |  
|--|--|--|--|--|--|--|--|
| índice do $1^{st}$ (n) | 1 | 2 | 4 | 6 | 9 | 12 |? |

Dessa forma construímos a \"*sequência auxiliar*\".

``` {.python}
#Python 3 script to alternatively find the nth number of the Golomb sequence
#non-recurrent

def alternativefindNthElement(n):
    
    #unexpected parameter
    if (n <= 0):
        print("Expected positive values (nth position in the sequence, starting at 1)!")
        return

    #vector that stores the index of the first occurrence of n
    #indexFirst[n] <- index of the first occurrence of n (starting at 1)
    indexFirst = [1]
    a_n = 2
    temp = int()

    #build index vector
    while True:
        #find how many times n occurs (n occurs a_n times)
        #as we do not know the value of a_n, we look for the index  
        #in the vector indexFirst which encompasses the position a_n
        for lastIndex in indexFirst:
            if lastIndex < a_n : temp = lastIndex
            else: break
        
        #indexFirst[n+1] = indexFirst[n] + how many times n occurs
        nextIndex = indexFirst[-1] + (indexFirst.index(temp)+1)
        
        #stop condition
        if (nextIndex > n): break   

        indexFirst.append(nextIndex)

        a_n += 1
    
    return len(indexFirst)
```

``` {.python}
inicio = time()

searchedIndex = 45
print("The element #" + str(searchedIndex) +  " of the sequence is " + str(alternativefindNthElement(searchedIndex)))

fim = time()
print("\n⏱️ Runtime: " + str(fim - inicio)[:7] + " seconds.")
```
Output:

``` {.python}
    The element #45 of the sequence is 13

    ⏱️ Runtime: 0.00080 seconds.
```
------------------------------------------------------------------------

Repare que é muito mais eficiente que a solução recursiva, tanto em
complexidade de tempo quanto de espaço.

Até agora, desenvolvemos um script para gerar a lista com a sequência de
Golomb e dois outros scripts para consultar qual valor está em
determinada posição $n$ da sequência ($a_1, a_2, ..., a_n, ...$).

**Como fazer para consultar as todas as posições em que determinado
valor ocorre?**

# 4) Consultando determinado valor na sequência

Podemos aproveitar o algoritmo acima e alterar a condição de parada para
buscar onde começa o indice do $(n+1)$-ésimo número. Com isso, saberemos
o índice onde $n$ occorre pela primeira vez e o índice em que $n+1$
ocorre pela primeira vez. O intervalo de índices onde $n$ ocorre é
limitado por esses dois valores (intervalo fechado no primeiro, aberto
no segundo).

``` {.python}
#Python 3 script to find the range of indices where 
#the number n appears in the Golomb's sequence

def indexInterval(n):
    
    if (n <= 0):
        print("Expected positive values (starting at 1)!")
        return
    
    #vector that stores the index of the first occurrence of n
    #indexFirst[n] <- index of the first occurrence of n (starting at 1)
    indexFirst = [1]
    a_n = 2
    temp = int()

    #build index vector
    while True:
        #find how many times n occurs (n occurs a_n times)
        #as we do not know the value of a_n, we look for the index  
        #in the vector indexFirst which encompasses the position a_n
        for lastIndex in indexFirst:
            if lastIndex < a_n : temp = lastIndex
            else: break
        
        #indexFirst[n+1] = indexFirst[n] + how many times n occurs
        #factor 1 appears because array index starts at 0
        nextIndex = indexFirst[-1] + (indexFirst.index(temp) + 1)
        
        #stop condition
        if (len(indexFirst) > n): break   

        indexFirst.append(nextIndex)

        a_n += 1
    
    return tuple(range(indexFirst[-2], indexFirst[-1]))
```

``` {.python}
inicio = time()

n = 12
print("The number " + str(n) +  " occurs in the positions " + str(indexInterval(n)))

fim = time()
print("\n⏱️ Runtime: " + str(fim - inicio)[:7] + " seconds.")
```
Output:

``` {.python}
  The number 12 occurs in the positions (39, 40, 41, 42, 43, 44)

    ⏱️ Runtime: 0.00062 seconds.
```

## Resumo

Com esses algoritmos, é possível:

1.  Gerar a sequência de Golomb até onde precise (ou sua máquina
    permita);
2.  Encontrar o número $a_n$ informando sua posição $n$ na sequência;
3.  Encontrar o intervalo ($a_k, a_{k+1}, ..., a_{k+(a_n-1)}$) de
    posições em que o número $n$ ocorre;
4.  Em consequência de 3 ou adaptando o retorno do algoritmo em 2 é
    possível saber a quantidade de vezes que determinado número $n$
    ocorre na sequência;

Implemente os algoritmos acima, troque os parâmetros, teste. Implemente
uma das sugestões em 4. Entenda e aprenda.

------------------------------------------------------------------------
```
   "A maturidade vem com os obstáculos superados."
```
