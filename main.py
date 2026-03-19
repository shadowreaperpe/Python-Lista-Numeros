
lista = []
lista_pares = []
lista_impares = []
lista_maior_idade = []
lista_menor_idade = []
for numero in range(5):
    idade = int(input("Digite o Numero Ou Idade: "))
    while idade < 0:
        print("Idade Invalida")
        idade = int(input("Digite a Idade novamente: "))
    lista.append(idade)
media = sum(lista)/len(lista)
menu = """
Oque Voce Quer Fazer Agora
1 - Saber os números pares
2 - Saber os números ímpares
3 - Saber a maior idade da lista
4 - Saber o menor número da lista
5 - Mostrar apenas os mais velhos
6 - Mostrar apenas os mais novos
7 - Mostra A Divisão Do Seu Grupo
8 - Deixar Em Ordem Crescente
9 - Deixar Em Ordem Decrescente
10 - nada
"""

while True:
    print(menu)
    pergunta = int(input("Oque Você Quer Escolher? "))
    if pergunta == 1:
        for numero in lista:
            if numero % 2 == 0:
                lista_pares.append(numero)
        print(lista_pares)
    elif  pergunta == 2:
        for numero in lista:
            if numero % 2 != 0:
                lista_impares.append(numero)
        print(lista_impares)
    elif pergunta == 3:
        print("O Maior Numero Da Lista é", max(lista))
    elif pergunta == 4:
        print("O Menor Numero Da Lista é", min(lista))
    elif pergunta == 5:
        for numero in lista:
            if numero >= 18:
                lista_maior_idade.append(numero)
        print(lista_maior_idade)
    elif pergunta == 6:
        for numero in lista:
            if numero < 18:
                lista_menor_idade.append(numero)
        print(lista_menor_idade)

    elif pergunta == 7:
        if 0 <= media <= 25:
            print("O Grupo é Jovem, a Media De Idade é", media)
        elif 26 <= media <= 60:
            print("O Grupo é Adulto, a Media De Idade é", media)
        elif media > 60:
            print("O Grupo é Idoso, a Media De Idade é", media)

    elif pergunta == 8:
        lista.sort()
        print(lista)
    elif pergunta == 9:
        lista.sort(reverse=True)
        print(lista)
    elif pergunta == 10:
        print("OK")
    repetir = str(input("Quer Escolher Outra Opção? ")).upper()
    if repetir == "S":
        lista_pares.clear()
        lista_impares.clear()
        lista_maior_idade.clear()
        lista_menor_idade.clear()
        continue
    elif repetir == "N":
        break

