from pwn import * # pip install pwntools
import base64
import json

r = remote('socket.cryptohack.org', 13377, level = 'debug')

def json_recv():
    line = r.recvline()
    return json.loads(line.decode())

def json_send(hsh):
    request = json.dumps(hsh).encode()
    r.sendline(request)


for i in range(100):

    received = json_recv()

    print("Received type: ")
    print(received["type"])
    print("Received encoded value: ")
    print(received["encoded"])

    send = ""
    if received["type"] == "rot13": # v
        for i in received["encoded"]:
            if i == '_':
                send += i
            elif (ord(i) + 13 > 122):
                send += chr(ord(i) + 13 -26)
            else:
                send += chr(ord(i) + 13)

    elif received["type"] == "utf-8": #v
        for i in received["encoded"]:
            send += chr(i)
            
    elif received["type"] == "bigint": #v
        hex = ""
        j = 0
        for i in received["encoded"]:
            if (j >= 2):
                hex += i
                if len(hex) == 2:
                    send += bytes.fromhex(hex).decode('utf-8')
                    hex = ""
                    continue  
            j += 1
                
    elif received["type"] == "hex": #v
        hex = ""
        for i in received["encoded"]:
            hex += i
            if len(hex) == 2:
                send += bytes.fromhex(hex).decode('utf-8')
                hex = ""
                continue
            
    elif received["type"] == "base64": #v
        send = base64.b64decode(received["encoded"])
        send = send.decode('utf-8')
        
        
    to_send = {
        "decoded": send
    }
    json_send(to_send)

json_recv()
