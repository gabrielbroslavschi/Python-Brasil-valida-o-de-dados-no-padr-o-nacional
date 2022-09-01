import re
from telefonesBr import TelefonesBr

"""padrao = "\w{5,50}@\w{3,10}.\w{2,3}.\w{2,3}"
padrao1 = "\w{5,50}@[a-z]{3,10}.com.br"
padrao2_molde = "(xx)aaaa-wwwww"
padrao2 = "[0-9]{2}[0-9]{4,5}-[0-9]{4}"


texto = "gabriel@gmail.com.br"
texto2 = "eu gosto do numero 1112345-6789"

resposta = re.search(padrao2, texto2)

print(resposta.group())
"""




telefone = "551195302-5599"

telefone_objeto = TelefonesBr(telefone)
"""padrao = "([0-9]{2,3})?([0-9]{2})?([0-9]{4,5})-([0-9]{4})"
resposta = re.search(padrao, telefone)
print(resposta.group())"""

print(telefone_objeto)