from PIL import Image

def xor(a, b):
    return a ^ b
#take image
flag = Image.open('./flag_7ae18c704272532658c10b5faad06d74.png').convert("RGB")
lemur = Image.open('./lemur_ed66878c338e662d3473f0d98eedbd0d.png').convert("RGB")

#take pixels
pixFlag = flag.load()
pixLemur = lemur.load()

#xor every pixel
for i in range(flag.size[0]):
    for j in range(flag.size[1]):
        r = xor(pixFlag[i, j][0], pixLemur[i, j][0])
        g = xor(pixFlag[i, j][1], pixLemur[i, j][1])
        b = xor(pixFlag[i, j][2], pixLemur[i, j][2])
        newColor = (r, g, b)
        pixFlag[i, j] = newColor

#save image
flag.save('new_flag.png')