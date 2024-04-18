# Autor: Leonardo Gama Teixeira
# Componente Curricular: 2024.1 EXA854 - MI - ALGORITMOS (TP03) 
# Concluido em: 15/04/2024
# Declaro que este código foi elaborado por mim de forma individual e não contém nenhum
# trecho de código de outro colega ou de outro autor, tais como provindos de livros e
# apostilas, e páginas ou documentos eletrônicos da Internet. Qualquer trecho de código
# de outra autoria que não a minha está destacado com uma citação para o autor e a fonte
# do código, e estou ciente que estes trechos não serão considerados para fins de avaliação.

# Essa parte é apenas para qual menu inicial, onde o usuario seleciona
# se vai configurar o progama, usar a versão padrão(a do problema) 
# ou encerrar o progama
InvalidOp = True
while InvalidOp == True:
    NumOpMenu = input('''
-------Menu de inicial---------
                      
1- Para configurar o progama
2- Para usar versão padrão(Evento EngComp da UEFS)
3- Para encerrar o progama
                      
Selecione uma opção: ''')

    match NumOpMenu:
# Após o usuario selecionar uma opção alguma das opções será iniciada
        case "1":          
# O progama será configurado pelo usuario e depois
# o progama irá para a tela de vendas
            ingressos = int(input("\nDigite a quantidade de ingressos: "))
            precoInt = float(input("Digite o preço do ingresso: R$"))
            precoMeia = float(input("Digite o preço da meia-entrada: R$"))
            precoDesc = float(input("Digite o preço do ingresso com desconto, caso não tenha digite 0: R$"))
            curso1 = input("Digite o primeiro curso que está participando das vendas: ")
            curso2 = input("Digite o segundo curso que está participando das vendas: ")
            InvalidOp = False
        case "2":
# Versão do problema proposto vai ser selecionada e as os valores
# do problema serão utilizados nas respectivas variáveis
            print("\nVersão padrão selecionada\n")
            ingressos = 2000
            precoInt = 30      
            precoMeia = 15
            precoDesc = 10
            curso1 = "Biologia"
            curso2 = "Enfermagem"
            InvalidOp = False
        case "3":
# Encerra o progama
            print("Encerrando progama")
            exit()
        case _:
            print("Digite uma opção válida!")

# Após selecionar ou a versão ou configurar começa a tela de vendas onde eu pré-criei algumas
# variaveis fora do while para guardar as informações e elas não serem perdidas nos loops

IntVendas = 0
CortesiaFinal = 0
DAcortesias = 0
EstudanteVendas = 0
IdosoVendas = 0
CortesiaVenda = 0
DescontoVendas = 0
EventoFim = 2
CortCurso1 = 0
CortCurso2 = 0

while ingressos > 0 and int(EventoFim) > 1:
    InvalidOp = True
    while InvalidOp == True:
        NumOpIng = input('''
-------Tela de Vendas------

1- Inteira
2- Meia-entrada(Estudante)
3- Meia-entrada(idoso)
4- Descontos
5- Cortesia
                         
Selecione um tipo de ingresso: ''')
        if NumOpIng.isdecimal() == True and 5 >= int(NumOpIng) >= 1:
            InvalidOp = False
        else:
            print("\nDigite uma opção válida!\n")
# o usuario seleciona qual tipo de ingresso será vendido e pergunta quantos ingressos foram 
# vendidos e soma suas idades com o uma estrutura de repetição, que repetira a pergunta de
# idade para cada ingresso que foi vendido.
    InvalidOp = True
    while InvalidOp == True:
        CursoOp = input(f'''
1- {curso1}
2- {curso2} 
Qual o curso do vendedor? ''')
        if CursoOp.isdecimal() == True and 2 >= int(CursoOp) >= 1:
            InvalidOp = False
        else:
            print("\nDigite uma opção válida\n")
    InvalidOp = True
    while InvalidOp == True:
        VendasIng = input("\nQuantos ingressos foram vendidos? ")
        if VendasIng.isdecimal() == True:
            InvalidOp = False
            VendasIng = int(VendasIng)
        else:
            print("\nDigite uma opção válida\n")

    IdadeSoma = 0
    for idade in range(0,VendasIng):
        InvalidOp = True
        while InvalidOp == True:
            InvalidOp = True
            idade = input("\nDigite a idade de cada cliente: ")
            if idade.isdecimal() == True and 120 >= int(idade) >= 1:
                InvalidOp = False
                idade = int(idade)
                IdadeSoma += idade
            else:
                print("\nDigite uma idade válida!\n")

    Cortesia = int(VendasIng) // 10
    InvalidOp = True
    while InvalidOp == True:
        match NumOpIng:
# Caso o usuario selecione a opção inteira 
            case "1":
                ingressos -= VendasIng
                IntVendas += VendasIng
                InvalidOp = False
# Caso o usuario selecione a opção meia-estudante
            case "2":
