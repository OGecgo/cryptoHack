
from pwn import xor

hex = "73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d"

byte = bytes.fromhex(hex)

#brudforce
for i in range(0, 128):
    var = xor(byte, i).decode("utf-8")
    print (var[0:6])
    if var[0:6] == "crypto":
        print("----->>>>>>>",var,"<<<<<-------")
    print(var)