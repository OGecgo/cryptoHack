encode = "label"
key = 13

decode = ""
for i in encode:
    decode += chr(ord(i) ^ key)


print(decode)
