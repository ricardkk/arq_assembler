#Tabela de instruções
# 6 itens -> R
# 4 itens -> I
# 2 itens -> J
tipoR = ['sll','slr','jr','mfhi','mflo','mult','multu','div','divu','add','addu',
         'sub','subu','and','or','slt','sltu','mul']
tipoI = ['beq','bne','addi','addiu','slti','sltiu','andi','ori','lui','lw','sw']
tipoJ = ['j','jal']

instrucoesR = {
    'sll'       : ['0','rs','rt','rd','sa','0'],
    'slr'       : ['0','rs','rt','rd','sa','2'],
    'jr'        : ['0','rs','rt','rd','sa','8'],
    'mfhi'      : ['0','rs','rt','rd','sa','16'],
    'mflo'      : ['0','rs','rt','rd','sa','18'],
    'mult'      : ['0','rs','rt','rd','sa','24'],
    'multu'     : ['0','rs','rt','rd','sa','25'],
    'div'       : ['0','rs','rt','rd','sa','26'],
    'divu'      : ['0','rs','rt','rd','sa','27'],
    'add'       : ['0','rs','rt','rd','sa','32'],
    'addu'      : ['0','rs','rt','rd','sa','33'],
    'sub'       : ['0','rs','rt','rd','sa','34'],
    'subu'      : ['0','rs','rt','rd','sa','35'],
    'and'       : ['0','rs','rt','rd','sa','36'],
    'or'        : ['0','rs','rt','rd','sa','37'],
    'slt'       : ['0','rs','rt','rd','sa','42'],
    'sltu'      : ['0','rs','rt','rd','sa','43'],
    'mul'       : ['28','rs','rt','rd','sa','2']
}

instrucoesI = {
    'beq'       : ['4','rs','rt','imed'],
    'bne'       : ['5','rs','rt','imed'],
    'addi'      : ['8','rs','rt','imed'],
    'addiu'     : ['9','rs','rt','imed'],
    'slti'      : ['10','rs','rt','imed'],
    'sltiu'     : ['11','rs','rt','imed'],
    'andi'      : ['12','rs','rt','imed'],
    'ori'       : ['13','rs','rt','imed'],
    'lui'       : ['15','rs','rt','imed'],
    'lw'        : ['35','rs','rt','imed'],
    'sw'        : ['43','rs','rt','imed']
}

instrucoesJ = {
    'j'         : ['2','ende'],
    'jal'       : ['3','ende']
}

registradores = {
        '$zero': '0',
        '$at': '1',
        '$v0': '2',
        '$v1': '3',
        '$a0': '4',
        '$a1': '5',
        '$a2': '6',
        '$a3': '7',
        '$t0': '8',
        '$t1': '9',
        '$t2': '10',
        '$t3': '11',
        '$t4': '12',
        '$t5': '13',
        '$t6': '14',
        '$t7': '15',
        '$s0': '16',
        '$s1': '17',
        '$s2': '18',
        '$s3': '19',
        '$s4': '20',
        '$s5': '21',
        '$s6': '22',
        '$s7': '23',
        '$t8': '24',
        '$t9': '25',
        '$k0': '26',
        '$k1': '27',
        '$gp': '28',
        '$sp': '29',
        '$fp': '30',
        '$ra': '31',
    }

