# Autenticação Hashlib
1. [Requisitos](#requisitos)
2. [Uso](#uso)
3. [Instruções](#instruções)


## Requisitos

``` python
pip install pycryptodome
```

## Uso

- Imports
``` python
import hashlib
from PyPDF2 import PdfFileReader
```

- Abertura do arquivo
``` python
f = open('data.pdf', mode = 'rb')
pdf = PdfFileReader(f)
print(pdf.getDocumentInfo())
```

- Criação da hash
``` python
data = f.read()
hashMD5 = hashlib.md5(data).digest()
hash512 = hashlib.sha512(data).digest()
```

- Fechar arquivo
``` python
f.close()
```

## Instruções

``` python
python main.py
```