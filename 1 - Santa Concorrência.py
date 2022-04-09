import string


def crypto(seq):
    sequencia, finalist, numeros, seqlist = [], [], [], [1]
    for simbolo in seq:
        sequencia.append(simbolo)
    for jk in range(len(seq)):
        numeros.append(jk + 2)
    variavel = 0
    while True:
        soma = 0
        if variavel >= len(sequencia):
            break
        else:
            if sequencia[variavel] == '+':
                seqlist.append(numeros[variavel])
            elif sequencia[variavel] == '-':
                oui = len(sequencia[:variavel])
                if not oui:
                    seqlist.insert(-1, numeros[variavel])
                else:
                    while True:
                        if sequencia[oui] != '-' or oui < 0:
                            break
                        else:
                            soma += 1
                            oui -= 1
                    seqlist.insert(-soma, numeros[variavel])
            variavel += 1
    for it in seqlist:
        finalist.append(str(it))
    return ''.join(finalist)


def deYodafy(phr):
    sublist = []
    phr = phr.split()
    for letras in phr[-1]:
        sublist.append(letras)
    if sublist[-1] in string.punctuation:
        pontofinal = sublist[-1]
        sublist.pop(-1)
        palavra = ''
        for letra in sublist:
            palavra += letra
        phr.pop(-1)
        phr.append(palavra)
        phr = list(reversed(phr))
        palavrafinal = phr[-1] + pontofinal
        phr.insert(-1, palavrafinal)
        phr.pop(-1)
        return ' '.join(phr)
    else:
        phr = list(reversed(phr))
        return ' '.join(phr)


class Merge(object):
    def merge(self, intervalo):
        if len(intervalo) == 0:
            return []
        self.quicksort(intervalo, 0, len(intervalo) - 1)
        pilha = [intervalo[0]]
        for k in range(1, len(intervalo)):
            ultimo = pilha[len(pilha) - 1]
            if ultimo[1] >= intervalo[k][0]:
                ultimo[1] = max(intervalo[k][1], ultimo[1])
                pilha.pop(len(pilha) - 1)
                pilha.append(ultimo)
            else:
                pilha.append(intervalo[k])
        return pilha

    @staticmethod
    def partition(listaa, inicio, fim):
        indic = inicio
        for n in range(inicio, fim):
            if listaa[n][0] <= listaa[fim][0]:
                listaa[n], listaa[indic] = listaa[indic], listaa[n]
                indic += 1
        listaa[fim], listaa[indic] = listaa[indic], listaa[fim]
        return indic

    def quicksort(self, listaa, inicio, fim):
        if inicio < fim:
            indexx = self.partition(listaa, inicio, fim)
            self.quicksort(listaa, inicio, indexx - 1)
            self.quicksort(listaa, indexx + 1, fim)


existe = False
listamerge, listacrypto, listayoda = [], [], []
finalizados = []
add, indx = {}, 0
qtd_process, qtd_final, var, qtd_lista, processos = 0, 0, 0, 0, 0
contagem, indice, reserva, newdic = 0, 1, {}, {}
while True:
    entrada = input().split()
    if entrada[0] == 'halt':
        if not existe:
            print(f'0 processo(s) e 0 comando(s) órfão(s).')
            break
        while True:
            if var >= qtd_process:
                break
            else:
                if len(listacrypto) != 0:
                    print(crypto(listacrypto[0][7:]))
                    listacrypto.pop(0)
                    finalizados.append('crypto')
                    var += 1
                    if var >= qtd_process:
                        break
                if len(listayoda) != 0:
                    print(deYodafy(listayoda[0][9:]))
                    listayoda.pop(0)
                    finalizados.append('yoda')
                    var += 1
                    if var >= qtd_process:
                        break
                if len(listamerge) != 0:
                    final = []
                    lista = listamerge[0][6:].split('] [')
                    for _ in range(len(lista)):
                        if _ == 0:
                            new = lista[_].split('[')
                            lista.pop(_)
                            lista.insert(_, new[1])
                        elif _ == len(lista) - 1:
                            lista[_].split(']')
                            new = lista[_].split(']')
                            lista.pop(_)
                            lista.insert(_, new[0])
                    for item in lista:
                        final.append(list(map(int, item.split(','))))
                    coordenadas = Merge().merge(final)
                    saida = ''
                    for j in coordenadas:
                        saida += str(j) + ' '
                    print(saida.rstrip())
                    listamerge.pop(0)
                    finalizados.append('merge')
                    var += 1
                    if var >= qtd_process:
                        break
        if listacrypto:
            qtd_lista += len(listacrypto)
        if listayoda:
            qtd_lista += len(listayoda)
        if listamerge:
            qtd_lista += len(listamerge)

        while True:
            if indice > len(add):
                break
            else:
                reserva[indice] = add[indice].copy()
                while True:
                    if contagem >= qtd_process or not add[indice]:
                        break
                    for itm in reserva[indice]:
                        if contagem >= qtd_process:
                            break
                        if itm in finalizados:
                            finalizados.remove(itm)
                            add[indice].remove(itm)
                            contagem += 1
                indice += 1
        for key in add:
            if add[key]:
                newdic[key] = add[key]
        if newdic:
            processos = len(newdic)

        print(f'{processos} processo(s) e {qtd_lista} comando(s) órfão(s).')
        break
    else:
        if entrada[0] == 'add':
            indx += 1
            add[indx] = []
            existe = True
            qtd_final += int(entrada[1])
            for i in range(int(entrada[1])):
                processo = input()
                if processo[:6] == 'crypto':
                    listacrypto.append(processo)
                    add[indx].append('crypto')
                elif processo[:8] == 'deYodafy':
                    listayoda.append(processo)
                    add[indx].append('yoda')
                elif processo[:5] == 'merge':
                    listamerge.append(processo)
                    add[indx].append('merge')
        elif entrada[0] == 'process':
            qtd_process += 1
