#Controle Participação em um evento

def registro_presenças():
   presenças_eventos = {
    'Palestra': ["Ana", "Carlos", "Marina"],
    'Workshop': ["Carlos", "João", "Ana"],
    'Mesa-redonda': ["Marina", "João", "Paula"]
   } 
   return presenças_eventos

def participou_todas_atividades(presenças_eventos):
   resultado = []
   lista_palestra = presenças_eventos['Palestra']
   lista_workshop = presenças_eventos['Workshop']
   lista_Mesa_redonda = presenças_eventos['Mesa-redonda']
   for pessoa in lista_palestra:
      if pessoa in lista_workshop and pessoa in lista_Mesa_redonda:
         resultado.append(pessoa)
   return resultado

def apensa_uma_atividade(presenças_eventos):
   compareceu_uma_vez = []
   contagem = {}
   for atividade in presenças_eventos:
    lista_pessoas = presenças_eventos[atividade]
    for pessoa in lista_pessoas:
       if pessoa in contagem:
          contagem[pessoa] += 1
       else:
          contagem[pessoa] = 1
   for pessoa, quantidade in contagem.items():
      if quantidade == 1:
         compareceu_uma_vez.append(pessoa)
   return compareceu_uma_vez

def nomes_unicos(presenças_eventos):
   nomes = []
   for nome in presenças_eventos:
      lista_nomes = presenças_eventos[nome]
      for pessoas in lista_nomes:
         nomes.append(pessoas)
         set(nomes)
   lista_de_nomes = list(set(nomes))
   return lista_de_nomes

def participantes_distintos(presenças_eventos):
   nomes_distintos = nomes_unicos(presenças_eventos)
   return len(nomes_distintos)
   

def main():
   dados = registro_presenças()
   todas_atividades = participou_todas_atividades(dados)
   uma_atividade = apensa_uma_atividade(dados)
   nomes = nomes_unicos(dados)
   quantidade_participantes = participantes_distintos(dados)
   print(f'As pessoas que participaram de todos as atividades foram: {todas_atividades}')
   print(f'Essas foram as pessoas que participaram só de uma atividade: {uma_atividade}')
   print(f'Os nomes únicos de todos participantes são: {nomes}')
   print(f'O total dos participantes distintos foram: {quantidade_participantes}')

main()   