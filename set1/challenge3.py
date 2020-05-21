import math
import sys 

def containsAny(str, set):
    """ Check whether sequence str contains ANY of the items in set. """
    return 1 in [c in str for c in set]

def check_encoded(in_int, test_char, num_bytes):
    byte_key = test_char.to_bytes(1, "big") * num_bytes
    int_key = int.from_bytes(byte_key, 'big')
    res = in_int ^ int_key
    res_bytes = res.to_bytes(num_bytes, 'big')
    bad_chars = "@#$%^&*`~|\\"
    if containsAny(str(res_bytes), bad_chars):
        return False, None
    else:
        return(True, res_bytes)
    

my_str = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"
print(len(my_str))
num_bytes = int(len(my_str)/2)
print(num_bytes)

my_str_int = int(my_str, 16)
for i in range(256):
    x,y = check_encoded(my_str_int, i, num_bytes)

    if x:
        print(i, y)

    """
    print(i)
    byte_key = i.to_bytes(1, "big") * num_bytes
    int_key = int.from_bytes(byte_key, 'big')
    res = my_str_int ^ int_key
    res_bytes = res.to_bytes(num_bytes, 'big')
    print(res_bytes)
    """

#Read all the output and check "b"Cooking MC's like a pound of bacon"" for i=88

