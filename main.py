emprestimo = float(input("Digite o valor do empréstimo:\n"))
juro = float(input("Digite o valor percentual dos juros anuais:\n"))/100
tempo = int(input("Digite o tempo esperado de pagamento pelo empréstimo em anos:\n"))

valor_final = emprestimo*(1+juro*tempo)

print(f"R${valor_final} é o valor total a ser pago pelo empréstimo.")

nome_cliente = input("Digite seu nome : ")
valor_financiamento = float(input("Digite o valor do financiamento estudantil : "))
parcelamento = int(input("Digite a quantidade de parcelas : "))
valor_parcelamento = (valor_financiamento / parcelamento)

print(f"Olá {nome_cliente} você deseja financiar o valor de: {valor_financiamento} em {parcelamento}, vai ficar o valor de : {valor_parcelamento}")

valor = float(input('Digite o valor do pagamento'))
valor_desconto = valor * 20/100
pagamento_antecipado = valor - valor_desconto
print(pagamento_antecipado)
