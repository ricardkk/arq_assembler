import tabelas

def ler_arquivo(arq):
    lista_inst = []
    arquivo = open(arq, "r")
    linhas = arquivo.readlines()
    
    dicionario_labels = {}

    for indice, item in enumerate(linhas):
        if ":" in item:
            chave = item.strip(': \n')  
            dicionario_labels[chave] = indice


    for i in range(len(linhas)):
        linha = linhas[i].replace(',',' ').replace('(',' ').replace(')','').strip().split()
        lista_inst.append(linha)
    return lista_inst,dicionario_labels


def assemble():
    instrucoes_escreve = []
    for i in range(len(lista_inst)):
        if lista_inst[i][0] in tabelas.tipoJ:
            endereco = dicionario_labels[lista_inst[i][1]]
            op = 2 if lista_inst[i][0] == 'j' else 3
            saida = f"{op}{endereco}"
            instrucoes_escreve.append(saida)

        elif lista_inst[i][0] in tabelas.tipoI:
            if lista_inst[i][0] == 'sw' or lista_inst[i][0] == 'lw':
                val = lista_inst[i][0]
                op = tabelas.instrucoesI[val][0]
                rs = tabelas.registradores[lista_inst[i][1]]
                rt = tabelas.registradores[lista_inst[i][3]]
                const = lista_inst[i][2]
                saida = f"{op}{rs}{rt}{const}"
                instrucoes_escreve.append(saida)

            elif lista_inst[i][0] == 'beq' or lista_inst[i][0] == 'bne':
                val = lista_inst[i][0]
                op = tabelas.instrucoesI[val][0]
                rs = tabelas.registradores[lista_inst[i][1]]
                rt = tabelas.registradores[lista_inst[i][2]]
                const = dicionario_labels[lista_inst[i][3]] 
                saida = f"{op}{rs}{rt}{const}"
                instrucoes_escreve.append(saida)

            elif lista_inst[i][0] == 'lui':
                rs = 0
                rt = tabelas.registradores[lista_inst[i][1]]
                const = lista_inst[i][2]
                saida = f"{op}{rs}{rt}{const}"
                instrucoes_escreve.append(saida)
            else:
                val = lista_inst[i][0]
                op = tabelas.instrucoesI[val][0]
                rs = tabelas.registradores[lista_inst[i][1]]
                rt = tabelas.registradores[lista_inst[i][2]]
                const = lista_inst[i][3]
                saida = f"{op}{rs}{rt}{const}"
                instrucoes_escreve.append(saida)
            

        elif lista_inst[i][0] in tabelas.tipoR:
            if lista_inst[i][0] == 'sll' or lista_inst[i][0] == 'slr':
                sm = lista_inst[i][3]
                rd = tabelas.registradores[lista_inst[i][1]]
                rs = tabelas.registradores[lista_inst[i][2]]
                rt = 0
                saida = f"{op}{rs}{rt}{rd}{sm}{func}"
                instrucoes_escreve.append(saida)

            else:    
                sm = 0
                val = lista_inst[i][0]
                op = tabelas.instrucoesR[val][0]
                func = tabelas.instrucoesR[val][5]
                rd = tabelas.registradores[lista_inst[i][1]]
                rs = tabelas.registradores[lista_inst[i][2]]
                rt = tabelas.registradores[lista_inst[i][3]]
                
                saida = f"{op}{rs}{rt}{rd}{sm}{func}"
                instrucoes_escreve.append(saida)

    return instrucoes_escreve

def escreve_arquivo(arq):
    arquivo = open(arq, "w")
    arquivo.write('v2.0 raw' + '\n')
    for i in lista_hexadecimal:
        arquivo.write(i + '\n')

            



lista_inst,dicionario_labels = ler_arquivo('txt.asm')
instrucoes_escreve = assemble()
lista_binaria = [bin(int(item))[2:] for item in instrucoes_escreve]
lista_hexadecimal = [hex(int(item, 2))[2:] for item in lista_binaria]
escreve_arquivo('alvo.hex')

print(instrucoes_escreve)
print(lista_binaria)
print(lista_hexadecimal)
