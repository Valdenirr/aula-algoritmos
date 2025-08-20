def login(senha123):
    tentativas = 0
    while tentativas < 3:
        senha = input('Digite a senha:')
        if senha == senha123:
            print('Bem-vindo!')
            return 'acesso permitido'
        else:
            tentativas += 1
            print(f'tentativa {tentativas} de 3')
    return 'Acesso Bloqueado'

print(login('senha123'))