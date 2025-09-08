#Ian Castanheira e Rafael Russo
cartao = input().strip()
digitos = [int(c) for c in cartao]

soma_impares = sum(digitos[-1::-2])

soma_pares = 0
for d in digitos[-2::-2]:
    dobro = d * 2
    if dobro > 9:
        dobro = (dobro // 10) + (dobro % 10)
    soma_pares += dobro

total = soma_impares + soma_pares

if total % 10 == 0:
    print("Cartão válido")
else:
    print("Cartão inválido")
  