# usei if-else para o usuario confirmar que as compras são validas
# em todas as opções abaixo foram usadas essa confirmação para saber
# se as compras são validas
                NumOpTipo = int(input("Todas compras foram mostradas a carteira de estudante?\n1-Sim\n2-Não"))
                if NumOpTipo == 1:
                    ingressos -= VendasIng
                    EstudanteVendas += VendasIng
                    InvalidOp = False
                else:
                    IdadeSoma -= idade
                    print("Garanta que todas as compras sejam comprovadas antes de continuar com o cadastro por favor.")
                    InvalidOp = False

# Caso o usuario selecione a opção meia-idoso
            case "3":
                NumOpTipo = int(input("Todas compras foram mostradas a carteira idoso?\n1-Sim\n2-Não"))
                if NumOpTipo == 1:
                    ingressos -= VendasIng
                    EstudanteVendas += VendasIng
                    InvalidOp = False
                else:
                    IdadeSoma -= idade
                    print("Garanta que todas as compras sejam comprovadas antes de continuar com o cadastro por favor.")
                    InvalidOp = False
# Caso o usuario selecione a opção desconto
            case "4":
                NumOpTipo = int(input("Todas compras foram mostradas o devido comprovante de desconto?\n1-Sim\n2-Não"))
                if NumOpTipo == 1:
                    ingressos -= VendasIng
                    EstudanteVendas += VendasIng
                    InvalidOp = False
                else:
                    IdadeSoma -= idade
                    print("Garanta que todas as compras sejam comprovadas antes de continuar com o cadastro por favor.")
                    InvalidOp = False
# Caso o usuario selecione a opção cortesia DA
            case "5":
                ingressos -= VendasIng
                DAcortesias += VendasIng   
                InvalidOp = False  
            case _:
                print("Digite uma opção válida!")      
# Ao final o progama verifica se é possivel dar cortesias ao vendedor
    if (ingressos - Cortesia) >= 0:
        ingressos -= Cortesia
        CortesiaFinal += Cortesia
        if ingressos > 0:
# Caso seja possivel serão mostradas as cortesias e os ingressos 
# depois é perguntado ao usuario se gostaria de encerrar o evento
            print(f"Foram dadas {Cortesia} cortesias ainda\nrestam {ingressos} ingressos.")
            InvalidOp = True
            while InvalidOp == True:
                EventoFim = input("Gostaria de encerrar o evento?\n1-Sim\n2-Não")
                if EventoFim.isdecimal() == True and  2 >= int(EventoFim) >= 1:
                    InvalidOp = False
                else:
                    print("\nDigite uma opção válida\n")
        else:
# Caso de para adcionar as cortesias e não restar mais ingressos sera impresso isso
            print(f"Foram dadas {Cortesia} cortesias\nnão restam mais ingressos.")
    else:
# Caso não seja possivel dar cortesias sera impresso isso
        print(f"Não foi possivel adcionar as as {Cortesia} cortesias,pois restam apenas {ingressos} ingressos.")

    if CursoOp == 1:
        CortCurso1 += Cortesia
    else:
        CortCurso2 += Cortesia

# Aqui são feitos os calculos para imprimir os valores finais do progama
RsMeia = ((EstudanteVendas+IdosoVendas)*precoMeia)
RsInt = (IntVendas*precoInt)
RsDesc = (DescontoVendas*precoDesc)
RsTotal = RsMeia + RsInt + RsDesc
VendasIngFinal = IntVendas + EstudanteVendas + IdosoVendas + DescontoVendas + DAcortesias + CortesiaFinal
MediaIdade = IdadeSoma / (VendasIngFinal - CortesiaFinal)

if EstudanteVendas > IdosoVendas and EstudanteVendas > IntVendas and EstudanteVendas > DescontoVendas:
    MaisVendas = "Meia-entrada para estudantes"
elif IdosoVendas > EstudanteVendas and IdosoVendas > IntVendas and EstudanteVendas > DescontoVendas:
    MaisVendas = "Meia-entrada para idosos"
elif DescontoVendas > EstudanteVendas and DescontoVendas > IdosoVendas and DescontoVendas > IntVendas:
    MaisVendas = "Desconto"
else:
    MaisVendas = "Inteira"
# Impressão final do progama
print(f'''
Total de ingressos emitidos: {VendasIngFinal};\n
Ingressos não emitidos: {ingressos};\n 
Total de meia-entradas para estudantes vendidas: {EstudanteVendas};\n
Total de meia-entradas para idosos vendidas: {IdosoVendas};\n
Total de inteiras vendidas: {IntVendas};\n
Total de descontos vendidos: {DescontoVendas};\n
Cortesias para DA e convidados: {DAcortesias};\n
Cortesias para o curso de {curso1}: {CortCurso1};\n
Cortesias para o curso de {curso2}: {CortCurso2};\n
Total de cortesias para vendedores comissionados: {CortesiaFinal};\n
Total de dinheiro arrecadado: R${RsTotal};\n
Total de dinheiro das meia-entradas: R${RsMeia};\n
Total de dinheiro das inteiras: R${RsInt};\n
Total de dinheiro dos descontos: R${RsDesc};\n
Ingresso mais vendido: {MaisVendas};\n
Média de idade dos compradores: {round(MediaIdade, 2)}
''')