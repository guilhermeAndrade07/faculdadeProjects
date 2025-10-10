# def calculoArea(base, altura):
#     area = base * altura
#     print(f"A área do retangulo é: {area}")
# 
# base = int(input("Digite o valor da base: "))
# altura = int(input("Digite o valor da altura: "))
# calculoArea(base,altura)


# def calculoImc(peso,altura):
#     imc = peso / (altura**2)
#     print(f"Seu IMC é de {imc}")
#     return imc
# 
# peso = float(input("Digite o seu peso: "))
# altura = float(input("Digite a sua altura: "))
# imc = calculoImc(peso, altura)
# if imc < 18.5:
#     print("Abaixo do peso")
# elif 18.5 <= imc or 25 < imc:
#     print("Peso normal")
# elif 25 <= imc or 30 < imc:
#     print("Sobrepeso")
# else:
#     print("Obesidade")


# def enviar_email(destinatario, mensagem, assunto, remetente=None):
#     print("\n--- Envio de e-mail ---")
#     print(f"Para: {destinatario}")
#     print(f"Assunto: {assunto}")
#     print(f"Mensagem: {mensagem}")
#     if remetente:
#         print(f"Remetente: {remetente}")
#     else:
#         print("Remetente: (não informado)")
#     print("--- E-mail enviado com sucesso! ---")
# 
# dest = input("Destinatário: ")
# msg = input("Mensagem: ")
# ass = input("Assunto: ")
# rem_opcao = input("Deseja informar o remetente? (sim/não): ").lower()
# 
# if rem_opcao == "sim":
#     rem = input("Remetente: ")
#     enviar_email(dest, msg, ass, rem)
# else:
#     enviar_email(dest, msg, ass)


# def temperatura(celsius):
#     fahrenheit = celsius * (9/5) + 32
#     kelvin = celsius + 273.15
#     print("\n-- Temperatura --")
#     print(f"Temperatura em Celsius: {celsius}")
#     print(f"Temperatura em Fahrenheit: {fahrenheit}")
#     print(f"Temperatura em Kelvin: {kelvin}")
# 
# graus = int(input("Digite uma temperatura em Granus Celsius: "))
# temperatura(graus)


# saldo_inicial = 1000
# def sacar(valor, saldo):
#     if valor > saldo:
#         print("Saldo insuficiente para saque!")
#         return saldo
#     else:
#         saldo -= valor
#         print(f"Saque de R${valor} realizado com sucesso.")
#         print(f"Saldo atual: R${saldo}")
#         return saldo
# 
# print(f"Saldo inicial: R${saldo_inicial}")
# valor_saque = float(input("Digite o valor para saque: "))
# saldo_inicial = sacar(valor_saque, saldo_inicial)


# def somar(a, b):
#     print(f"A soma de {a} + {b} = {a+b}")
#     
# def subtrair(a, b):
#     print(f"A subtração de {a} - {b} = {a-b}")
# 
# def multiplicar(a, b):
#     print(f"A multiplicação de {a} * {b} = {a*b}")
# 
# def divisao(a, b):
#     print(f"A divisão de {a} / {b} = {a/b}")
# 
# while True: 
#     print("\n-- CALCULADORA --")
#     operacao = int(input("Selecione qual operação você quer realizar: 1-Soma 2-Subtração 3-Multiplicação 4-Divisão \n"))
#     valorA = int(input("Digite o valor de A: "))
#     valorB = int(input("Digite o valor de B: "))
# 
#     if operacao == 1:
#         somar(valorA,valorB)
#     elif operacao == 2:
#         subtrair(valorA,valorB)
#     elif operacao == 3:
#         multiplicar(valorA,valorB)
#     elif operacao == 4:
#         divisao(valorA,valorB)
#     else:
#         print("Operação Inexistente, tente novamente!!")
# 
#     cont = input("Deseja continuar? (sim/não)\n").lower()
#     if cont == "não":
#         break