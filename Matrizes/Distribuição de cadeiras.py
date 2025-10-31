sala = []

for i in range(5):  
    fila = []
    for j in range(6):  # 6 cadeiras
        status = input(f"Fila {i+1}, Cadeira {j+1} está ocupada (X) ou livre (O)? ").upper()
        fila.append(status)
    sala.append(fila)

print("\nDistribuição das Cadeiras:")
for fila in sala:
    print(fila)
