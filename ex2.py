soma = 0
soma_par = 0
soma_impar = 0

cont_par = 0 
cont_impar = 0

while True:
    
    number = int(input("Digite um número: "))
    soma += number

    if number == 0:
        break
    
    if  number % 2 == 0:
        soma_par += number
        cont_par += 1
    else:
        soma_impar += number
        cont_impar += 1

media_par = 0
if cont_par > 0:
    media_par = soma_par / cont_par
    
media_impar = 0
if cont_impar > 0:
    media_impar = soma_impar / cont_impar    



print("-----------------------------------------")
print(f"A soma dos números digitados é : {soma}")
print(f"A soma dos números pares é : {soma_par}")
print(f"A média dos números pares é : {media_par:.2f}")
print(f"A soma dos números ímpares é : {soma_impar}")
print(f"A média dos números ímpares é : {media_impar:.2f}")

if media_par > media_impar:
    print("A maior média é dos números pares!")
elif media_impar > media_par:
    print("A maior média é dos números ímpares!")
else:
    print("As médias são iguais!!")