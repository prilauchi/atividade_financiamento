nome_cliente = input("Digite seu nome : ")
valor_financiamento = float(input("Digite o valor do financiamento estudantil : "))
parcelamento = int(input("Digite a quantidade de parcelas : "))
valor_parcelamento = (valor_financiamento / parcelamento)

print(f"Olá {nome_cliente} você deseja financiar o valor de: {valor_financiamento} em {parcelamento}, vai ficar o valor de : {valor_parcelamento}")

