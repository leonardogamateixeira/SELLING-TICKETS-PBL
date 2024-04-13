ingressos = int(input("ingresso: "))
EventoFim = 2
while ingressos > 0 and EventoFim > 1:
    
    
    NoIngresso = int(input("Menos ingressos: "))
    ingressos -= NoIngresso
    
    EventoFim = int(input("Gostaria de encerrar o evento?\n1-Sim\n2-Não"))
    print(ingressos, EventoFim)