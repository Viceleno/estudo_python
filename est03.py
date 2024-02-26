# Estudo de if, elif, else, e simbologia de comparação

primeiro_valor = input('Digite um valor: ')
segundo_valor = input('Digite segundo valor: ')
int_primeiro = int(primeiro_valor)
int_segundo = int(segundo_valor)
if primeiro_valor > segundo_valor:
  print(f'{primeiro_valor=} é maior que {segundo_valor=}')
elif primeiro_valor == segundo_valor:
  print(f'{primeiro_valor=} é igual ao {segundo_valor=}')
else:
  print(f'{segundo_valor=} é maior que {primeiro_valor=}')
