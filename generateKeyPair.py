import hashlib
from PyPDF2 import PdfFileReader

f = open('data.pdf', mode = 'rb')
pdf = PdfFileReader(f)
print(pdf.getDocumentInfo())

data = f.read()
hashMD5 = hashlib.md5(data).hexdigest()
hash512 = hashlib.sha512(data).hexdigest()

print(hashMD5)
print(hash512)

f.close()