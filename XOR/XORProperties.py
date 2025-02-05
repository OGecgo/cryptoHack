# KEY1 = a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313
# KEY2 ^ KEY1 = 37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e
# KEY2 ^ KEY3 = c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1
# FLAG ^ KEY1 ^ KEY3 ^ KEY2 = 04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf
def xorBytes (var, key):
    l = bytearray()
    
    #take paraler a and b from var and key
    for a, b in zip(var, key):
        l.append(a ^ b)
        
    return l

            

hex = "a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313"
key1 = bytes.fromhex(hex)

var = "37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e"
var = bytes.fromhex(var)
key2 = xorBytes(key1, var)

var = "c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1"
var = bytes.fromhex(var)
key3 = xorBytes(key2, var)

var = "04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf"
var = bytes.fromhex(var)
a = xorBytes(key2, key3)
b = xorBytes(key1, a)
flag = xorBytes(var, b)

print(flag)