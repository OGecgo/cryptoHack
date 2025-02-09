

from cryptography import x509
from cryptography.hazmat.primitives import serialization
from Cryptodome.PublicKey import RSA


pubKey = open('2048b-rsa-example-cert_3220bd92e30015fe4fbeb84a755e7ca5.der', 'rb')
textDer = pubKey.read()

#load certificate Der
textCrt = x509.load_der_x509_certificate(textDer)
#convert certificate to pem
pubKey = textCrt.public_bytes(serialization.Encoding.PEM)


rsa = RSA.importKey(pubKey)

print(rsa.publickey)