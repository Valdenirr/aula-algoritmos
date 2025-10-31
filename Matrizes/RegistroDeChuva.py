chuvas = [] 
for i in range(3):  
    linha = []
    print(f"\nCidade {i+1}:")
    for j in range(7):  
        valor = float(input(f"  Dia {j+1} - chuva (mm): "))
        linha.append(valor)
    chuvas.append(linha)

# Exibe a matriz
print("\nMatriz de chuvas (3 cidades x 7 dias):")
for i in range(3):
    print(f"Cidade {i+1}: {chuvas[i]}")


totais = []
for i in range(3):
    total = sum(chuvas[i])  
    totais.append(total)


print("\nTotal de chuva por cidade:")
for i in range(3):
    print(f"Cidade {i+1}: {totais[i]} mm")


maior = max(totais)
indice = totais.index(maior)

print(f"zA cidade com mais chuva foi a Cidade {indice+1}, com {maior} mm no total.")
