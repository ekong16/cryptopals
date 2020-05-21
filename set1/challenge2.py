a = "1c0111001f010100061a024b53535009181c"
b = "686974207468652062756c6c277320657965"

#a = bytes.fromhex(a)
#b = bytes.fromhex(b)

a = int(a, 16)
b = int(b, 16)
xor_ab = a^b 
print(hex(xor_ab))