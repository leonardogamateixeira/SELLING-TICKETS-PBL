NumOpMenu = int(input('''
-------Selecione uma opção---------
1- Para configurar o progama
2- Para usar versão padrão 
3- Para encerrar o progama
'''))
# Essa parte é apenas para qual menu o usuario quer ir
if NumOpMenu == 1:
# Vai para a tela de configuração do progama
    RespOpMenu = 2

    while RespOpMenu == 2:
# da os valores as variaveis
        ingressos = int(input("Digite a quantidade de ingressos: "))
        precoInt = float(input("Digite o preço do ingresso: R$"))
        precoMeia = float(input("Digite o preço da meia-entrada: R$"))
        precoDesc = float(input("Caso aja algum desconto digite-o, caso não digite 0: R$"))
        diasEvento = int(input("Digite quantos dias durará o evento: "))
        print(ingressos)
# usei um if-else apenas por detalhe para mudar a mensagem caso não tenha desconto.
        if precoDesc == 0:
            print(f"Você configurou que o evento durará {diasEvento} dias,a quantidade de ingressos como {ingressos}, o preço á R${precoInt},a meia-entrada á R${precoMeia}\ne não selecionou nenhum desconto, está tudo correto?")
# Adcionei a var RespOpMenu caso o usuario tenha digitado algo errado e queira retornar para a tela de configuração.
            RespOpMenu = int(input("1- Sim \n2- Não\n"))
        else:
            print(f"Você configurou que o evento durará {diasEvento} dias,a quantidade de ingressos como {ingressos}, o preço á R${precoInt},\n a meia-entrada á R${precoMeia} e o desconto como R${precoDesc}, está tudo correto?")
            RespOpMenu = int(input("1- Sim \n2- Não\n")) 

elif NumOpMenu == 2:
# A versão padrão é a do problema proposto
    print("Versão padrão selecionada\n")
    exit()
else:
# Encerra o progama
    print("Encerrando progama...")
    exit()

# Após selecionar ou a versão ou configurar começa a tela de vendas onde eu pré-criei algumas variaveis fora do while para guardar as informações e elas não serem perdidas nos loops
IntVendas = 0
EstudanteVendas = 0
IdosoVendas = 0
CortesiaVenda = 0
DescontoVendas = 0
while ingressos > 0:
    NumOpIng = int(input('''
-------Tela de Vendas------

Selecione um tipo de ingresso:
1- Inteira
2- Meia-entrada(Estudante)
3- Meia-entrada(idoso)
4- Cortesia
5- Descontos
'''))
# o usuario seleciona qual tipo de ingresso será vendido e pergunta quantos ingressos foram vendidos e a soma das idades
    VendasIng = 0
    VendasIngFinal = 0
    VendasIng = int(input("Quantos ingressos foram vendidos? "))
    idadeCompra = int(input("Qual a soma da idade dos clientes? "))
    AddCortesia = VendasIng // 10
# Foram criadas as vars VendaIng(variavel temporaria para guardar os ingressos vendidos por venda), VendasIngFinal(variavel usada para guardar a quantidade total de ingressos vendidos durante o evento) e AddCortesia(para calcular as cortesias por venda)
    if NumOpIng == 1:
        VendasIng += AddCortesia
        ingressos -= VendasIng
        IntVendas += VendasIng
        VendasIngFinal += VendasIng
        print("Compras registradas")

    elif NumOpIng == 2:
        NumOpTipo = int(input("Todas compras foram mostradas a carteira de estudante?\n1-Sim\n2-Não"))
        if NumOpTipo == 1:
            VendasIng += AddCortesia
            ingressos -= VendasIng
            EstudanteVendas += VendasIng
            VendasIngFinal += VendasIng
            print("Compras registradas")
            
    elif NumOpIng == 3:
        NumOpTipo = int(input("Todas compras foram mostradas a carteira de idoso?\n1-Sim\n2-Não"))
        if NumOpTipo == 1:
            VendasIng += AddCortesia
            ingressos -= VendasIng
            IdosoVendas += VendasIng
            VendasIngFinal += VendasIng
            print("Compras registradas")

    elif NumOpIng == 4:
        VendasIng += AddCortesia
        ingressos -= VendasIng
        CortesiaVenda += VendasIng
        VendasIngFinal += VendasIng
        print("As cortesias foram registradas")

    else:
        NumOpTipo = int(input("Todas compras foram mostradas o comprovante para o desconto?\n1-Sim\n2-Não"))
        if NumOpTipo == 1:
            VendasIng += AddCortesia
            ingressos -= VendasIng
            DescontoVendas += VendasIng
            VendasIngFinal += VendasIng
            print("Compras registradas")

RsMeia = ((EstudanteVendas+IdosoVendas)*precoMeia)
RsInt = (IntVendas*precoInt)
RsDesc = (DescontoVendas*precoDesc)
RsTotal = RsMeia + RsInt + RsDesc

if EstudanteVendas > IdosoVendas and EstudanteVendas > IntVendas and EstudanteVendas > DescontoVendas:
    MaisVendas = "Meia-entrada para estudantes"
elif IdosoVendas > EstudanteVendas and IdosoVendas > IntVendas and EstudanteVendas > DescontoVendas:
    MaisVendas = "Meia-entrada para idosos"
elif DescontoVendas > EstudanteVendas and DescontoVendas > IdosoVendas and DescontoVendas > IntVendas:
    MaisVendas = "Descontos"
else:
    MaisVendas = "Inteira"

idadeMedia = idadeCompra / VendasIngFinal

print(f"Ingressos Vendidos: {VendasIngFinal}, ingressos restantes: {ingressos}, EstudanteVendas: {EstudanteVendas}, IdosoVendas: {IdosoVendas}, IntVendas: {IntVendas}, DescontoVendas: {DescontoVendas},Cortesia para DA e convidados:{AddCortesia}, CortesiaVenda: {CortesiaVenda}, Total de dinheiro: R${RsTotal}, Meia: R${RsMeia}, inteira: R${RsInt}, desconto: R${RsDesc}, mais vendido:{MaisVendas}, média de idade:fazer")