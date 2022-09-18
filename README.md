# Autenticação Hashlib

## Uso:

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
hashMD5 = hashlib.md5(data).hexdigest()
hash512 = hashlib.sha512(data).hexdigest()
```

- Fechar arquivo
``` python
f.close()
```