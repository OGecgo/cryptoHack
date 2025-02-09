#!/bin/python3

from Cryptodome.PublicKey import RSA

#take rsa key
pubKey = open('privacy_enhanced_mail_1f696c053d76a78c2c531bb013a92d4a.pem')
dataPubKey = pubKey.read()
rsa = RSA.importKey(dataPubKey)

#private key
print (rsa.d)