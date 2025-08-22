import json # imprimir em JSON
from pprint import pprint # print legível de dict/list
import mean_var_std # módulo com calculate()
from unittest import main # roda os testes

# Saída legível
res = mean_var_std.calculate([0,1,2,3,4,5,6,7,8]) # calcula as estatísticas
pprint(res, width=200, compact=True, sort_dicts=False)  # uma linha por chave, listas internas na mesma linha

# Rodar testes locais
main(module='test_module', exit=False) # executa os testes do arquivo test_module.py