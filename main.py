from Crypto.PublicKey import RSA
from PyPDF2 import PdfFileReader
import hashlib

# ================================================
# Gera par chave publica e privada
# ================================================
keyPair = RSA.generate(bits = 2048)
privateKey = keyPair.exportKey()
publicKey = keyPair.publickey().exportKey()

with open("./rsa_priv.pem", "wb") as f:
    f.write(privateKey)

with open("./rsa_pub.pem", "wb") as f:
    f.write(publicKey)

# ================================================
# Abre arquivo com dados que serão assinados
# ================================================
f = open('data.pdf', mode = 'rb')
pdf = PdfFileReader(f)
data = f.read()

# ================================================
# Assina mensagem
# ================================================

hash512 = hashlib.sha512(data).digest()
hashInt = int.from_bytes(hash512, byteorder = 'big')
signature = pow(hashInt, keyPair.d, keyPair.n)
print("Signature:", hex(signature))

# ================================================
# Verifica assinatura
# ================================================

hash512 = hashlib.sha512(data).digest()
hashInt = int.from_bytes(hash512, byteorder = 'big')
hashFromSignature = pow(signature, keyPair.e, keyPair.n)
print("Signature valid:", hashInt == hashFromSignature)