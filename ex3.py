maior_valor = float('-inf')
menor_valor = float('inf')

print("--- Monitor de Carga da CPU (Versão Simplificada) ---")
print("Digite a carga em % (ex: 85.5) ou '-1' para sair.")
print("----------------------------------------------------")

while True:
    entrada_usuario = input("Digite a carga atual da CPU(%): ")

    carga = float(entrada_usuario)

    if carga == -1:
        break

    if carga < 0 or carga > 100:
        print("O valor tem que ser entre 0 e 100!!")
        continue

    if carga > maior_valor:
        maior_valor = carga

    if carga < menor_valor:
        menor_valor = carga

    if carga > 90:
        print(f"Status: CPU CRÍTICA!!!")
    elif carga >= 81:
        print(f"Status: ATENÇÃO, CPU ALTA!")
    else:
        print(f"Status: CPU normal")

print("\n---------------------------------")
print("Monitoramento encerrado.")

if maior_valor == float('-inf') or menor_valor == float('inf'):
    print("Nenhum valor de carga foi registrado.")
else:
    print(f"Maior valor registrado: {maior_valor:.1f}%")
    print(f"Menor valor registrado: {menor_valor:.1f}%")

print("---------------------------------")