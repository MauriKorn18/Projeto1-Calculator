# This entrypoint file to be used in development. Start by reading README.md
import json
import mean_var_std
from unittest import main as unittest_main

# Saída legível
print(json.dumps(mean_var_std.calculate([0,1,2,3,4,5,6,7,8]), indent=2))

# Rodar testes locais
main(module='test_module', exit=False)