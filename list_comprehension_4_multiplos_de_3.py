"""
Dada uma lista de números inteiros, crie uma nova lista que contenha apenas os
números que são múltiplos de 3 e que também sejam maiores que 5.

numeros = [1, 3, 4, 6, 9, 12, 15, 18, 20, 21, 24]

Requisito: Utilize list comprehension para gerar a nova lista.

Dica: Você pode usar a combinação de dois operadores (% para encontrar múltiplos de 3
e > para verificar se o número é maior que 5).
"""

numeros = [1, 3, 4, 6, 9, 12, 15, 18, 20, 21, 24]

multiplos = [num for num in numeros if num > 5 and num % 3 == 0]

print(multiplos)