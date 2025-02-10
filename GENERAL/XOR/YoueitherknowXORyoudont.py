from pwn import xor

hex = "0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104"
byte = bytes.fromhex(hex)
help = b'crypto{'
key = b''

for i in range(7):
    for keys in range(0,128):
        b = xor(byte[i], keys)
        if (b == help[i:i+1]):
            key += keys.to_bytes(1, "big")
key += b'y'  #the secret key 
        
print(key)
flag = xor(byte, key)
print(flag)



            

    

