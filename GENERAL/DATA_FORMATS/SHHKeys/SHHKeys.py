from cryptography.hazmat.primitives import  serialization
from Cryptodome.PublicKey import RSA

ssh = open('./.ssh/bruce_rsa_6e7ecd53b443a97013397b1a1ea30e14.pub', 'rb')
ssh = ssh.read()


pubKey = serialization.load_ssh_public_key(ssh)
pem = pubKey.public_bytes(serialization.Encoding.PEM, serialization.PublicFormat.SubjectPublicKeyInfo)

rsa = RSA.import_key(pem)
print(rsa.publickey)