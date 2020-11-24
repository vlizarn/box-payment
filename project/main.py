import sys #Importa o modulo de sys

#Função de caixa de Pagamento
def caixa_de_pagamento(Preço, Pagamento):
    
    # Notas de 5, 10, 20, 50, 100, 200 e 500 euros. Moedas de 1 e 2 euros.
    Valores = [1, 2, 5, 10, 20, 50, 100, 200, 500]

    if(Pagamento >= Preço and Pagamento in Valores[0:9]):
        
        #Devolução (Troco).
        Troco = round(float(Pagamento - Preço) * 100 ) / 100

        #Princípais variáveis de Troco de moedas.
        TrocoC1 = int(Troco / 2)
        TrocoC2 = int(Troco) - (TrocoC1 * 2)
        TrocoC3 = int(((Troco) - int(Troco)) * 100 / 50)
        TrocoC4 = 0
        TrocoC5 = 0
        TrocoC6 = 0
        TrocoC7 = 0
        TrocoC8 = 0

        #Se for menor que 50 cêntimos.
        if(TrocoC3 < 1):
            TrocoC4 = int(round(int(round(((Troco) - int(Troco)) * 100) / 20 ) - (TrocoC3 * 0.5)))
            TrocoC5 = int(round(int(round(((Troco) - int(Troco)) * 100) / 20  * 2.01) - TrocoC4 * 2))
            TrocoC6 = int((((Troco * 10) - int(Troco * 10)) * 10) / 5)
        
            #Se for maior ou igual que 5 cêntimos.
            if(TrocoC6 >= 1):
                TrocoC7 = int(round((((Troco * 10) - int(Troco * 10)) * 10) - 5) / 2)
                TrocoC8 = int(round(round(((Troco * 10) - int(Troco * 10)) * 10) - 5) / (2) + 0.5) - TrocoC7
     
            #Se for menor que 5 cêntimos.
            elif(TrocoC6 < 1):
                TrocoC7 = int(round((((Troco * 10) - int(Troco * 10)) * 10)) / 2)
                TrocoC8 = int(round(round(((Troco * 10) - int(Troco * 10)) * 10) + 2) / (2) + 0.5) - (TrocoC7 + 1)
                
            #Se possuir alguma falha na Operação.
            else:
                print("Falha na Operação!")
                
        #Se for maior ou igual que 50 cêntimos.
        elif(TrocoC3 >= 1):
            TrocoC4 = int(round((((Troco) - int(Troco)) - 0.50) * 100) / 20)
            TrocoC5 = int(round(round((((Troco) - int(Troco)) - 0.50) * 100) / 20 * 1.01) - TrocoC4)
            TrocoC6 = int((((Troco * 10) - int(Troco * 10)) * 10) / 5)
     
            #Se for maior ou igual que 5 cêntimos.
            if(TrocoC6 >= 1):
                TrocoC7 = int(round((((Troco * 10) - int(Troco * 10)) * 10) - 5) / 2)
                TrocoC8 = int(round(round(((Troco * 10) - int(Troco * 10)) * 10) - 5) / (2) + 0.5) - TrocoC7
     
            #Se for menor que 5 cêntimos.
            elif(TrocoC6 < 1):
                TrocoC7 = int(round((((Troco * 10) - int(Troco * 10)) * 10)) / 2)
                TrocoC8 = int(round(round(((Troco * 10) - int(Troco * 10)) * 10) + 2) / (2) + 0.5) - (TrocoC7 + 1)
    
            #Se possuir alguma falha na Operação.
            else:
                print("Falha na Operação!")
            
        #Se possuir alguma falha na Operação.
        else:
            print("Falha na Operação!")

        Trocos = [TrocoC1, TrocoC2, TrocoC3, TrocoC4, TrocoC5, TrocoC6, TrocoC7, TrocoC8]

        #Mostrar os resultados
        print("\nTroco:", Troco)

        print("\nMoedas devolvida(s):\n")
        print(Trocos[0], "moeda(s) de 2 euros.")
        print(Trocos[1], "moeda(s) de 1 euros.")
        print(Trocos[2], "moeda(s) de 50 centimos.")
        print(Trocos[3] ,"moeda(s) de 20 centimos.")
        print(Trocos[4] ,"moeda(s) de 10 centimos.")
        print(Trocos[5] ,"moeda(s) de 5 centimos.")
        print(Trocos[6], "moeda(s) de 2 centimos.")
        print(Trocos[7], "moeda(s) de 1 centimos.\n")

    #Se Pagamento for menor que Preço e o valor do Pagamento é idêntico.
    elif(Pagamento < Preço and Pagamento not in Valores[0:9]):
        print("\nNão pode efetuar o pagamento!")
        print("\nMotivo: Valor do pagamento é invalido e inferior ao preço.\n")
        print("Valor devolvido:", Pagamento,"euro(s).\n")
                    
    #Se Pagamento for menor que Preço e o valor do Pagamento é idêntico.        
    elif(Pagamento < Preço and Pagamento in Valores[0:9]):
        print("\nNão pode efetuar o pagamento!")
        print("\nMotivo: Valor do pagamento é inferior ao preço.")
        print("\nValor devolvido:", Pagamento,"euro(s).")

    #O valor do pagamento não correspondem.
    elif(Pagamento not in Valores[0:9]):
        print("\nNão pode efetuar o pagamento!")
        print("\nMotivo: Valor do pagamento é invalido.\n")
        print("Valor devolvido:", Pagamento,"euro(s).\n")

    #Se possuir alguma falha na Operação.
    else:
        print("Falha na Operação!")

def print_fatura():

    print("                                     CAIXA DE PAGAMENTO")
    print("            Só são aceites valores <1, 2, 5, 10, 20, 50, 100, 200 e 500 euros>\n")
    
    #Introdução dos Valores.
    Preço = input("Introduza um valor: ")
    Pagamento = input("Introduza o pagamento: ")

    #caixa_de_pagamento(1.48, 2)
    caixa_de_pagamento(float(Preço), float(Pagamento))

def main():
    print_fatura()

while True:
    try:
        main()
    except ValueError as Value:
        print("\nUnexpected error: {0}".format(Value))
    except:
        print("\nUnexpected error: ", sys.exc_info()[1])


