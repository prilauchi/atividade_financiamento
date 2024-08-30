emprestimo = float(input("Digite o valor do empréstimo:\n"))
juro = float(input("Digite o valor percentual dos juros anuais:\n"))/100
tempo = int(input("Digite o tempo esperado de pagamento pelo empréstimo em anos:\n"))

valor_final = emprestimo*(1+juro*tempo)

print(f"R${valor_final} é o valor total a ser pago pelo empréstimo.")