from Cryptodome.PublicKey import RSA
from Cryptodome.Hash import SHA256

pem = open('transparency_afff0345c6f99bf80eab5895458d8eab.pem', 'rb')
pem = pem.read()

rsa = RSA.import_key(pem)


pubKeyDer = rsa.export_key(format="DER")
#search in format sha256
sha256_hash = SHA256.new(pubKeyDer).hexdigest()
print(sha256_hash)

#https://crt.sh/?spkisha256=29ab37df0a4e4d252f0cf12ad854bede59038fdd9cd652cbc5c222edd26d77d2