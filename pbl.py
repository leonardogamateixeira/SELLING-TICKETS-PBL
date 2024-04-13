# Essa parte é apenas para qual menu o usuario quer ir
NumOpMenu = int(input('''
-------Selecione uma opção---------
1- Para configurar o progama
2- Para usar versão padrão(Evento EngComp da UEFS)
3- Para encerrar o progama
'''))

match NumOpMenu:
# Vai para a tela de configuração do progama

    case 1:
        RespOpMenu = 2
        while RespOpMenu == 2:           
# Case 1, o progama será configurado e depois irá para a tela de vendas
            ingressos = int(input("Digite a quantidade de ingressos: "))
            precoInt = float(input("Digite o preço do ingresso: R$"))
            precoMeia = float(input("Digite o preço da meia-entrada: R$"))
            precoDesc = float(input("Caso aja algum desconto digite-o, caso não digite 0: R$"))

            print(f"Você configurou a quantidade de ingressos como {ingressos}, o preço á R${precoInt},\n a meia-entrada á R${precoMeia} e o desconto como R${precoDesc}, está tudo correto?")
            RespOpMenu = int(input("1- Sim \n2- Não\n")) 
# Adcionei a var RespOpMenu caso o usuario tenha digitado algo errado e queira retornar para a tela de configuração. 
    case 2:
# A versão do problema proposto vai ser selecionada e as os valores serão atribuidos as variaveis
        print("Versão padrão selecionada\n")
        ingressos = 2000
        precoInt = 30      
        precoMeia = 15
        precoDesc = 10
    case 3:
        print("Encerrando progama")
        exit()
    
    case _:
        print("Opção invalida\nEncerrando progama")
        exit()

# Após selecionar ou a versão ou configurar começa a tela de vendas onde eu pré-criei algumas variaveis fora do while para guardar as informações e elas não serem perdidas nos loops

IntVendas = 0
EstudanteVendas = 0
IdosoVendas = 0
CortesiaVenda = 0
DescontoVendas = 0
EventoFim = 2

while ingressos > 0 and EventoFim > 1:
    NumOpIng = int(input('''
-------Tela de Vendas------

Selecione um tipo de ingresso:
1- Inteira
2- Meia-entrada(Estudante)1
3- Meia-entrada(idoso)
4- Cortesia
5- Descontos
'''))
# o usuario seleciona qual tipo de ingresso será vendido e pergunta quantos ingressos foram vendidos e soma suas idades com o uma estrutura de repetição, que repetira a pergunta de idade para cada ingresso que foi vendido.
    VendasIng = 0
    VendasIng = int(input("Quantos ingressos foram vendidos? "))
    IdadeSoma = 0
    for idade in range(0,VendasIng):
        idade = int(input("Digite a idade de cada cliente: "))
        IdadeSoma += idade

    Cortesia = VendasIng // 10

    match NumOpIng:
#inteira
        case 1:
            ingressos -= VendasIng
            IntVendas += VendasIng
#meia-estudante
        case 2:
            NumOpTipo = int(input("Todas compras foram mostradas a carteira de estudante?\n1-Sim\n2-Não"))
            if NumOpTipo == 1:
                ingressos -= VendasIng
                EstudanteVendas += VendasIng
            else:
                comprovante = 0
                print("Garanta que todas as compras sejam comprovadas antes de continuar com o cadastro por favor.")
#meia-idoso
        case 3:
            NumOpTipo = int(input("Todas compras foram mostradas a carteira idoso?\n1-Sim\n2-Não"))
            if NumOpTipo == 1:
                ingressos -= VendasIng
                EstudanteVendas += VendasIng
            else:
                comprovante = 0
                print("Garanta que todas as compras sejam comprovadas antes de continuar com o cadastro por favor.")
#desconto
        case 4:
            NumOpTipo = int(input("Todas compras foram mostradas o devido comprovante de desconto?\n1-Sim\n2-Não"))
            if NumOpTipo == 1:
                ingressos -= VendasIng
                EstudanteVendas += VendasIng
            else:
                comprovante = 0
                print("Garanta que todas as compras sejam comprovadas antes de continuar com o cadastro por favor.")
    if (ingressos - Cortesia) > 0:
        ingressos -= Cortesia
        print("Compras registradas!")
        print(f"Ainda restam {ingressos} ingressos")
    else:
        print("Acabaram os ingressos, por tanto as cortesias não puderam ser adcionadas")

    EventoFim = int(input("Gostaria de encerrar o evento?\n1-Sim\n2-Não"))




RsMeia = ((EstudanteVendas+IdosoVendas)*precoMeia)
RsInt = (IntVendas*precoInt)
RsDesc = (DescontoVendas*precoDesc)
RsTotal = RsMeia + RsInt + RsDesc

VendasIngFinal = IntVendas + EstudanteVendas + IdosoVendas + DescontoVendas + Cortesia

MediaIdade = IdadeSoma / VendasIngFinal

if EstudanteVendas > IdosoVendas and EstudanteVendas > IntVendas and EstudanteVendas > DescontoVendas:
    MaisVendas = "Meia-entrada para estudantes"
elif IdosoVendas > EstudanteVendas and IdosoVendas > IntVendas and EstudanteVendas > DescontoVendas:
    MaisVendas = "Meia-entrada para idosos"
elif DescontoVendas > EstudanteVendas and DescontoVendas > IdosoVendas and DescontoVendas > IntVendas:
    MaisVendas = "Descontos"
else:
    MaisVendas = "Inteira"



print(f'''
Total de ingressos Vendidos: {VendasIngFinal};\n 
Ingressos restantes: {ingressos};\n 
Total de meia-entradas para estudantes vendidas: {EstudanteVendas};\n
Total de meia-entradas para Idosos vendidas: {IdosoVendas};\n
Total de inteiras vendidas: {IntVendas};\n
Total de descontos vendidos: {DescontoVendas};\n
Cortesias para DA e convidados: {Cortesia};\n
Total de dinheiro arrecadado: R${RsTotal};\n
Total de dinheiro das meia-entradas: R${RsMeia};\n
Total de dinheiro das inteiras: R${RsInt};\n
Total de dinheiro das descontos: R${RsDesc};\n
Ingresso mais vendido: {MaisVendas};\n
Média de idade dos compradores: {MediaIdade}
''')