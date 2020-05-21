import base64

my_str = '49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'
hex_bytes = bytes.fromhex(my_str)
#str_int = int(my_str, 16)
#print("from int: ", base64.b64encode(str_int))

print("hex_bytes: ", hex_bytes)
print(base64.standard_b64encode(hex_bytes))
print(base64.b64encode(hex_bytes))

print(type(hex_bytes))